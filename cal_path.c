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
#include <signal.h>
#include <math.h>
#include <time.h>
#include <dirent.h>
#include <sys/types.h>
#include <unistd.h>
#include <limits.h>
#include <stdio.h>
#include <sys/stat.h>
#include "cal_path.h"
#include "util.h"
#include "inp.h"

static char share_path[400];
static char light_path[400];
static char lang_path[400];

void cal_path()
{
	if (isfile("main.c") == 0) {
		if (getcwd(share_path, 1000) == NULL) {
			ewe("IO error\n");
		}
	} else {
		strcpy(share_path, "/usr/lib64/gpvdm/");
	}
	join_path(2, light_path, share_path, "light");
	join_path(2, lang_path, share_path, "lang");

}

char *get_light_path()
{
	return light_path;
}

char *get_lang_path()
{
	return lang_path;
}

char *get_share_path()
{
	return share_path;
}
