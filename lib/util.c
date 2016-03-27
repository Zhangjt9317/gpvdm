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
#include <math.h>
#include <stdarg.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <dirent.h>
#include <fcntl.h>
#include <sys/time.h>
#include "util.h"
#include "log.h"
#include <const.h>
//#include "dump_ctrl.h"
//#include "dos_types.h"
//#include "gui_hooks.h"
//#include "server.h"
#include <lang.h>

void fx_with_units(char *out, double number)
{
	if (number < 1e3) {
		sprintf(out, "%.3lf Hz", number);
	} else if (number < 1e6) {
		sprintf(out, "%.3lf KHz", number * 1e-3);
	} else if (number < 1e9) {
		sprintf(out, "%.3lf MHz", number * 1e-6);
	} else if (number < 1e12) {
		sprintf(out, "%.3lf GHz", number * 1e-9);
	}

}

void join_path(int max, ...)
{
	max = max + 1;
	char temp[1000];
	strcpy(temp, "");
	va_list arguments;
	int i;
	va_start(arguments, max);
	char *ret = va_arg(arguments, char *);
	strcpy(ret, "");
	for (i = 1; i < max; i++) {
		if ((i != 1) && (strcmp(temp, "") != 0)) {
			strcat(ret, "/");
		}
		strcpy(temp, va_arg(arguments, char *));
		strcat(ret, temp);
	}
	va_end(arguments);	// Cleans up the list

	return;
}

void string_to_hex(char *out, char *in)
{
	int i;
	char temp[8];
	strcpy(out, "");

	for (i = 0; i < strlen(in); i++) {
		sprintf(temp, "%02x", in[i]);
		strcat(out, temp);
	}

}

void print_hex(unsigned char *data)
{
	int i;
	for (i = 0; i < 16; i++) {
		printf("%02x", data[i]);
	}
	printf("\n");
}

void write_x_y_to_file(char *name, double *x, double *y, int len)
{
	int i;
	FILE *out;

	out = fopen(name, "w");
	if (out == NULL) {
		ewe("Error writing file %s\n", name);
	}

	for (i = 0; i < len; i++) {
		fprintf(out, "%le %le\n", x[i], y[i]);
	}
	fclose(out);
}

void write_x_y_z_to_file(char *name, double *x, double *y, double *z, int len)
{
	int i;
	FILE *out;

	out = fopen(name, "w");
	if (out == NULL) {
		ewe("Error writing file %s\n", name);
	}

	for (i = 0; i < len; i++) {
		fprintf(out, "%le %le %le\n", x[i], y[i], z[i]);
	}
	fclose(out);
}

int check_int(char *in)
{
	int i = 0;
	int numeric = TRUE;
	for (i = 0; i < strlen(in); i++) {
		if ((in[i] < 48) || (in[i] > 57)) {
			numeric = FALSE;
			break;
		}
	}
	return numeric;
}

static int unused __attribute__ ((unused));

int english_to_bin(char *in)
{
	int ret = 0;
	if (check_int(in) == TRUE) {
		sscanf(in, "%d", &ret);
		return ret;
	}

	if (strcmp(in, "true") == 0) {
		return TRUE;
	} else if (strcmp(in, "false") == 0) {
		return FALSE;
	} else if (strcmp(in, "1") == 0) {
		return TRUE;
	} else if (strcmp(in, "0") == 0) {
		return FALSE;
	} else if (strcmp(in, "yes") == 0) {
		return TRUE;
	} else if (strcmp(in, "no") == 0) {
		return FALSE;
	} else if (strcmp(in, "left") == 0) {
		return LEFT;
	} else if (strcmp(in, "links") == 0) {
		return LEFT;
	} else if (strcmp(in, "ja") == 0) {
		return TRUE;
	} else if (strcmp(in, "nein") == 0) {
		return FALSE;
	} else if (strcmp(in, "right") == 0) {
		return RIGHT;
	} else if (strcmp(in, "rechts") == 0) {
		return RIGHT;

	} else if (strcmp(in, "gaus") == 0) {
		return 0;
	} else if (strcmp(in, "exp") == 0) {
		return 1;
	} else if (strcmp(in, "exponential") == 0) {
		return dos_exp;
	} else if (strcmp(in, "complex") == 0) {
		return dos_an;
	} else if (strcmp(in, "open_circuit") == 0) {
		return pulse_open_circuit;
	} else if (strcmp(in, "load") == 0) {
		return pulse_load;
	} else if (strcmp(in, "none") == 0) {
		return log_level_none;
	} else if (strcmp(in, "screen") == 0) {
		return log_level_screen;
	} else if (strcmp(in, "disk") == 0) {
		return log_level_disk;
	} else if (strcmp(in, "screen_and_disk") == 0) {
		return log_level_screen_and_disk;
	}

	ewe("I don't understand the command %s\n", in);
	return 0;
}

double read_value(char *file, int skip, int line)
{
	FILE *in;
	char buf[1000];
	double value;
	in = fopen(file, "r");
	if (in == NULL) {
		ewe("Can not read file %s\n", file);
	}
	int l = 0;

	do {
		l++;
		unused = fscanf(in, "%s", buf);

		if (l == line) {
			sscanf((buf + skip), "%le\n", &value);
			break;
		}

	} while (!feof(in));

	fclose(in);

	return value;
}

void safe_file(char *name)
{
	FILE *file;
	file = fopen(name, "rb");

	if (!file) {
		ewe("File %s not found\n", name);
	}

	fclose(file);
}

int cmpstr_min(char *in1, char *in2)
{
	int i;
	int max = strlen(in1);
	if (strlen(in2) < max)
		max = strlen(in2);
	for (i = 0; i < max; i++) {
		if (in1[i] != in2[i])
			return 1;
	}
	return 0;
}

int strextract_name(char *out, char *in)
{
	int i;
	for (i = 0; i < strlen(in); i++) {
		if (in[i] == '@') {
			out[i] = 0;
			return strlen(out);
		}
		out[i] = in[i];

	}
	strcpy(out, "");
	return -1;
}

int strcmp_end(char *str, char *end)
{
	if (strlen(str) < strlen(end))
		return 1;
	int pos = strlen(str) - strlen(end);
	return strcmp((char *)(str + pos), end);
}

int strcmp_begin(char *str, char *begin)
{
	int i;
	if (strlen(str) < strlen(begin))
		return 1;
	int lb = strlen(begin);
	for (i = 0; i < lb; i++) {
		if (str[i] != begin[i])
			return 1;
	}
	return 0;
}

char *strextract_domain(char *in)
{
	int i = 0;
	for (i = 0; i < strlen(in) - 1; i++) {
		if (in[i] == '@') {
			return (char *)(&in[i + 1]);
		}
	}
	return (char *)-1;
}

int is_domain(char *in)
{
	int i = 0;
	for (i = 0; i < strlen(in) - 1; i++) {
		if (in[i] == '@') {
			return 0;
		}
	}

	return -1;
}

int extract_str_number(char *in, char *cut)
{
	int out;
	int len = strlen(cut);
	sscanf((in + len), "%d", &out);
	return out;
}

int strextract_int(char *in)
{
	char temp[200];
	int i = 0;
	int ret = 0.0;
	int count = 0;
	for (i = 0; i < strlen(in); i++) {
		if ((in[i] > 47) && (in[i] < 58)) {
			temp[count] = in[i];
			count++;
		}

	}
	temp[count] = 0;
	sscanf(temp, "%d", &ret);
	return ret;
}

void waveprint(char *in, double wavelength)
{
	if (wavelength < 400.0) {
		textcolor(fg_purple);
	} else if (wavelength < 500.0) {
		textcolor(fg_blue);
	} else if (wavelength < 575.0) {
		textcolor(fg_green);
	} else if (wavelength < 600.0) {
		textcolor(fg_yellow);
	} else {
		textcolor(fg_red);
	}

	printf("%s", in);
	textcolor(fg_reset);

}

void randomprint(char *in)
{
	int i;
	for (i = 0; i < strlen(in); i++) {
		int rnd = (float)6.0 * rand() / (float)RAND_MAX;
		if (rnd == 0)
			textcolor(fg_reset);
		if (rnd == 1)
			textcolor(fg_red);
		if (rnd == 2)
			textcolor(fg_green);
		if (rnd == 3)
			textcolor(fg_yellow);
		if (rnd == 4)
			textcolor(fg_blue);
		if (rnd == 5)
			textcolor(fg_purple);
		printf("%c", in[i]);
	}

}

void textcolor(int color)
{
	char command[13];
	sprintf(command, "\e[%dm", color);
	printf("%s", command);
}

FILE *fopena(char *path, char *name, const char *mode)
{
	char wholename[200];
	join_path(2, wholename, path, name);

	FILE *pointer;
	pointer = fopen(wholename, mode);

	return pointer;
}

int scanarg(char *in[], int count, char *find)
{
	int i;
	for (i = 0; i < count; i++) {
		if (strcmp(in[i], find) == 0)
			return TRUE;
	}
	return FALSE;
}

int get_arg_plusone_pos(char *in[], int count, char *find)
{
	int i;
	for (i = 0; i < count; i++) {
		if (strcmp(in[i], find) == 0) {
			if ((i + 1) < count) {
				return i + 1;
			} else {
				return FALSE;
			}
		}
	}
	return FALSE;
}

char *get_arg_plusone(char *in[], int count, char *find)
{
	int i;
	static char no[] = "";
	for (i = 0; i < count; i++) {
//printf("%s %s\n",in[i],find);
		if (strcmp(in[i], find) == 0) {
			if ((i + 1) < count) {
				//printf("%s\n",in[i+1]);
				return in[i + 1];
			} else {
				return no;
			}
		}
	}

	return no;
}

void edit_file_int(char *in_name, char *front, int line_to_edit, int value)
{

	FILE *in;
	FILE *out;
	char *line;
	int file_size = 0;
	in = fopen(in_name, "r");
	int pos = 0;
	char temp[200];
	if (in == NULL) {
		ewe("edit_file_by_var: File %s not found\n", in_name);
	}
	fseek(in, 0, SEEK_END);
	file_size = ftell(in);
	fseek(in, 0, SEEK_SET);

	char *in_buf = malloc(file_size + 1);
	memset(in_buf, 0, (file_size + 1) * sizeof(char));

	fread(in_buf, file_size, 1, in);
	in_buf[file_size] = 0;
	fclose(in);

	char *out_buf = out_buf = malloc((file_size + 100) * sizeof(char));
	memset(out_buf, 0, (file_size + 100) * sizeof(char));

	line = strtok(in_buf, "\n");
	while (line) {
		pos++;
		if (pos != line_to_edit) {
			strcat(out_buf, line);
			strcat(out_buf, "\n");
		} else {
			sprintf(temp, "%s%d\n", front, value);
			strcat(out_buf, temp);
		}
		line = strtok(NULL, "\n");
	}

	free(in_buf);

	out = fopen(in_name, "w");
	if (in == NULL) {
		ewe("edit_file_by_var: Can not write file %s \n", in_name);
	}
	fwrite(out_buf, strlen(out_buf), 1, out);
	free(out_buf);
	fclose(out);

}

void edit_file(char *in_name, char *front, int line_to_edit, double value)
{

	FILE *in;
	FILE *out;
	char *line;
	int file_size = 0;
	in = fopen(in_name, "r");
	int pos = 0;
	char temp[200];
	if (in == NULL) {
		ewe("edit_file_by_var: File %s not found\n", in_name);
	}
	fseek(in, 0, SEEK_END);
	file_size = ftell(in);
	fseek(in, 0, SEEK_SET);

	char *in_buf = malloc(file_size + 1);
	memset(in_buf, 0, (file_size + 1) * sizeof(char));

	fread(in_buf, file_size, 1, in);
	in_buf[file_size] = 0;
	fclose(in);

	char *out_buf = out_buf = malloc((file_size + 100) * sizeof(char));
	memset(out_buf, 0, (file_size + 100) * sizeof(char));

	line = strtok(in_buf, "\n");
	while (line) {
		pos++;
		if (pos != line_to_edit) {
			strcat(out_buf, line);
			strcat(out_buf, "\n");
		} else {
			sprintf(temp, "%s%le\n", front, value);
			strcat(out_buf, temp);
		}
		line = strtok(NULL, "\n");
	}

	free(in_buf);

	out = fopen(in_name, "w");
	if (in == NULL) {
		ewe("edit_file_by_var: Can not write file %s \n", in_name);
	}
	fwrite(out_buf, strlen(out_buf), 1, out);
	free(out_buf);
	fclose(out);

}

void mass_copy_file(char **output, char *input, int n)
{
//printf ("%s %s",input,output);
	char buf[8192];
	int i;
	struct stat results;
	int in_fd = open(input, O_RDONLY);

	if (in_fd == -1) {
		ewe("File %s can not be opened\n", input);
	}

	stat(input, &results);

	int out_fd[10];

	for (i = 0; i < n; i++) {
		out_fd[i] =
		    open(output[i], O_WRONLY | O_CREAT | O_TRUNC,
			 results.st_mode);
		if (out_fd[i] == -1) {
			ewe("File %s can not be opened\n", output);
		}
	}

	while (1) {
		memset(buf, 0, (8192) * sizeof(char));
		ssize_t result = read(in_fd, buf, 8192 * sizeof(char));
		if (result == 0) {
			break;
		}
		//printf("mas copy %s %s %d\n",input,buf,result,strlen(buf));
		for (i = 0; i < n; i++) {
			write(out_fd[i], buf, result * sizeof(char));
		}
	}

	close(in_fd);
	for (i = 0; i < n; i++) {
		close(out_fd[i]);
	}
}

void copy_file(char *output, char *input)
{
//printf ("%s %s",input,output);
	char buf[8192];
	struct stat results;
	int in_fd = open(input, O_RDONLY);
	if (in_fd == -1) {
		ewe("File %s can not be opened\n", input);
	}

	stat(input, &results);

	int out_fd =
	    open(output, O_WRONLY | O_CREAT | O_TRUNC, results.st_mode);
	if (in_fd == -1) {
		ewe("File %s can not be opened\n", output);
	}

	while (1) {
		ssize_t result = read(in_fd, buf, 8192 * sizeof(char));

		//printf("%d\n",result);

		if (result == 0) {
			break;
		}
		write(out_fd, buf, result * sizeof(char));
	}

	close(in_fd);
	close(out_fd);
}

void edit_file_by_var(char *in_name, char *token, char *newtext)
{
	FILE *in;
	FILE *out;
	char *line;
	int found = FALSE;
	int file_size = 0;
	in = fopen(in_name, "r");
	if (in == NULL) {
		ewe("edit_file_by_var: File %s not found\n", in_name);
	}
	fseek(in, 0, SEEK_END);
	file_size = ftell(in);
	fseek(in, 0, SEEK_SET);

	char *in_buf = malloc(file_size + 1);
	memset(in_buf, 0, (file_size + 1) * sizeof(char));

	fread(in_buf, file_size, 1, in);
	in_buf[file_size] = 0;
	fclose(in);

	char *out_buf = out_buf =
	    malloc((file_size + strlen(newtext) + 10) * sizeof(char));
	memset(out_buf, 0, (file_size + strlen(newtext) + 10) * sizeof(char));

	line = strtok(in_buf, "\n");
	while (line) {
		if (strcmp(line, token) != 0) {
			strcat(out_buf, line);
			strcat(out_buf, "\n");
		} else {
			strcat(out_buf, line);
			strcat(out_buf, "\n");
			strcat(out_buf, newtext);
			strcat(out_buf, "\n");
			line = strtok(NULL, "\n");
			found = TRUE;
		}
		line = strtok(NULL, "\n");
	}

	if (found == FALSE) {
		ewe("edit_file_by_var: Token not found in file %s\n", token);
	}

	free(in_buf);

	out = fopen(in_name, "w");
	if (in == NULL) {
		ewe("edit_file_by_var: Can not write file %s \n", in_name);
	}
	fwrite(out_buf, strlen(out_buf), 1, out);
	free(out_buf);
	fclose(out);

}

char *get_file_name_from_path(char *in)
{
	int i = 0;
	for (i = strlen(in) - 1; i > 0; i--) {
		if (in[i] == '/') {
			return (in + i + 1);
		}
	}
	return in;
}

char *get_dir_name_from_path(char *in)
{
	static char ret[1000];
	strcpy(ret, in);

	int i = 0;
	for (i = strlen(in); i > 0; i--) {
		if (in[i] == '/') {
			ret[i] = 0;
			return ret;
		}
	}

	strcpy(ret, "");
	return ret;
}

int isdir(const char *path)
{
	struct stat statbuf;
	if (stat(path, &statbuf) != 0) {
		return 1;
	} else {
		if (S_ISDIR(statbuf.st_mode) == 0) {
			return 1;
		} else {
			return 0;
		}
	}
}

void remove_dir(char *dir_name)
{

	struct dirent *next_file;
	DIR *theFolder;
	char filepath[256];

//if (get_dump_status(dump_newton)==TRUE)
//{

	theFolder = opendir(dir_name);
	if (theFolder != NULL) {
		while ((next_file = readdir(theFolder)) != NULL) {
			if ((strcmp(next_file->d_name, ".") != 0)
			    && (strcmp(next_file->d_name, "..") != 0)) {
				join_path(2, filepath, dir_name,
					  next_file->d_name);
				if (isdir(filepath) == 0) {
					remove_dir(filepath);
					printf_log(_("Deleting dir =%s\n"),
						   filepath);
					remove(filepath);
				} else {
					//printf("Deleteing file =%s\n",filepath);
					remove(filepath);
				}
			}
		}

		closedir(theFolder);
	}
//}

}
