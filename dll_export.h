//    General-purpose Photovoltaic Device Model - a drift diffusion base/Shockley-Read-Hall
//    model for 1st, 2nd and 3rd generation solar cells.
//    Copyright (C) 2012 Roderick C. I. MacKenzie
//
//      roderick.mackenzie@nottingham.ac.uk
//      www.roderickmackenzie.eu
//      Room B86 Coates, University Park, Nottingham, NG7 2RD, UK
//
//    This program is free software; you can redistribute it and/or modify
//    it under the terms of the GNU General Public License as published by
//    the Free Software Foundation; either version 2 of the License, or
//    (at your option) any later version.
//
//    This program is distributed in the hope that it will be useful,
//    but WITHOUT ANY WARRANTY; without even the implied warranty of
//    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//    GNU General Public License for more details.
//
//    You should have received a copy of the GNU General Public License along
//    with this program; if not, write to the Free Software Foundation, Inc.,
//    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

#ifndef h_dll_export
#define h_dll_export

#define EXPORT

#include "dll_interface.h"

extern struct dll_interface *fun;

EXPORT void set_interface(struct dll_interface *in);

//Matrix solver
EXPORT void dll_matrix_solve(int col, int nz, int *Ti, int *Tj, long double *Tx,
			     long double *b);
EXPORT void dll_matrix_dump(int col, int nz, int *Ti, int *Tj, long double *Tx,
			    long double *b, char *index);
EXPORT void dll_matrix_solver_free();

//Light
EXPORT void light_dll_init();
EXPORT void light_dll_free(struct light *in);
EXPORT void light_dll_solve_and_update(struct device *cell, struct light *in,
				       gdouble Psun_in, gdouble laser_eff_in,
				       gdouble pulse_width);
EXPORT int light_dll_solve_lam_slice(struct light *in, int lam);
EXPORT void light_dll_ver();
EXPORT void light_fixup(char *name, void (*in));

//Newton solver
EXPORT void dll_newton_set_min_ittr(int ittr);
EXPORT int dll_solve_cur(struct device *in);
EXPORT void dll_solver_realloc(struct device *in);
EXPORT void dll_solver_free_memory(struct device *in);

#endif