#    General-purpose Photovoltaic Device Model - a drift diffusion base/Shockley-Read-Hall
#    model for 1st, 2nd and 3rd generation solar cells.
#    Copyright (C) 2012-2016 Roderick C. I. MacKenzie <r.c.i.mackenzie@googlemail.com>
#
#	https://www.gpvdm.com
#	Room B86 Coates, University Park, Nottingham, NG7 2RD, UK
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License v2.0, as published by
#    the Free Software Foundation.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import i18n
_ = i18n.language.gettext

class my_data():
	token=""
	units=""
	info=""
	def __init__(self,a,b,c,d,e,f):
		self.token=a
		self.units=b
		self.info=c
		self.opt=d
		self.number_type=e
		self.number_mul=f


lib=[]
lib.append(my_data("#mueffe","m^{2}V^{-1}s^{-1}",_("Electron mobility"),["text"],"e",1.0))
lib.append(my_data("#mueffh","m^{2}V^{-1}s^{-1}",_("Hole mobility"),["text"],"e",1.0))
lib.append(my_data("#Ntrape","m^{-3} eV^{-1}",_("Electron trap density"),["text"],"e",1.0))
lib.append(my_data("#Ntraph","m^{-3} eV^{-1}",_("Hole trap density"),["text"],"e",1.0))
lib.append(my_data("#Etrape","eV",_("Electron tail slope"),["text"],"e",1.0))
lib.append(my_data("#Etraph","eV",_("Hole tail slope"),["text"],"e",1.0))
lib.append(my_data("#epsilonr","au",_("Relative permittivity"),["text"],"e",1.0))
lib.append(my_data("#srhsigman_e","m^{-2}",_("Free electron to Trapped electron"),["text"],"e",1.0))
lib.append(my_data("#srhsigmap_e","m^{-2}",_("Trapped electron to Free hole"),["text"],"e",1.0))
lib.append(my_data("#srhsigman_h","m^{-2}",_("Trapped hole to Free electron"),["text"],"e",1.0))
lib.append(my_data("#srhsigmap_h","m^{-2}",_("Free hole to Trapped hole"),["text"],"e",1.0))
lib.append(my_data("#Rshunt","Ohms",_("Shunt resistance"),["text"],"e",1.0))
lib.append(my_data("#Rcontact","Ohms",_("Series resistance"),["text"],"e",1.0))
lib.append(my_data("#lcharge","m^{-3}",_("Charge on left contact"),["text"],"e",1.0))
lib.append(my_data("#rcharge","m^{-3}",_("Charge on right contact"),["text"],"e",1.0))
lib.append(my_data("#Vstart","V",_("Start voltage"),["text"],"e",1.0))
lib.append(my_data("#Vstop","V",_("Stop voltage"),["text"],"e",1.0))
lib.append(my_data("#Vstep","V",_("Voltage step"),["text"],"e",1.0))
lib.append(my_data("#I0","Apms",_("I0"),["text"],"e",1.0))
lib.append(my_data("#nid","(a.u.)",_("ideality factor"),["text"],"e",1.0))
#lib.append(my_data("#Psun","Sun","Intensity of the sun"),["text"],"e",1.0))

lib.append(my_data("#saturation_n0","#saturation_n0",_("#saturation_n0"),["text"],"e",1.0))
lib.append(my_data("#saturation_rate","#saturation_rate",_("#saturation_rate"),["text"],"e",1.0))
lib.append(my_data("#imps_saturate","#imps_saturate",_("#imps_saturate"),["text"],"e",1.0))


lib.append(my_data("#simplephotondensity","m^{-2}s^{-1}",_("Photon density"),["text"],"e",1.0))
lib.append(my_data("#simple_alpha","m^{-1}",_("Absorption of material"),["text"],"e",1.0))
lib.append(my_data("#simmode","au",_("#simmode"),["text"],"e",1.0))
lib.append(my_data("#Nc","m^{-3}",_("Effective density of free electron states"),["text"],"e",1.0))
lib.append(my_data("#Nv","m^{-3}",_("Effective density of free hole states"),["text"],"e",1.0))
lib.append(my_data("#sun","filename",_("Sun's spectra"),["text"],"e",1.0))
lib.append(my_data("#meshpoints","au",_("Mesh points (x)"),["text"],"e",1.0))
lib.append(my_data("#lpoints","au",_("Mesh points (lambda)"),["text"],"e",1.0))
lib.append(my_data("#lstart","m",_("Lambda start"),["text"],"e",1.0))
lib.append(my_data("#lstop","m",_("Lambda stop"),["text"],"e",1.0))
lib.append(my_data("#laserwavelength","m",_("Laser wavelength"),["text"],"e",1.0))
lib.append(my_data("#spotx","m",_("Spot size x"),["text"],"e",1.0))
lib.append(my_data("#spoty","m",_("Spot size y"),["text"],"e",1.0))
lib.append(my_data("#pulseJ","J",_("Energy in pulse"),["text"],"e",1.0))
lib.append(my_data("#gather","au",_("#gather"),["text"],"e",1.0))
lib.append(my_data("#laser_pulse_width","s",_("Length of pulse"),["text"],"e",1.0))
lib.append(my_data("#electron_eff","0-1",_("Electron generation efficiency"),["text"],"e",1.0))
lib.append(my_data("#hole_eff","0-1",_("Hole generation efficiency"),["text"],"e",1.0))
lib.append(my_data("#function","au",_("#function"),["text"],"e",1.0))
lib.append(my_data("#lr_pcontact",_("left/right"),_("Hole majority contact on left/right of device."),[("leftright")],"s",1.0))
lib.append(my_data("#Vexternal","V",_("start voltage"),["text"],"e",1.0))
lib.append(my_data("#Vmax","V",_("Max voltage"),["text"],"e",1.0))
lib.append(my_data("#Eg","eV",_("Eg"),["text"],"e",1.0))
lib.append(my_data("#Xi","eV",_("Xi"),["text"],"e",1.0))
lib.append(my_data("#start_stop_time","s",_("Time of pause"),["text"],"e",1.0))
lib.append(my_data("#stopstart","1/0",_("Pause between iterations"),["1","0"],"e",1.0))
lib.append(my_data("#invert_current",_("True/False"),_("Invert output"),["text"],"e",1.0))
lib.append(my_data("#lr_bias",_("left/right"),_("Apply potential to  left/right of device"),[("leftright")],"s",1.0))
lib.append(my_data("#otherlayers","m",_("Other layers"),["text"],"e",1.0))

lib.append(my_data("#use_capacitor","1/0",_("Use capacitor"),["1","0"],"e",1.0))
lib.append(my_data("#stark_startime","s",_("startime"),["text"],"e",1.0))
lib.append(my_data("#stark_ea_factor","au",_("ea_factor"),["text"],"e",1.0))
lib.append(my_data("#stark_Np","1/0",_("Np"),["text"],"e",1.0))
lib.append(my_data("#stark_den","1/0",_("den"),["text"],"e",1.0))
lib.append(my_data("#stark_externalv","V",_("externalv"),["text"],"e",1.0))
lib.append(my_data("#stark_dt_neg_time","s",_("dt_neg_time"),["text"],"e",1.0))
lib.append(my_data("#stark_dt","s",_("dt"),["text"],"e",1.0))
lib.append(my_data("#stark_dt_mull","au",_("dt_mull"),["text"],"e",1.0))
lib.append(my_data("#stark_stop","s",_("stop"),["text"],"e",1.0))
lib.append(my_data("#stark_stark","1/0",_("stark"),["text"],"e",1.0))
lib.append(my_data("#stark_lasereff","1/0",_("lasereff"),["text"],"e",1.0))
lib.append(my_data("#stark_probe_wavelength","nm",_("wavelength"),["text"],"e",1e9))
lib.append(my_data("#stark_sim_contacts","1/0",_("sim_contacts"),["text"],"e",1.0))

#pulse
lib.append(my_data("#Rshort_pulse","Ohms",_("R_{short}"),["text"],"e",1.0))
lib.append(my_data("#pulse_bias","V",_("V_{bias}"),["text"],"e",1.0))
lib.append(my_data("#pulse_light_efficiency","au",_("Efficiency of light"),["text"],"e",1.0))
#
lib.append(my_data("#Rshort_imps","Ohms",_("R_{short}"),["text"],"e",1.0))
lib.append(my_data("#imps_sun","1=1 Sun",_("Backgroud light bias"),["text"],"e",1.0))
lib.append(my_data("#imps_modulation_max","1=1 Sun",_("Modulation depth"),["text"],"e",1.0))
lib.append(my_data("#imps_modulation_fx","Hz",_("Modulation frequency"),["text"],"e",1.0))
lib.append(my_data("#high_sun_scale","au",_("High light multiplyer"),["text"],"e",1.0))
lib.append(my_data("#Dphotoneff","0-1",_("Photon efficiency"),["text"],"e",1.0))

#jv.inp
lib.append(my_data("#jv_step_mul","0-2.0",_("JV voltage step multiplyer"),["text"],"e",1.0))
lib.append(my_data("#jv_max_j","A m^{-2}",_("Maximum current density"),["text"],"e",1.0))
lib.append(my_data("#jv_light_efficiency","au",_("JV curve photon generation efficiency"),["text"],"e",1.0))
lib.append(my_data("#jv_pmax_n","m^{-3}","Average carrier density at P_{max}",["text"],"e",1.0))
lib.append(my_data("#jv_pmax_tau","m^{-1}","Recombination time constant",["text"],"e",1.0))

#sim_info.dat
lib.append(my_data("#voc","V",_("V_{oc}"),["text"],"e",1.0))
lib.append(my_data("#pce","Percent",_("Power conversion efficiency"),["text"],"e",1.0))
lib.append(my_data("#ff","a.u.",_("Fill factor"),["text"],"e",1.0))

lib.append(my_data("#imps_r","Amps",_("Re(i)"),["text"],"e",1.0))
lib.append(my_data("#imps_i","Amps",_("Im(i)"),["text"],"e",1.0))
lib.append(my_data("#imps_Jr","Amps $m^{-2}$",_("Re(J)"),["text"],"e",1.0))
lib.append(my_data("#imps_Ji","Amps $m^{-2}$",_("Im(J)"),["text"],"e",1.0))
lib.append(my_data("#imps_fx","Hz",_("Frequency"),["text"],"e",1.0))
lib.append(my_data("#imps_delta_i","s",_("Phase shift"),["text"],"e",1.0))
lib.append(my_data("#imps_delta_g","s",_("Phase shift"),["text"],"e",1.0))
lib.append(my_data("#imps_delta_phase","s",_("Phase shift"),["text"],"e",1.0))
lib.append(my_data("#imps_points","s",_("points"),["text"],"e",1.0))
lib.append(my_data("#imps_n","s",_("Wavelengths to simulate"),["text"],"e",1.0))
lib.append(my_data("#imps_Vexternal","Volts",_("External voltage"),["text"],"e",1.0))

lib.append(my_data("#Cext","C",_("External C"),["text"],"e",1.0))
lib.append(my_data("#Rext","Ohms",_("External R"),["text"],"e",1.0))

lib.append(my_data("#Rscope","Ohms",_("Resistance of scope"),["text"],"e",1.0))
lib.append(my_data("#srh_bands","bands",_("Number of traps"),["text"],"s",1.0))

lib.append(my_data("#dostype","au",_("DoS distribution"),["exponential","complex"],"s",1.0))

lib.append(my_data("#sun_voc_single_point","1/0",_("Single point"),["1","0"],"e",1.0))
lib.append(my_data("#sun_voc_Psun_start","Suns",_("Start intensity"),["text"],"e",1.0))
lib.append(my_data("#sun_voc_Psun_stop","Suns",_("Stop intensity"),["text"],"e",1.0))
lib.append(my_data("#sun_voc_Psun_mul","au",_("step multiplier"),["text"],"e",1.0))


lib.append(my_data("#simplephotondensity","m^{-2}s^{-1}",_("Photon Flux"),["text"],"e",1.0))
lib.append(my_data("#simple_alpha","m^{-1}",_("Absorption"),["text"],"e",1.0))
lib.append(my_data("#xlen","m",_("device width"),["text"],"e",1.0))
lib.append(my_data("#zlen","m",_("device breadth"),["text"],"e",1.0))
#translated to here

lib.append(my_data("#ver","","",["text"],"e",1.0))
lib.append(my_data("#dostype","","",["text"],"e",1.0))
lib.append(my_data("#me","","",["text"],"e",1.0))
lib.append(my_data("#mh","","",["text"],"e",1.0))
lib.append(my_data("#gendos","","",["text"],"e",1.0))
lib.append(my_data("#notused","","",["text"],"e",1.0))
lib.append(my_data("#notused","","",["text"],"e",1.0))
lib.append(my_data("#Tstart","","",["text"],"e",1.0))
lib.append(my_data("#Tstop","","",["text"],"e",1.0))
lib.append(my_data("#Tpoints","","",["text"],"e",1.0))
lib.append(my_data("#nstart","","",["text"],"e",1.0))
lib.append(my_data("#nstop","","",["text"],"e",1.0))
lib.append(my_data("#npoints","","",["text"],"e",1.0))
lib.append(my_data("#nstart","","",["text"],"e",1.0))
lib.append(my_data("#nstop","","",["text"],"e",1.0))
lib.append(my_data("#npoints","","",["text"],"e",1.0))
lib.append(my_data("#srhbands","","",["text"],"e",1.0))
lib.append(my_data("#srh_start","","",["text"],"e",1.0))
lib.append(my_data("#srhvth_e","","",["text"],"e",1.0))
lib.append(my_data("#srhvth_h","","",["text"],"e",1.0))
lib.append(my_data("#srh_cut","","",["text"],"e",1.0))
lib.append(my_data("#lumodelstart","","",["text"],"e",1.0))
lib.append(my_data("#lumodelstop","","",["text"],"e",1.0))
lib.append(my_data("#homodelstart","","",["text"],"e",1.0))
lib.append(my_data("#homodelstop","","",["text"],"e",1.0))
lib.append(my_data("#gaus_mull","","",["text"],"e",1.0))
lib.append(my_data("#Esteps","","",["text"],"e",1.0))

#server.inp
lib.append(my_data("#server_cpus","au","Number of CPUs",["text"],"e",1.0))
lib.append(my_data("#server_stall_time","","",["text"],"e",1.0))
lib.append(my_data("#server_exit_on_dos_error","","",["text"],"e",1.0))
lib.append(my_data("#server_max_run_time","","",["text"],"e",1.0))
lib.append(my_data("#server_auto_cpus","","",["text"],"e",1.0))
lib.append(my_data("#server_min_cpus","","",["text"],"e",1.0))
lib.append(my_data("#server_steel","","",["text"],"e",1.0))
lib.append(my_data("#server_ip","au","Cluster IP",["text"],"e",1.0))
lib.append(my_data("#port","au","Cluster port",["text"],"e",1.0))
lib.append(my_data("#path_to_src","au","Path to source code",["text"],"e",1.0))
lib.append(my_data("#path_to_libs","au","Path to compiled libs for cluster",["text"],"e",1.0))
lib.append(my_data("#make_command","au","Make command",["text"],"e",1.0))
lib.append(my_data("#exe_name","au","exe name",["text"],"e",1.0))


lib.append(my_data("#invert_applied_bias","","",["text"],"e",1.0))
lib.append(my_data("#Rshort","","",["text"],"e",1.0))
lib.append(my_data("#Dphoton","","",["text"],"e",1.0))
lib.append(my_data("#interfaceleft","","",["text"],"e",1.0))
lib.append(my_data("#interfaceright","","",["text"],"e",1.0))
lib.append(my_data("#phibleft","","",["text"],"e",1.0))
lib.append(my_data("#phibright","","",["text"],"e",1.0))
lib.append(my_data("#vl_e","","",["text"],"e",1.0))
lib.append(my_data("#vl_h","","",["text"],"e",1.0))
lib.append(my_data("#vr_e","","",["text"],"e",1.0))
lib.append(my_data("#vr_h","","",["text"],"e",1.0))
lib.append(my_data("#light_model","","",["text"],"e",1.0))
lib.append(my_data("#NDfilter","","",["text"],"e",1.0))
lib.append(my_data("#plottime","","",["text"],"e",1.0))
lib.append(my_data("#startstop","","",["text"],"e",1.0))
lib.append(my_data("#plotfile","","",["text"],"e",1.0))


lib.append(my_data("#Rshort","","",["text"],"e",1.0))
lib.append(my_data("#solve_at_Vbi","","",["text"],"e",1.0))

#math.inp
lib.append(my_data("#maxelectricalitt_first","au","Max Electrical itterations (first step)",["text"],"e",1.0))
lib.append(my_data("#electricalclamp_first","au","Electrical clamp (first step)",["text"],"e",1.0))
lib.append(my_data("#math_electrical_error_first","au","Desired electrical solver error (first step)",["text"],"e",1.0))
lib.append(my_data("#math_enable_pos_solver","true/false","Enable poisson solver",[("switch")],"e",1.0))

lib.append(my_data("#maxelectricalitt","au",_("Max electrical itterations"),["text"],"e",1.0))
lib.append(my_data("#electricalclamp","au",_("Electrical clamp"),["text"],"e",1.0))
lib.append(my_data("#posclamp","au",_("Poisson clamping"),["text"],"e",1.0))
lib.append(my_data("#electricalerror","au",_("Minimum electrical error"),["text"],"e",1.0))
lib.append(my_data("#pos_max_ittr","au",_("Poisson solver max itterations"),["text"],"e",1.0))
lib.append(my_data("#newton_clever_exit","true/false","Newton solver clever exit",[("switch")],"e",1.0))
lib.append(my_data("#newton_min_itt","au",_("Newton minimum iterations"),["text"],"e",1.0))
lib.append(my_data("#solver_name","dll name",_("Matrix solver to use"),["text"],"e",1.0))
lib.append(my_data("#newton_name","dll name",_("Newton solver to use"),["text"],"e",1.0))



lib.append(my_data("#remesh","","",["text"],"e",1.0))
lib.append(my_data("#newmeshsize","","",["text"],"e",1.0))
lib.append(my_data("#epitaxy","","",["text"],"e",1.0))
lib.append(my_data("#alignmesh","","",["text"],"e",1.0))
lib.append(my_data("#stark_start_time","","",["text"],"e",1.0))



lib.append(my_data("#voc_nt","m^{-3}","Trapped electrons at Voc",["text"],"e",1.0))
lib.append(my_data("#voc_pt","m^{-3}","Trapped holes at Voc",["text"],"e",1.0))
lib.append(my_data("#voc_nf","m^{-3}","Free electrons at Voc",["text"],"e",1.0))
lib.append(my_data("#voc_pf","m^{-3}","Free holes at Voc",["text"],"e",1.0))
lib.append(my_data("#voc_np_tot","m^{-3}","Total carriers (n+p)/2 at Voc",["text"],"e",1.0))
lib.append(my_data("#voc_tau","s","Recombination time constant at Voc",["text"],"e",1.0))
lib.append(my_data("#voc_R","m^{-3}s^{-1}","Recombination rate at Voc",["text"],"e",1.0))
lib.append(my_data("#voc_J","A m^{-2}","Current density at Voc",["text"],"e",1.0))
lib.append(my_data("#voc_J_to_Jr","au","Ratio of conduction current to recombination current",["text"],"e",1.0))

lib.append(my_data("#voc_i","au","Current",["text"],"e",1.0))
lib.append(my_data("#kl_in_newton","1/0","KCL in Newton solver",["1","0"],"e",1.0))

lib.append(my_data("#simplexmul","au","simplex mull",["text"],"e",1.0))
lib.append(my_data("#simplex_reset","au","Reset steps",["text"],"e",1.0))

lib.append(my_data("#max_nfree_to_ptrap","m^{-3}s^{-1}","nfree_to_ptrap",["text"],"e",1.0))
lib.append(my_data("#max_pfree_to_ntrap","m^{-3}s^{-1}","max_pfree_to_ntrap",["text"],"e",1.0))
lib.append(my_data("#max_nrelax","m^{-3}s^{-1}","max_nrelax",["text"],"e",1.0))
lib.append(my_data("#max_prelax","m^{-3}s^{-1}","max_prelax",["text"],"e",1.0))

lib.append(my_data("#max_nfree","m^{-3}","max_nfree",["text"],"e",1.0))
lib.append(my_data("#max_pfree","m^{-3}","max_pfree",["text"],"e",1.0))
lib.append(my_data("#max_ntrap","m^{-3}","max_ntrap",["text"],"e",1.0))
lib.append(my_data("#max_ptrap","m^{-3}","max_ptrap",["text"],"e",1.0))
lib.append(my_data("#alpha_max_reduction","m^{-1}","alpha_max_reduction",["text"],"e",1.0))
lib.append(my_data("#alpha_max_increase","m^{-1}","alpha_max_increase",["text"],"e",1.0))

lib.append(my_data("#srh_n_r1","m^{-3}s^{-1}","srh electron rate 1",["text"],"e",1.0))
lib.append(my_data("#srh_n_r2","m^{-3}s^{-1}","srh electron rate 2",["text"],"e",1.0))
lib.append(my_data("#srh_n_r3","m^{-3}s^{-1}","srh electron rate 3",["text"],"e",1.0))
lib.append(my_data("#srh_n_r4","m^{-3}s^{-1}","srh electron rate 4",["text"],"e",1.0))

lib.append(my_data("#srh_p_r1","m^{-3}s^{-1}","srh hole rate 1",["text"],"e",1.0))
lib.append(my_data("#srh_p_r2","m^{-3}s^{-1}","srh hole rate 2",["text"],"e",1.0))
lib.append(my_data("#srh_p_r3","m^{-3}s^{-1}","srh hole rate 3",["text"],"e",1.0))
lib.append(my_data("#srh_p_r4","m^{-3}s^{-1}","srh hole rate 4",["text"],"e",1.0))

lib.append(my_data("#band_bend_max","percent","band bend max",["text"],"e",1.0))

lib.append(my_data("#gui_config_3d_enabled","true/false","Enable 3d effects",[("switch")],"e",1.0))

#fit
lib.append(my_data("#enabled",_("True/False"),_("Enable fit"),[("switch")],"e",1.0))
lib.append(my_data("#time_shift","s","time shift",["text"],"e",1.0))
lib.append(my_data("#start","s","start",["text"],"e",1.0))
lib.append(my_data("#stop","s","stop",["text"],"e",1.0))
lib.append(my_data("#log_x",_("True/False"),_("log x"),[("switch")],"e",1.0))
lib.append(my_data("#sim_data","filename","Fit file name",["text"],"e",1.0))
lib.append(my_data("#fit_error_mul","au","Fit error multiplyer",["text"],"e",1.0))

lib.append(my_data("#fit_invert_simulation_y",_("True/False"),_("Invert simulated data (y)"),[("switch")],"e",1.0))


#Thermal
lib.append(my_data("#Tll","Kelvin",_("Device temperature on left"),["text"],"e",1.0))
lib.append(my_data("#Tlr","Kelvin",_("Device temperature on right"),["text"],"e",1.0))
lib.append(my_data("#thermal",_("True/False"),_("Enable thermal solver"),[("switch")],"e",1.0))
lib.append(my_data("#thermal_l",_("True/False"),_("Lattice heat model"),[("switch")],"e",1.0))
lib.append(my_data("#thermal_e",_("True/False"),_("Electron heat model"),[("switch")],"e",1.0))
lib.append(my_data("#thermal_h",_("True/False"),_("Hole heat model"),[("switch")],"e",1.0))
lib.append(my_data("#thermal_kl","W m^{-1} C^{-1}","Thermal conductivity",["text"],"e",1.0))
lib.append(my_data("#Tliso",_("True/False"),_("Isothermal boundary on left"),[("switch")],"e",1.0))
lib.append(my_data("#Triso",_("True/False"),_("Isothermal boundary on right"),[("switch")],"e",1.0))
lib.append(my_data("#thermal_tau_e","s",("Electron relaxation time"),["text"],"e",1.0))
lib.append(my_data("#thermal_tau_h","s",("Hole relaxation time"),["text"],"e",1.0))
#
lib.append(my_data("#layer0","m","Active layer width",["text"],"e",1.0))
lib.append(my_data("#stark_saturate","au","Stark saturate",["text"],"e",1.0))

lib.append(my_data("#n_mul","au","n mul",["text"],"e",1.0))
lib.append(my_data("#alpha_mul","m^{-1}","Alpha mul",["text"],"e",1.0))

lib.append(my_data("#stark_point0","au","DR/R",["text"],"e",1.0))
lib.append(my_data("#stark_point1","au","DR/R",["text"],"e",1.0))
lib.append(my_data("#stark_point2","au","DR/R",["text"],"e",1.0))
lib.append(my_data("#stark_point3","au","DR/R",["text"],"e",1.0))
lib.append(my_data("#stark_point4","au","DR/R",["text"],"e",1.0))
lib.append(my_data("#stark_subtracted_value","s","subtracted value",["text"],"e",1.0))
lib.append(my_data("#light_energy","eV","Energy",["text"],"e",1.0))
lib.append(my_data("#sim_id","au","sim id",["text"],"e",1.0))


lib.append(my_data("#Rload","Ohms","External load resistor",["text"],"e",1.0))
lib.append(my_data("#pulse_shift","s","Shift of TPC signal",["text"],"e",1.0))

lib.append(my_data("#flip_field","au",_("Filp the opticl field"),["text"],["1","0"],1.0))

#dump.inp
lib.append(my_data("#newton_dump",_("True/False"),_("Dump from newton solver"),[("switch")],"e",1.0))
lib.append(my_data("#plot",_("True/False"),_("Plot bands etc.. "),[("switch")],"e",1.0))
lib.append(my_data("#dump_band_structure","","",["text"],"e",1.0))
lib.append(my_data("#dump_slices_by_time",_("True/False"),_("dump slices by time"),[("switch")],"e",1.0))
lib.append(my_data("#dump_1d_slices",_("True/False"),_("Dump 1D slices"),[("switch")],"e",1.0))
lib.append(my_data("#dump_slices",_("True/False"),_("Dump slices"),[("switch")],"e",1.0))
lib.append(my_data("#dump_dynamic",_("True/False"),_("Dump dynamic"),[("switch")],"e",1.0))
lib.append(my_data("#dump_zip_files",_("True/False"),_("Dump zip files"),[("switch")],"e",1.0))
lib.append(my_data("#dump_write_out_band_structure",_("True/False"),_("Write out band structure"),[("switch")],"e",1.0))
lib.append(my_data("#dump_iodump","","",["text"],"e",1.0))
lib.append(my_data("#dump_movie","","",["text"],"e",1.0))
lib.append(my_data("#dump_optics",_("True/False"),_("Dump optical information"),[("switch")],"e",1.0))
lib.append(my_data("#dump_optics_verbose","","",["text"],"e",1.0))
lib.append(my_data("#dump_print_newtonerror",_("True/False"),_("Print newton error"),[("switch")],"e",1.0))
lib.append(my_data("#dump_print_converge",_("True/False"),_("Print solver convergence"),[("switch")],"e",1.0))
lib.append(my_data("#dump_write_converge",_("True/False"),_("Write newton solver convergence to disk"),[("switch")],"e",1.0))
lib.append(my_data("#dump_print_pos_error",_("True/False"),_("Print poisson solver convergence"),[("switch")],"e",1.0))
lib.append(my_data("#dump_pl",_("True/False"),_("Dump PL spectra"),[("switch")],"e",1.0))
lib.append(my_data("#dump_norm_time_to_one",_("True/False"),_("Normalize output x-time to one"),[("switch")],"e",1.0))
lib.append(my_data("#dump_built_in_voltage",_("True/False"),_("Dump the built in voltage."),[("switch")],"e",1.0))
lib.append(my_data("#dump_optical_probe_spectrum",_("True/False"),_("Dump optical probe spectrum"),[("switch")],"e",1.0))
lib.append(my_data("#dump_optics_summary",_("True/False"),_("Dump optical summary"),[("switch")],"e",1.0))
lib.append(my_data("#dump_ray_trace_map",_("True/False"),_("Dump raytrace plots"),[("switch")],"e",1.0))
lib.append(my_data("#dumpitdos","","",["text"],"e",1.0))
lib.append(my_data("#dump_workbook",_("True/False"),_("Dump an excel workbook for each simulation run congaing the results."),[("switch")],"e",1.0))
lib.append(my_data("#dump_file_access_log",_("True/False"),_("Write file access log to disk."),[("switch")],"e",1.0))


lib.append(my_data("#pl_enabled",_("True/False"),_("Turn on luminescence"),[("switch")],"e",1.0))
lib.append(my_data("#pl_fe_fh","0.0-1.0",_("n_{free} to p_{free} photon generation efficiency"),["text"],"e",1.0))
lib.append(my_data("#pl_fe_te","0.0-1.0",_("n_{free} to n_{trap} photon generation efficiency"),["text"],"e",1.0))
lib.append(my_data("#pl_te_fh","0.0-1.0",_("n_{trap} to p_{free} photon generation efficiency"),["text"],"e",1.0))
lib.append(my_data("#pl_th_fe","0.0-1.0",_("p_{trap} to n_{free} photon generation efficiency"),["text"],"e",1.0))
lib.append(my_data("#pl_fh_th","0.0-1.0",_("p_{free} to p_{trap} photon generation efficiency"),["text"],"e",1.0))

lib.append(my_data("#free_to_free_recombination","0.0-1.0",_("n_{free} to p_{free} Recombination rate constant"),["text"],"e",1.0))

#LED
lib.append(my_data("#led_on",_("True/False"),_("Turn on LED"),[("switch")],"e",1.0))
lib.append(my_data("#led_wavelength","m",_("LED emission wavelength"),["text"],"e",1.0))
lib.append(my_data("#led_extract_eff","m",_("LED extraction efficiency"),["text"],"e",1.0))


def dump_lib():
	global lib
	for i in range(0, len(lib)):
		print(">",lib[i].token,"<>",lib[i].info,"<")

class tokens:

	def find(self,token):
		global lib
		for i in range(0, len(lib)):
			if lib[i].token==token.strip():
				if lib[i].units=="" and lib[i].info=="":
					return False
				else:
					return lib[i]

		#sys.stdout.write("Add -> lib.append(my_data(\""+token+"\",\"\",\"\",[\"text\"]))\n")
		return False
