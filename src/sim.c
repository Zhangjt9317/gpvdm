//
//  General-purpose Photovoltaic Device Model gpvdm.com- a drift diffusion
//  base/Shockley-Read-Hall model for 1st, 2nd and 3rd generation solarcells.
// 
//  Copyright (C) 2012 Roderick C. I. MacKenzie
//
//      roderick.mackenzie@nottingham.ac.uk
//      www.roderickmackenzie.eu
//      Room B86 Coates, University Park, Nottingham, NG7 2RD, UK
//
//
// This program is free software; you can redistribute it and/or modify it
// under the terms and conditions of the GNU General Public License,
// version 2, as published by the Free Software Foundation.
//
// This program is distributed in the hope it will be useful, but WITHOUT
// ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
// FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
// more details.

#include <sim.h>

void sim_init(struct simulation *sim)
{
//plotting
	sim->gnuplot = NULL;
	sim->gnuplot_time = NULL;
	sim->converge = NULL;
	sim->tconverge = NULL;
	sim->log_level = -1;
	sim->last_col = 0;
	sim->last_nz = 0;
	sim->x = NULL;
	sim->Ap = NULL;
	sim->Ai = NULL;
	sim->Ax = NULL;
	sim->b = NULL;
	sim->Tx = NULL;

	//complex solver
	sim->complex_last_col = 0;
	sim->complex_last_nz = 0;
	sim->complex_x = NULL;
	sim->complex_xz = NULL;
	sim->complex_Ap = NULL;
	sim->complex_Ai = NULL;
	sim->complex_Ax = NULL;
	sim->complex_Az = NULL;

}
