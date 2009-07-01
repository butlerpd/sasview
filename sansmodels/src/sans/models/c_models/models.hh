/**
	This software was developed by the University of Tennessee as part of the
	Distributed Data Analysis of Neutron Scattering Experiments (DANSE)
	project funded by the US National Science Foundation.

	If you use DANSE applications to do scientific research that leads to
	publication, we ask that you acknowledge the use of the software with the
	following sentence:

	"This work benefited from DANSE software developed under NSF award DMR-0520547."

	copyright 2008, University of Tennessee
 */
#ifndef MODEL_CLASS_H
#define MODEL_CLASS_H

#include <vector>
#include "parameters.hh"
extern "C" {
	#include "cylinder.h"
	#include "parallelepiped.h"
}

using namespace std;

class CylinderModel{
public:
	// Model parameters
	Parameter radius;
	Parameter scale;
	Parameter length;
	Parameter contrast;
	Parameter background;
	Parameter cyl_theta;
	Parameter cyl_phi;

	// Constructor
	CylinderModel();

	// Operators to get I(Q)
	double operator()(double q);
	double operator()(double qx, double qy);
	double evaluate_rphi(double q, double phi);
};

class ParallelepipedModel{
public:
	// TODO: add 2D 
	// Model parameters
	Parameter scale;
	Parameter short_edgeA;
	Parameter longer_edgeB;
	Parameter longuest_edgeC;
	Parameter contrast;
	Parameter background;
	Parameter parallel_theta;
	Parameter parallel_phi;

	// Constructor
	ParallelepipedModel();

	// Operators to get I(Q)
	double operator()(double q);
	double operator()(double qx, double qy);
	double evaluate_rphi(double q, double phi);
};


class SphereModel{
public:
	// Model parameters
	Parameter radius;
	Parameter scale;
	Parameter contrast;
	Parameter background;

	// Constructor
	SphereModel();

	// Operators to get I(Q)
	double operator()(double q);
	double operator()(double qx, double qy);
	double evaluate_rphi(double q, double phi);
};

class HardsphereStructure{
public:
	// Model parameters
	Parameter radius;
	Parameter volfraction;

	// Constructor
	HardsphereStructure();

	// Operators to get I(Q)
	double operator()(double q);
	double operator()(double qx, double qy);
	double evaluate_rphi(double q, double phi);
};

class StickyHSStructure{
public:
	// Model parameters
	Parameter radius;
	Parameter volfraction;
	Parameter perturb;
	Parameter stickiness;

	// Constructor
	StickyHSStructure();

	// Operators to get I(Q)
	double operator()(double q);
	double operator()(double qx, double qy);
	double evaluate_rphi(double q, double phi);
};

class SquareWellStructure{
public:
	// Model parameters
	Parameter radius;
	Parameter volfraction;
	Parameter welldepth;
	Parameter wellwidth;

	// Constructor
	SquareWellStructure();

	// Operators to get I(Q)
	double operator()(double q);
	double operator()(double qx, double qy);
	double evaluate_rphi(double q, double phi);
};

class HayterMSAStructure{
public:
	// Model parameters
	Parameter radius;
	Parameter charge;
	Parameter volfraction;
	Parameter temperature;
	Parameter saltconc;
	Parameter dielectconst;

	// Constructor
	HayterMSAStructure();

	// Operators to get I(Q)
	double operator()(double q);
	double operator()(double qx, double qy);
	double evaluate_rphi(double q, double phi);
};

class DiamEllipFunc{
public:
	// Model parameters
	Parameter radius_a;
	Parameter radius_b;

	// Constructor
	DiamEllipFunc();

	// Operators to get I(Q)
	double operator()(double q);
	double operator()(double qx, double qy);
	double evaluate_rphi(double q, double phi);
};

class DiamCylFunc{
public:
	// Model parameters
	Parameter radius;
	Parameter length;

	// Constructor
	DiamCylFunc();

	// Operators to get I(Q)
	double operator()(double q);
	double operator()(double qx, double qy);
	double evaluate_rphi(double q, double phi);
};

class CoreShellModel{
public:
	// Model parameters
	Parameter radius;
	Parameter scale;
	Parameter thickness;
	Parameter core_sld;
	Parameter shell_sld;
	Parameter solvent_sld;
	Parameter background;

	// Constructor
	CoreShellModel();

	// Operators to get I(Q)
	double operator()(double q);
	double operator()(double qx, double qy);
	double evaluate_rphi(double q, double phi);
};

class CoreShellCylinderModel{
public:
	// Model parameters
	Parameter radius;
	Parameter scale;
	Parameter thickness;
	Parameter length;
	Parameter core_sld;
	Parameter shell_sld;
	Parameter solvent_sld;
	Parameter background;
	Parameter axis_theta;
	Parameter axis_phi;

	// Constructor
	CoreShellCylinderModel();

	// Operators to get I(Q)
	double operator()(double q);
	double operator()(double qx, double qy);
	double evaluate_rphi(double q, double phi);
};

class EllipsoidModel{
public:
	// Model parameters
	Parameter radius_a;
	Parameter scale;
	Parameter radius_b;
	Parameter contrast;
	Parameter background;
	Parameter axis_theta;
	Parameter axis_phi;

	// Constructor
	EllipsoidModel();

	// Operators to get I(Q)
	double operator()(double q);
	double operator()(double qx, double qy);
	double evaluate_rphi(double q, double phi);
};

class EllipticalCylinderModel{
public:
	// Model parameters
	Parameter r_minor;
	Parameter scale;
	Parameter r_ratio;
	Parameter length;
	Parameter contrast;
	Parameter background;
	Parameter cyl_theta;
	Parameter cyl_phi;
	Parameter cyl_psi;

	// Constructor
	EllipticalCylinderModel();

	// Operators to get I(Q)
	double operator()(double q);
	double operator()(double qx, double qy);
	double evaluate_rphi(double q, double phi);
};
class TriaxialEllipsoidModel{
public:
	// Model parameters
	Parameter scale;
	Parameter semi_axisA;
	Parameter semi_axisB;
	Parameter semi_axisC;
	Parameter contrast;
	Parameter background;
	Parameter axis_theta;
	Parameter axis_phi;
	
	// Constructor
	TriaxialEllipsoidModel();

	// Operators to get I(Q)
	double operator()(double q);
	double operator()(double qx, double qy);
	double evaluate_rphi(double q, double phi);
};

class FlexibleCylinderModel{
public:
	// Model parameters
	Parameter scale;
	Parameter length;
	Parameter kuhn_length;
	Parameter radius;
	Parameter contrast;
	Parameter background;
	Parameter axis_theta;
	Parameter axis_phi;
	
	// Constructor
	FlexibleCylinderModel();

	// Operators to get I(Q)
	double operator()(double q);
	double operator()(double qx, double qy);
	double evaluate_rphi(double q, double phi);
};

class StackedDisksModel{
public:
	// Model parameters
	Parameter scale;
	Parameter length;
	Parameter radius;
	Parameter thickness;
	Parameter core_sld;
	Parameter layer_sld;
	Parameter solvent_sld;
	Parameter nlayers;
	Parameter spacing;
	Parameter background;
	Parameter axis_theta;
	Parameter axis_phi;
	
	// Constructor
	StackedDisksModel();

	// Operators to get I(Q)
	double operator()(double q);
	double operator()(double qx, double qy);
	double evaluate_rphi(double q, double phi);
};

class LamellarPSModel{
public:
	// Model parameters
	Parameter scale;
	Parameter spacing;
	Parameter delta;
	Parameter sigma;
	Parameter contrast;
	Parameter n_plates;
	Parameter caille;
	Parameter background;
	
	// Constructor
	LamellarPSModel();

	// Operators to get I(Q)
	double operator()(double q);
	double operator()(double qx, double qy);
	double evaluate_rphi(double q, double phi);
};

class LamellarPSHGModel{
public:
	// Model parameters
	Parameter scale;
	Parameter spacing;
	Parameter deltaT;
	Parameter deltaH;
	Parameter sld_tail;
	Parameter sld_head;
	Parameter sld_solvent;
	Parameter n_plates;
	Parameter caille;
	Parameter background;
	
	// Constructor
	LamellarPSHGModel();

	// Operators to get I(Q)
	double operator()(double q);
	double operator()(double qx, double qy);
	double evaluate_rphi(double q, double phi);
};

class OblateModel{
public:
	// Model parameters
	Parameter scale;
	Parameter major_core;
	Parameter minor_core;
	Parameter major_shell;
	Parameter minor_shell;
	Parameter contrast;
	Parameter sld_solvent;
	Parameter background;
	Parameter axis_theta;
	Parameter axis_phi;
	
	// Constructor
	OblateModel();

	// Operators to get I(Q)
	double operator()(double q);
	double operator()(double qx, double qy);
	double evaluate_rphi(double q, double phi);
};
class ProlateModel{
public:
	// Model parameters
	Parameter scale;
	Parameter major_core;
	Parameter minor_core;
	Parameter major_shell;
	Parameter minor_shell;
	Parameter contrast;
	Parameter sld_solvent;
	Parameter background;
	Parameter axis_theta;
	Parameter axis_phi;
	
	// Constructor
	ProlateModel();

	// Operators to get I(Q)
	double operator()(double q);
	double operator()(double qx, double qy);
	double evaluate_rphi(double q, double phi);
};

#endif
