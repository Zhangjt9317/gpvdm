//    Organic Photovoltaic Device Model - a drift diffusion base/Shockley-Read-Hall
//    model for organic solar cells. 
//    Copyright (C) 2012 Roderick C. I. MacKenzie
//
//	roderick.mackenzie@nottingham.ac.uk
//	www.roderickmackenzie.eu
//	Room B86 Coates, University Park, Nottingham, NG7 2RD, UK
//
//    This program is free software; you can redistribute it and/or modify
//    it under the terms of the GNU General Public License as published by
//    the Free Software Foundation; version 2 of the License
//
//    This program is distributed in the hope that it will be useful,
//    but WITHOUT ANY WARRANTY; without even the implied warranty of
//    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//    GNU General Public License for more details.
//
//    You should have received a copy of the GNU General Public License along
//    with this program; if not, write to the Free Software Foundation, Inc.,
//    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <errno.h>
#include <util.h>
#include <dump_ctrl.h>
#include <complex_solver.h>
#include <const.h>
#include <light.h>
#include <device.h>
#include <light_interface.h>

#include <functions.h>
#include <dll_interface.h>

EXPORT void light_dll_ver()
{
        printf("Flat light model\n");
}

EXPORT int light_dll_solve_lam_slice(struct light *in,int lam)
{
if ((*fun->get_dump_status)(dump_optics)==TRUE)
{
	char one[100];
	sprintf(one,"Solve light optical slice at %Lf nm\n",in->l[lam]*1e9);
	//printf("%s\n",one);
	waveprint(one,in->l[lam]*1e9);
}

int i;

gdouble complex n0=0.0+0.0*I;

//complex gdouble r=0.0+0.0*I;
complex gdouble t=0.0+0.0*I;
gdouble complex beta0=0.0+0.0*I;
complex gdouble Ep=in->sun_E[lam]+0.0*I;
complex gdouble En=0.0+0.0*I;
gdouble dx=in->x[1]-in->x[0];

for (i=0;i<in->points;i++)
{
	n0=in->nbar[lam][i];
	beta0=(2*PI*n0/in->l[lam]);

	if ((in->x[i]>in->device_start) &&(in->x[i]<in->device_ylen+in->device_start))
	{
		beta0=creal(beta0)+I*0;
	}

	Ep=Ep*cexp(-beta0*dx*I);

	//r=in->r[lam][i];
	t=in->t[lam][i];

	//if ((in->n[lam][i]!=in->n[lam][i+1])||(in->alpha[lam][i]!=in->alpha[lam][i+1]))
	//{
	//	En=Ep*r;
	//}

	in->Ep[lam][i]=creal(Ep);
	in->Epz[lam][i]=cimag(Ep);
	in->En[lam][i]=creal(En);
	in->Enz[lam][i]=cimag(En);

	if ((in->n[lam][i]!=in->n[lam][i+1])||(in->alpha[lam][i]!=in->alpha[lam][i+1]))
	{
		Ep=Ep*t;
	}
}

return 0;
}


