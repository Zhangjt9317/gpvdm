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

#include <stdio.h>
#include <stdlib.h>
#include "util.h"

#include <dlfcn.h>

#include "inp.h"
#include "light_interface.h"
#include "const.h"
#include "device.h"
#include "dump_ctrl.h"
#include "config.h"
#include "complex_solver.h"
#include "cal_path.h"
#include "lang.h"
#include "log.h"
#include "dll_interface.h"
#include "newton_interface.h"

static int unused __attribute__ ((unused));
static void (*dll_set_interface) () = NULL;
static void (*dll_newton_set_min_ittr) () = NULL;
static int (*dll_solve_cur) () = NULL;
static int (*dll_solver_realloc) () = NULL;
static int (*dll_solver_free_memory) () = NULL;

static void *dll_handle;

void newton_init(struct simulation *sim, char *solver_name)
{
	printf_log(sim, _("Solver initialization\n"));
	char lib_name[100];
	char lib_path[1000];
	sprintf(lib_name, "%s.so", solver_name);

	join_path(2, lib_path, get_plugins_path(sim), lib_name);
	printf_log(sim, "I want to open %s %s %s\n", lib_path,
		   get_plugins_path(sim), lib_name);

	char *error;

	dll_handle = dlopen(lib_path, RTLD_LAZY);

	if (!dll_handle) {
		fprintf(stderr, "%s\n", dlerror());
		exit(0);
	}

	dll_solve_cur = dlsym(dll_handle, "dll_solve_cur");
	if ((error = dlerror()) != NULL) {
		fprintf(stderr, "%s\n", error);
		exit(0);
	}
	printf("calling %p\n", dll_solve_cur);

	dll_newton_set_min_ittr = dlsym(dll_handle, "dll_newton_set_min_ittr");
	if ((error = dlerror()) != NULL) {
		fprintf(stderr, "%s\n", error);
		exit(0);
	}

	dll_set_interface = dlsym(dll_handle, "set_interface");
	if ((error = dlerror()) != NULL) {
		fprintf(stderr, "%s\n", error);
		exit(0);
	}

	dll_solver_realloc = dlsym(dll_handle, "dll_solver_realloc");
	if ((error = dlerror()) != NULL) {
		fprintf(stderr, "%s\n", error);
		exit(0);
	}

	dll_solver_free_memory = dlsym(dll_handle, "dll_solver_free_memory");
	if ((error = dlerror()) != NULL) {
		fprintf(stderr, "%s\n", error);
		exit(0);
	}

	(*dll_newton_set_min_ittr) (0);

	(*dll_set_interface) (dll_get_interface());
}

int solve_cur(struct simulation *sim, struct device *in)
{
	printf("calling %p\n", dll_solve_cur);
	return (*dll_solve_cur) (sim, in);
}

void newton_set_min_ittr(int ittr)
{

	(*dll_newton_set_min_ittr) (ittr);
}

void solver_realloc(struct simulation *sim, struct device *in)
{
	(*dll_solver_realloc) (sim, in);
}

void solver_free_memory(struct device *in)
{
	(*dll_solver_free_memory) (in);
}

void newton_interface_free()
{
	printf("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n");
	dlclose(dll_handle);
}
