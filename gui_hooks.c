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
//    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.s
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include "gui_hooks.h"
#include "util.h"

#ifdef dbus
#include <dbus/dbus.h>
#endif

int gui_send_data(char *tx_data_in)
{
	char tx_data[1024];
	char temp[1024];
	string_to_hex(temp, tx_data_in);
	sprintf(tx_data, "hex%s", temp);
	//printf("tx: %s\n",tx_data);
#ifdef dbus
	DBusConnection *connection;
	DBusError error;
	dbus_error_init(&error);
	connection = dbus_bus_get(DBUS_BUS_SESSION, &error);

	if (!connection) {
		printf("Failed to connect to the D-BUS daemon: %s",
		       error.message);
		dbus_error_free(&error);
		return 1;
	}

	DBusMessage *message;
	message =
	    dbus_message_new_signal("/org/my/test", "org.my.gpvdm", tx_data);
	/* Send the signal */
	dbus_connection_send(connection, message, NULL);
	dbus_connection_flush(connection);
	dbus_message_unref(message);
	//dbus_connection_close(connection);
#endif

	return 0;
}

int dbus_init()
{
#ifdef dbus

#endif
	return 0;
}

void gui_start()
{
	gui_send_data("start");
}
