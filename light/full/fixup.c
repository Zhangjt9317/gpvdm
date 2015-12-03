#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <errno.h>
#include <util.h>
#include <true_false.h>
#include "../../dump_ctrl.h"
#include "../../complex_solver.h"
#include "../../const.h"
#include "../../light.h"
#include "../../device.h"
#include "functions.h"
#include "../../light_interface.h"

EXPORT void light_dll_fixup(char * name,void (*in))
{
	if (strcmp(name,"waveprint")==0)
	{
		l_waveprint=in;
	}else
	if (strcmp(name,"get_dump_status")==0)
	{
		l_get_dump_status=in;
	}else
	if (strcmp(name,"light_dump_1d")==0)
	{
		l_light_dump_1d=in;
	}else
	if (strcmp(name,"light_solve_optical_problem")==0)
	{
		l_light_solve_optical_problem=in;
	}else
	if (strcmp(name,"light_free_memory")==0)
	{
		l_light_free_memory=in;
	}else
	if (strcmp(name,"light_transfer_gen_rate_to_device")==0)
	{
		l_light_transfer_gen_rate_to_device=in;
	}else
	if (strcmp(name,"complex_solver")==0)
	{
		l_complex_solver=in;
	}else
	{
		printf("fixup in dll function %s not found\n",name);
	}
}

