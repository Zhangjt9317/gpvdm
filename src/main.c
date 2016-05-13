//
//  General-purpose Photovoltaic Device Model gpvdm.com- a drift diffusion
//  base/Shockley-Read-Hall model for 1st, 2nd and 3rd generation solarcells.
// 
//  Copyright (C) 2012 Roderick C. I. MacKenzie <r.c.i.mackenzie@googlemail.com>
//
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



#include <sys/types.h>
#include <dirent.h>
#include <stdio.h>
#include <stdlib.h>


#include <time.h>
#include <unistd.h>

#include <util.h>

#include <sim.h>
#include <dos.h>
#include <server.h>
#include <light_interface.h>
#include <dump.h>
#include <complex_solver.h>
#include <license.h>
#include <inp.h>
#include <gui_hooks.h>
#include <timer.h>
#include <rand.h>
#include <hard_limit.h>
#include <patch.h>
#include <cal_path.h>
#include <lang.h>
#include <log.h>
#include <device.h>
#include <fit.h>
#include <advmath.h>
#include <plot.h>
#include <buffer.h>

static int unused __attribute__((unused));



int main (int argc, char *argv[])
{
struct simulation sim;
sim_init(&sim);

int log_level=0;
set_logging_level(&sim,log_level_screen);
cal_path(&sim);

if (scanarg( argv,argc,"--help")==TRUE)
{
	printf_log(&sim,"gpvdm_core - General-purpose Photovoltaic Device Model\n");
	printf_log(&sim,copyright);
	printf_log(&sim,"\n");
	printf_log(&sim,"Usage: gpvdm_core [options]\n");
	printf_log(&sim,"\n");
	printf_log(&sim,"Options:\n");
	printf_log(&sim,"\n");
	printf_log(&sim,"\t--outputpath\toutput data path");
	printf_log(&sim,"\t--inputpath\t sets the input path\n");
	printf_log(&sim,"\t--version\tdisplays the current version\n");
	printf_log(&sim,"\t--zip_results\t zip the results\n");
	printf_log(&sim,"\t--simmode\t forces a simulation mode.\n");
	printf_log(&sim,"\t--cpus\t sets the number of CPUs\n");
	printf_log(&sim,"\n");
	printf_log(&sim,"Additional information about gpvdm is available at www.gpvdm.com.\n");
	printf_log(&sim,"\n");
	printf_log(&sim,"Report bugs to: roderick.mackenzie@nottingham.ac.uk\n\n");
	exit(0);
}
if (scanarg( argv,argc,"--version")==TRUE)
{
	printf_log(&sim,"gpvdm_core, Version %s\n",gpvdm_ver);
	printf_log(&sim,copyright);
	printf_log(&sim,this_is_free_software);
	printf_log(&sim,"There is ABSOLUTELY NO WARRANTY; not even for MERCHANTABILITY or\n");
	printf_log(&sim,"FITNESS FOR A PARTICULAR PURPOSE.\n");
	printf_log(&sim,"\n");
	exit(0);
}



//solver_test();
//printf_log(&sim,"rod\n");
//solver_ld_test();
//exit(0);
setlocale(LC_MESSAGES,"");
bindtextdomain("gpvdm",get_lang_path(&sim));
textdomain("gpvdm");

timer_init(0);
timer_init(1);
dbus_init();

set_ewe_lock_file("","");

char pwd[1000];
if (getcwd(pwd,1000)==NULL)
{
	ewe(&sim,"IO error\n");
}


remove("snapshots.zip");
remove("light_dump.zip");
log_clear(&sim);

hard_limit_init(&sim);

set_plot_script_dir(pwd);

//set_plot_script_dir(char * in)



if(geteuid()==0) {
	ewe(&sim,"Don't run me as root!\n");
}

srand(time(0));
textcolor(fg_green);
randomprint(_("General-purpose Photovoltaic Device Model (www.gpvdm.com)\n"));
randomprint(_("You should have received a copy of the GNU General Public License\n"));
randomprint(_("along with this software.  If not, see www.gnu.org/licenses/.\n"));
randomprint("\n");
randomprint(_("If you wish to collaborate in anyway please get in touch:\n"));
randomprint(_("roderick.mackenzie@nottingham.ac.uk\n"));
randomprint(_("www.roderickmackenzie.eu/contact.html\n"));
randomprint("\n");
textcolor(fg_reset);

sim.server.on=FALSE;
sim.server.cpus=1;
sim.server.readconfig=TRUE;

if (scanarg( argv,argc,"--outputpath")==TRUE)
{
	strcpy(sim.output_path,get_arg_plusone( argv,argc,"--outputpath"));
}


if (scanarg( argv,argc,"--inputpath")==TRUE)
{
	strcpy(sim.input_path,get_arg_plusone( argv,argc,"--inputpath"));
}





char name[200];
struct inp_file inp;
struct buffer buf;
buffer_init(&buf);

inp_init(&sim,&inp);
if (inp_load_from_path(&sim,&inp,sim.input_path,"ver.inp")!=0)
{
	printf_log(&sim,"can't find file %s ver.inp",sim.input_path);
	exit(0);
}
inp_check(&sim,&inp,1.0);
inp_search_string(&sim,&inp,name,"#core");
inp_free(&sim,&inp);

if (strcmp(name,gpvdm_ver)!=0)
{
printf_log(&sim,"Software is version %s and the input files are version %s\n",gpvdm_ver,name);
exit(0);
}

gui_start();
server_init(&sim);

if (scanarg( argv,argc,"--lock")==TRUE)
{
	server_set_dbus_finish_signal(&(sim.server), get_arg_plusone( argv,argc,"--lock"));
}


int ret=0;


if (scanarg( argv,argc,"--simmode")==TRUE)
{
	strcpy(sim.force_sim_mode,get_arg_plusone( argv,argc,"--simmode"));
}

gen_dos_fd_gaus_fd(&sim);

server_add_job(&sim,sim.output_path,sim.input_path);
print_jobs(&sim);

ret=server_run_jobs(&sim,&(sim.server));

server_shut_down(&sim,&(sim.server));

hard_limit_free(&sim);
if (ret!=0)
{
	return 1;
}
return 0;
}

