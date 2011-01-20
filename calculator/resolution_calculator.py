"""
This object is a small tool to allow user to quickly
determine the variance in q  from the 
instrumental parameters.
"""
from instrument import Sample
from instrument import Detector
from instrument import Neutron
from instrument import Aperture
# import math stuffs
from math import pi
from math import sqrt
from math import cos
from math import sin
from math import atan
from math import atan2
from math import pow
from math import asin
from math import tan

import numpy

#Plank's constant in cgs unit
_PLANK_H = 6.62606896E-27
#Gravitational acc. in cgs unit
_GRAVITY = 981.0

class ResolutionCalculator(object):
    """
    compute resolution in 2D
    """
    def __init__(self):
        
        # wavelength
        self.wave = Neutron()
        # sample
        self.sample = Sample()
        # aperture
        self.aperture = Aperture()
        # detector
        self.detector = Detector()
        # 2d image of the resolution
        self.image = []
        # resolutions
        self.sigma_1 = 0
        self.sigma_2 = 0
        self.sigma_1d = 0
        # q min and max
        self.qx_min = -0.3
        self.qx_max = 0.3
        self.qy_min = -0.3
        self.qy_max = 0.3
        # q min and max of the detector
        self.detector_qx_min = -0.3
        self.detector_qx_max = 0.3
        self.detector_qy_min = -0.3
        self.detector_qy_max = 0.3
        # plots
        self.plot = None
        # instrumental params defaults
        self.mass = 0
        self.intensity = 0
        self.wavelength = 0
        self.wavelength_spread = 0
        self.source_aperture_size = []
        self.source2sample_distance = []
        self.sample2sample_distance = []
        self.sample_aperture_size = []
        self.sample2detector_distance = []
        self.detector_pix_size = []
        self.detector_size = []
        # get all the values of the instrumental parameters
        self.get_all_instrument_params()
        
    def compute_and_plot(self, qx_value, qy_value, qx_min, qx_max, 
                          qy_min, qy_max, coord = 'polar'):
        """
        Compute the resolution
        : qx_value: x component of q
        : qy_value: y component of q
        """
        # compute 2d resolution
        _, _, sigma_1, sigma_2 = self.compute(qx_value, qy_value, coord)
        # make image
        image = self.get_image(qx_value, qy_value, sigma_1, sigma_2, 
                               qx_min, qx_max, qy_min, qy_max, coord)
        # plot image
        return self.plot_image(image) 

    def compute(self, qx_value, qy_value, coord = 'polar'):
        """
        Compute the Q resoltuion in || and + direction of 2D
        : qx_value: x component of q
        : qy_value: y component of q
        """
        # make sure to update all the variables need.
        self.get_all_instrument_params()
        # wavelength
        lamb = self.wavelength
   
        if lamb == 0:
            msg = "Can't compute the resolution: the wavelength is zero..." 
            raise RuntimeError, msg
        # wavelength spread
        lamb_spread = self.wavelength_spread
        # Find polar values
        qr_value, phi = self._get_polar_value(qx_value, qy_value)
        # vacuum wave transfer
        knot = 2*pi/lamb
        # scattering angle theta; always true for plane detector
        # aligned vertically to the ko direction
        if qr_value > knot:
            theta = pi/2
        else:
            theta = asin(qr_value/knot)
        # source aperture size
        rone = self.source_aperture_size
        # sample aperture size
        rtwo = self.sample_aperture_size
        # detector pixel size
        rthree = self.detector_pix_size
        # source to sample(aperture) distance
        l_ssa = self.source2sample_distance[0]
        # sample(aperture) to detector distance
        l_sad = self.sample2detector_distance[0]
        # sample (aperture) to sample distance
        l_sas = self.sample2sample_distance[0]
        # source to sample distance
        l_one = l_ssa + l_sas
        # sample to detector distance
        l_two = l_sad - l_sas
        
        # Sample offset correction for l_one and Lp on variance calculation
        l1_cor = (l_ssa * l_two) / (l_sas + l_two)
        lp_cor = (l_ssa * l_two) / (l_one + l_two)
        # the radial distance to the pixel from the center of the detector
        radius = tan(theta)*l_two
        #Lp = l_one*l_two/(l_one+l_two)
        # default polar coordinate
        comp1 = 'radial'
        comp2 = 'phi'
        # in the case of the cartesian coordinate
        if coord == 'cartesian':
            comp1 = 'x'
            comp2 = 'y'

        # sigma in the radial/x direction
        # for source aperture
        sigma_1  = self.get_variance(rone, l1_cor, phi, comp1)
        # for sample apperture
        sigma_1 += self.get_variance(rtwo, lp_cor, phi, comp1)
        # for detector pix
        sigma_1 += self.get_variance(rthree, l_two, phi, comp1)
        # for gravity term
        sigma_1 +=  self.get_variance_gravity(l_ssa, l_sad, lamb, lamb_spread, 
                             phi, comp1, 'on')  
        # for wavelength spread
        # reserve for 1d calculation
        sigma_wave_1 = self.get_variance_wave(radius, l_two, lamb_spread, 
                                          phi, comp1, 'on')
        # for 1d
        variance_1d_1 = sigma_1/2 +sigma_wave_1
        # normalize
        variance_1d_1 = knot*knot*variance_1d_1/12
        
        # for 2d
        sigma_1 += sigma_wave_1
        # normalize
        sigma_1 = knot*sqrt(sigma_1/12)

        # sigma in the phi/y direction
        # for source apperture
        sigma_2  = self.get_variance(rone, l1_cor, phi, comp2)
        # for sample apperture
        sigma_2 += self.get_variance(rtwo, lp_cor, phi, comp2)
        # for detector pix
        sigma_2 += self.get_variance(rthree, l_two, phi, comp2)
        # for gravity term
        sigma_2 +=  self.get_variance_gravity(l_ssa, l_sad, lamb, lamb_spread, 
                             phi, comp2, 'on')
        # for wavelength spread
        # reserve for 1d calculation
        sigma_wave_2 = self.get_variance_wave(radius, l_two, lamb_spread, 
                                          phi, comp2, 'on') 
        # for 1d
        variance_1d_2 = sigma_2/2 +sigma_wave_2
        # normalize
        variance_1d_2 = knot*knot*variance_1d_2/12
        
        # for 2d
        sigma_2 += sigma_wave_2
        # normalize
        sigma_2 =  knot*sqrt(sigma_2/12)

        # set sigmas
        self.sigma_1 = sigma_1
        self.sigma_2 = sigma_2
        
        self.sigma_1d = sqrt(variance_1d_1 + variance_1d_2)
        return qr_value, phi, sigma_1, sigma_2
    
    def get_image(self, qx_value, qy_value, sigma_1, sigma_2,
                  qx_min, qx_max, qy_min, qy_max, coord = 'polar'): 
        """
        Get the resolution in polar coordinate ready to plot
        : qx_value: qx_value value
        : qy_value: qy_value value
        : sigma_1: variance in r direction
        : sigma_2: variance in phi direction
        : coord: coordinate system of image, 'polar' or 'cartesian'
        """
        # Get  qx_max and qy_max...
        output = self._get_detector_qxqy_pixels()
        # Set qx_value/qy_value min/max
        #qx_min = self.qx_min
        #qx_max = self.qx_max
        #qy_min = self.qy_min
        #qy_max = self.qy_max

        # Find polar values
        qr_value, phi = self._get_polar_value(qx_value, qy_value)
        
        # Check whether the q value is within the detector range
        msg = "Invalid input: Q value out of the detector range..."
        if qx_min < self.qx_min:
            self.qx_min = qx_min
            #raise ValueError, msg
        if qx_max > self.qx_max:
            self.qx_max = qx_max
            #raise ValueError, msg
        if qy_min < self.qy_min:
            self.qy_min = qy_min
            #raise ValueError, msg
        if qy_max > self.qy_max:
            self.qy_max = qy_max
            #raise ValueError, msg

        # Make an empty graph in the detector scale
        dx_size = (self.qx_max - self.qx_min) / (1000 - 1)
        dy_size = (self.qy_max - self.qy_min) / (1000 - 1)
        x_val = numpy.arange(self.qx_min, self.qx_max, dx_size)
        y_val = numpy.arange(self.qy_max, self.qy_min, -dy_size)
        q_1, q_2 = numpy.meshgrid(x_val, y_val)

        # check whether polar or cartesian
        if coord == 'polar':
            q_1, q_2 = self._rotate_z(q_1, q_2, phi)
            qc_1 = qr_value
            qc_2 = 0.0
        else:
            # catesian coordinate
            # qx_center
            qc_1 = qx_value
            # qy_center
            qc_2 = qy_value
            
        # Calculate the 2D Gaussian distribution image
        image = self._gaussian2d(q_1, q_2, qc_1, qc_2, sigma_1, sigma_2)
        # Add it if there are more than one inputs.
        if len(self.image) > 0:
            self.image += image
        else:
            self.image = image

        return self.image
    
    def plot_image(self, image):
        """
        Plot image using pyplot
        : image: 2d resolution image 
        
        : return plt: pylab object
        """
        import matplotlib.pyplot as plt

        self.plot = plt
        plt.xlabel('$\\rm{Q}_{x} [A^{-1}]$')
        plt.ylabel('$\\rm{Q}_{y} [A^{-1}]$')
        # Max value of the image
        max = numpy.max(image)
        # Image
        im = plt.imshow(image, 
                extent = [self.qx_min, self.qx_max, self.qy_min, self.qy_max])

        # bilinear interpolation to make it smoother
        im.set_interpolation('bilinear')

        return plt
    
    def reset_image(self):
        """
        Reset image to default (=[])
        """
        self.image = []
        
    def get_variance(self, size = [], distance = 0, phi = 0, comp = 'radial'):
        """
        Get the variance when the slit/pinhole size is given
        : size: list that can be one(diameter for circular) 
                or two components(lengths for rectangular)
        : distance: [z, x] where z along the incident beam, x // qx_value
        : comp: direction of the sigma; can be 'phi', 'y', 'x', and 'radial'
        
        : return variance: sigma^2
        """   
        # check the length of size (list)
        len_size = len(size)
        
        # define sigma component direction
        if comp == 'radial':
            phi_x = cos(phi)
            phi_y = sin(phi)
        elif comp == 'phi':
            phi_x = sin(phi)
            phi_y = cos(phi)
        elif comp == 'x':
            phi_x = 1
            phi_y = 0
        elif comp == 'y':
            phi_x = 0
            phi_y = 1
        else:
            phi_x = 0
            phi_y = 0
        # calculate each component
        # for pinhole w/ radius = size[0]/2
        if len_size == 1:
            x_comp = (0.5 * size[0]) * sqrt(3)
            y_comp = 0
        # for rectangular slit
        elif len_size == 2:
            x_comp = size[0] * phi_x 
            y_comp = size[1] * phi_y
        # otherwise
        else:
            raise ValueError, " Improper input..."
        # get them squared  
        sigma  = x_comp * x_comp 
        sigma += y_comp * y_comp
        # normalize by distance
        sigma /= (distance * distance)

        return sigma

    def get_variance_wave(self, radius, distance, spread, phi, 
                          comp = 'radial', switch = 'on'):
        """
        Get the variance when the wavelength spread is given
        
        : radius: the radial distance from the beam center to the pix of q
        : distance: sample to detector distance
        : spread: wavelength spread (ratio)
        : comp: direction of the sigma; can be 'phi', 'y', 'x', and 'radial'
        
        : return variance: sigma^2
        """
        if switch.lower() == 'off':
            return 0
        # check the singular point
        if distance == 0 or comp == 'phi':
            return 0
        else:
            # calculate sigma^2
            sigma = 2 * pow(radius/distance*spread, 2)
            if comp == 'x':
                sigma *= (cos(phi)*cos(phi))
            elif comp == 'y':
                sigma *= (sin(phi)*sin(phi))
            else:
                sigma *= 1          
                
            return sigma

    def get_variance_gravity(self, s_distance, d_distance, wavelength, spread, 
                             phi, comp = 'radial', switch = 'on'):
        """
        Get the variance from gravity when the wavelength spread is given
        
        : s_distance: source to sample distance
        : d_distance: sample to detector distance
        : wavelength: wavelength
        : spread: wavelength spread (ratio)
        : comp: direction of the sigma; can be 'phi', 'y', 'x', and 'radial'
        
        : return variance: sigma^2
        """
        if switch.lower() == 'off':
            return 0
        if self.mass == 0.0:
            return 0
        # check the singular point
        if d_distance == 0 or comp == 'x':
            return 0
        else:
            # neutron mass in cgs unit
            self.mass = self.get_neutron_mass()
            # plank constant in cgs unit
            h_constant = _PLANK_H
            # gravity in cgs unit
            gravy = _GRAVITY
            # m/h
            m_over_h = self.mass /h_constant
            # A value
            a_value = d_distance * (s_distance + d_distance)
            a_value *= pow(m_over_h / 2, 2)
            a_value *= gravy
            # unit correction (1/cm to 1/A) for A and d_distance below
            a_value *= 1.0E-16
            
            # calculate sigma^2
            sigma = pow(a_value / d_distance, 2)
            sigma *= pow(wavelength, 4)
            sigma *= pow(spread, 2)
            sigma *= 8
            
            # only for the polar coordinate
            if comp == 'radial':
                sigma *= (sin(phi) * sin(phi))
            elif comp == 'phi':
                sigma *= (cos(phi) * cos(phi))
            
            return sigma
        
    def get_intensity(self):
        """
        Get intensity
        """
        return self.wave.intensity

    def get_wavelength(self):
        """
        Get wavelength
        """
        return self.wave.wavelength
    
    def get_wavelength_spread(self):
        """
        Get wavelength spread
        """
        return self.wave.wavelength_spread
    
    def get_neutron_mass(self):
        """
        Get Neutron mass
        """
        return self.wave.mass
    
    def get_source_aperture_size(self):
        """
        Get source aperture size
        """
        return self.aperture.source_size
    
    def get_sample_aperture_size(self):
        """
        Get sample aperture size
        """
        return self.aperture.sample_size
    
    def get_detector_pix_size(self):
        """
        Get detector pixel size
        """
        return self.detector.pix_size
    
    def get_detector_size(self):
        """
        Get detector size
        """
        return self.detector.size   
     
    def get_source2sample_distance(self):
        """
        Get detector source2sample_distance
        """
        return self.aperture.sample_distance
    
    def get_sample2sample_distance(self):
        """
        Get detector sampleslitsample_distance
        """
        return self.sample.distance
    
    def get_sample2detector_distance(self):
        """
        Get detector sample2detector_distance
        """
        return self.detector.distance
    
    def set_intensity(self, intensity):
        """
        Set intensity
        """
        self.wave.set_intensity(intensity)
   
    def set_wavelength(self, wavelength):
        """
        Set wavelength
        """
        self.wave.set_wavelength(wavelength)
    
    def set_wavelength_spread(self, wavelength_spread):
        """
        Set wavelength spread
        """
        self.wave.set_wavelength_spread(wavelength_spread)
    
    def set_source_aperture_size(self, size):
        """
        Set source aperture size
        
        : param size: [dia_value] or [x_value, y_value]
        """        
        if len(size) < 1 or len(size) > 2:
            raise RuntimeError, "The length of the size must be one or two."
        self.aperture.set_source_size(size)
        
    def set_neutron_mass(self, mass):
        """
        Set Neutron mass
        """
        self.wave.set_mass(mass)
        
    def set_sample_aperture_size(self, size):
        """
        Set sample aperture size
        
        : param size: [dia_value] or [xheight_value, yheight_value]
        """
        if len(size) < 1 or len(size) > 2:
            raise RuntimeError, "The length of the size must be one or two."
        self.aperture.set_sample_size(size)
    
    def set_detector_pix_size(self, size):
        """
        Set detector pixel size
        """
        self.detector.set_pix_size(size)
        
    def set_detector_size(self, size):
        """
        Set detector size in number of pixels
        : param size: [pixel_nums] or [x_pix_num, yx_pix_num]
        """
        self.detector.set_size(size)
        
    def set_source2sample_distance(self, distance):
        """
        Set detector source2sample_distance
        
        : param distance: [distance, x_offset]
        """
        if len(distance) < 1 or len(distance) > 2:
            raise RuntimeError, "The length of the size must be one or two."
        self.aperture.set_sample_distance(distance)

    def set_sample2sample_distance(self, distance):
        """
        Set detector sample_slit2sample_distance
        
        : param distance: [distance, x_offset]
        """
        if len(distance) < 1 or len(distance) > 2:
            raise RuntimeError, "The length of the size must be one or two."
        self.sample.set_distance(distance)
   
    def set_sample2detector_distance(self, distance):
        """
        Set detector sample2detector_distance
        
        : param distance: [distance, x_offset]
        """
        if len(distance) < 1 or len(distance) > 2:
            raise RuntimeError, "The length of the size must be one or two."
        self.detector.set_distance(distance)
        
    def get_all_instrument_params(self):
        """
        Get all instrumental parameters
        """
        self.intensity = self.get_intensity()
        self.wavelength = self.get_wavelength()
        self.wavelength_spread = self.get_wavelength_spread()
        self.mass = self.get_neutron_mass()
        self.source_aperture_size = self.get_source_aperture_size()
        self.sample_aperture_size = self.get_sample_aperture_size()
        self.detector_pix_size = self.get_detector_pix_size()
        self.detector_size = self.get_detector_size()
        self.source2sample_distance = self.get_source2sample_distance()
        self.sample2sample_distance = self.get_sample2sample_distance()
        self.sample2detector_distance = self.get_sample2detector_distance()


          
    def _rotate_z(self, x_value, y_value, theta= 0.0):
        """
        Rotate x-y cordinate around z-axis by theta
        : x_value: numpy array of x values
        : y_value: numpy array of y values
        : theta: angle to rotate by in rad
        
        :return: x_prime, y-prime
        """        
        # rotate by theta
        x_prime = x_value * cos(theta) + y_value * sin(theta)
        y_prime =  -x_value * sin(theta) + y_value * cos(theta)
    
        return x_prime, y_prime
    
    def _gaussian2d(self, x_val, y_val, x0_val, y0_val, sigma_x, sigma_y):
        """
        Calculate 2D Gaussian distribution
        : x_val: x value
        : y_val: y value
        : x0_val: mean value in x-axis
        : y0_val: mean value in y-axis
        : sigma_x: variance in x-direction
        : sigma_y: variance in y-direction
        
        : return: gaussian (value)
        """
        # call gaussian1d 
        gaussian  = self._gaussian1d(x_val, x0_val, sigma_x)
        gaussian *= self._gaussian1d(y_val, y0_val, sigma_y)
 
        # normalizing factor correction
        if sigma_x != 0 and sigma_y != 0:
            gaussian *= sqrt(2 * pi)
        return gaussian

    def _gaussian1d(self, value, mean, sigma):
        """
        Calculate 1D Gaussian distribution
        : value: value
        : mean: mean value
        : sigma: variance 
        
        : return: gaussian (value)
        """
        # default
        gaussian = 1.0
        if sigma != 0:
            # get exponent
            nu_value = (value - mean) / sigma
            nu_value *= nu_value
            nu_value *= -0.5
            gaussian *= numpy.exp(nu_value)
            gaussian /= sigma
            # normalize
            gaussian /= sqrt(2 * pi)
            
        return gaussian
    
    def _atan_phi(self, qy_value, qx_value):
        """
        Find the angle phi of q on the detector plane for qx_value, qy_value given
        : qx_value: x component of q
        : qy_value: y component of q
        
        : return phi: the azimuthal angle of q on x-y plane
        """
        # default
        phi = 0
        # ToDo: This is misterious - sign???
        #qy_value = -qy_value
        # Take care of the singular point
        if qx_value == 0:
            if qy_value > 0:
                phi = pi / 2
            elif qy_value < 0:
                phi = -pi / 2
            else:
                phi = 0
        else:
            # the angle
            phi = atan2(qy_value, qx_value)

        return phi

    def _get_detector_qxqy_pixels(self):
        """
        Get the pixel positions of the detector in the qx_value-qy_value space
        """
        
        # update all param values
        self.get_all_instrument_params()
        
        # wavelength
        wavelength = self.wavelength
        # Gavity correction
        delta_y = self._get_beamcenter_drop() # in cm
        
        # detector_pix size
        detector_pix_size = self.detector_pix_size
        # Square or circular pixel
        if len(detector_pix_size) == 1:
            pix_x_size = detector_pix_size[0]
            pix_y_size = detector_pix_size[0]
        # rectangular pixel pixel
        elif len(detector_pix_size) == 2:
            pix_x_size = detector_pix_size[0]
            pix_y_size = detector_pix_size[1]
        else:
            raise ValueError, " Input value format error..."
        # Sample to detector distance = sample slit to detector 
        # minus sample offset
        sample2detector_distance = self.sample2detector_distance[0] - \
                                    self.sample2sample_distance[0]
        # detector offset in x-direction
        detector_offset = 0
        try:
            detector_offset = self.sample2detector_distance[1]
        except:
            pass
        
        # detector size in [no of pix_x,no of pix_y]
        detector_pix_nums_x = self.detector_size[0]
        
        # get pix_y if it exists, otherwse take it from [0]
        try:
            detector_pix_nums_y = self.detector_size[1]
        except:
            detector_pix_nums_y = self.detector_size[0]
        
        # detector offset in pix number
        offset_x = detector_offset / pix_x_size
        offset_y = delta_y / pix_y_size
        
        # beam center position in pix number (start from 0)
        center_x, center_y = self._get_beamcenter_position(detector_pix_nums_x,
                                    detector_pix_nums_y, offset_x, offset_y)
        # distance [cm] from the beam center on detector plane
        detector_ind_x = numpy.arange(detector_pix_nums_x)
        detector_ind_y = numpy.arange(detector_pix_nums_y)

        # shif 0.5 pixel so that pix position is at the center of the pixel
        detector_ind_x = detector_ind_x + 0.5
        detector_ind_y = detector_ind_y + 0.5

        # the relative postion from the beam center
        detector_ind_x = detector_ind_x - center_x
        detector_ind_y = detector_ind_y - center_y
        
        # unit correction in cm
        detector_ind_x = detector_ind_x * pix_x_size
        detector_ind_y = detector_ind_y * pix_y_size
        
        qx_value = numpy.zeros(len(detector_ind_x))
        qy_value = numpy.zeros(len(detector_ind_y))
        i = 0

        for indx in detector_ind_x:
            qx_value[i] = self._get_qx(indx, sample2detector_distance, wavelength)
            i += 1
        i = 0
        for indy in detector_ind_y:
            qy_value[i] = self._get_qx(indy, sample2detector_distance, wavelength)
            i += 1
            
        # qx_value and qy_value values in array
        qx_value = qx_value.repeat(detector_pix_nums_y) 
        qx_value = qx_value.reshape(detector_pix_nums_x, detector_pix_nums_y)
        qy_value = qy_value.repeat(detector_pix_nums_x)  
        qy_value = qy_value.reshape(detector_pix_nums_y, detector_pix_nums_x)
        qy_value = qy_value.transpose()

        # p min and max values among the center of pixels
        self.qx_min = numpy.min(qx_value)
        self.qx_max = numpy.max(qx_value)
        self.qy_min = numpy.min(qy_value)
        self.qy_max = numpy.max(qy_value)
                
        # Appr. min and max values of the detector display limits 
        # i.e., edges of the last pixels.
        self.qy_min += self._get_qx(-0.5 * pix_y_size, 
                                sample2detector_distance, wavelength)
        self.qy_max += self._get_qx(0.5 * pix_y_size, 
                                sample2detector_distance, wavelength)
        #if self.qx_min == self.qx_max:
        self.qx_min += self._get_qx(-0.5 * pix_x_size, 
                                sample2detector_distance, wavelength)
        self.qx_max += self._get_qx(0.5 * pix_x_size, 
                                    sample2detector_distance, wavelength)
        # min and max values of detecter
        self.detector_qx_min = self.qx_min
        self.detector_qx_max = self.qx_max
        self.detector_qy_min = self.qy_min
        self.detector_qy_max = self.qy_max

        # try to set it as a Data2D otherwise pass (not required for now)
        try:
            from DataLoader.data_info import Data2D
            output = Data2D()
            inten = numpy.zeros_like(qx_value)
            output.data     = inten
            output.qx_data  = qx_value
            output.qy_data  = qy_value            
        except:
            pass
        
        return output#qx_value,qy_value
        
    def _get_qx(self, dx_size, det_dist, wavelength):
        """
        :param dx_size: x-distance from beam center [cm]
        :param det_dist: sample to detector distance [cm]
        
        :return: q-value at the given position
        """
        # Distance from beam center in the plane of detector
        plane_dist = dx_size
        # full scattering angle on the x-axis
        theta  = atan(plane_dist / det_dist)
        qx_value     = (2.0 * pi / wavelength) * sin(theta)
        return qx_value  
    
    def _get_polar_value(self, qx_value, qy_value):
        """
        Find qr_value and phi from qx_value and qy_value values
        
        : return qr_value, phi
        """
        # find |q| on detector plane
        qr_value = sqrt(qx_value*qx_value + qy_value*qy_value)
        # find angle phi
        phi = self._atan_phi(qy_value, qx_value)
        
        return qr_value, phi
    
    def _get_beamcenter_position(self, num_x, num_y, offset_x, offset_y):
        """
        :param num_x: number of pixel in x-direction
        :param num_y: number of pixel in y-direction
        :param offset: detector offset in x-direction in pix number
        
        :return: pix number; pos_x, pos_y in pix index
        """
        # beam center position
        pos_x = num_x / 2
        pos_y = num_y / 2

        # correction for offset
        pos_x += offset_x
        # correction for gravity that is always negative
        pos_y -= offset_y

        return pos_x, pos_y     

    def _get_beamcenter_drop(self):
        """
        Get the beam center drop (delta y) in y diection due to gravity
        
        :return delta y: the beam center drop in cm
        """
        # Check if mass == 0 (X-ray). 
        if self.mass == 0:
            return 0
        # Covert unit from A to cm
        unit_cm = 1e-08
        # Velocity of neutron in horizontal direction (~ actual velocity)
        velocity = _PLANK_H / (self.mass * self.wavelength * unit_cm)
        # Compute delta y
        delta_y = 0.5
        delta_y *= _GRAVITY
        delta_y *= self.sample2detector_distance[0] 
        delta_y *= (self.source2sample_distance[0] + self.sample2detector_distance[0])
        delta_y /= (velocity * velocity)

        return delta_y     

    