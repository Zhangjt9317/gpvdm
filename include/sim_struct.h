//
//  General-purpose Photovoltaic Device Model gpvdm.com- a drift diffusion
//  base/Shockley-Read-Hall model for 1st, 2nd and 3rd generation solarcells.
// 
//  Copyright (C) 2012 Roderick C. I. MacKenzie
//
//	roderick.mackenzie@nottingham.ac.uk
//	www.roderickmackenzie.eu
//	Room B86 Coates, University Park, Nottingham, NG7 2RD, UK
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


#ifndef sim_struct_h
#define sim_struct_h

#include <stdio.h>

struct simulation
{
	//plotting
	FILE *gnuplot;
	FILE *gnuplot_time;
	FILE *converge;
	FILE *tconverge;
	//dump
	int dump_array[100];
	int log_level;
	//paths
	char plugins_path[400];
	char lang_path[400];
	char input_path[400];
	char output_path[400];
	char share_path[400];
};

#endif
