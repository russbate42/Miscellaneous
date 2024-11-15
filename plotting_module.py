''' 
Russell Bate
russell.bate@cern.ch, russellbate@phas.ubc.ca

Module which contains plotting functions as well as dictionaries
'''

import numpy as np
import matplotlib.pyplot as plt
import atlas_mpl_style as ampl # ATLAS Style
ampl.use_atlas_style()
import matplotlib.colors as mplc
import matplotlib.cm as cm

def plot_data_per_trigger(data,
        var,
        var_dict,
        axis_coordinates=[.12,.16,.825,.775],
        show=True,
        save_fig=False,
        save_fig_name=''
        ):
    fig = plt.figure(figsize=(6,4), dpi=200)
    
    var_range = var_dict['range']
    var_hist_x = var_range[:-1] + .5 * (var_range[1] - var_range[0])
    
    # create dictionaries for each trigger/axes object
    ax_dict = dict()
    np_hist_dict = dict()
    # loop through triggers
    for key, val in data.items():
        np_hist_dict[key], *rest = np.histogram(val,
                           bins=var_range)
        ax_dict[key] = fig.add_axes(axis_coordinates)
        ax_dict[key].scatter(var_hist_x, np_hist_dict[key],
                   color='black', s=8, label=key)

    #ampl.draw_atlas_label(0.05, 0.9, ax=plt.gca(), status='', simulation=True,
    #                    energy='13.0 TeV', desc=f"Data 2017")
    
    ax.legend()
    if show == True:
        plt.show()
    if save_fig == True:
        format = save_fig_name.split('.')[-1]
        plt.save_fig(save_fig_name, format=format)

    return fig

plot_vars = ["H1_pt", "H1_eta", "H1_phi", "H1_mass", "H1_energy",
    "H2_pt", "H2_eta", "H2_phi", "H2_mass", "H2_energy"]
jz_slices = ['JZ1', 'JZ2', 'JZ3', 'JZ4', 'JZ5', 'JZ6', 'JZ7', 'JZ8', 'JZ9']

plt_dct = dict()
plt_dct["truth_H1_pt"] = {}
plt_dct["truth_H2_pt"] = {}
plt_dct["truth_H_pt"] = {}
plt_dct["truth_H1_eta"] = {}
plt_dct["truth_H2_eta"] = {}
plt_dct["truth_H_eta"] = {}
plt_dct["truth_H1_phi"] = {}
plt_dct["truth_H2_phi"] = {}
plt_dct["truth_H_phi"] = {}
plt_dct["truth_H1_mass"] = {}
plt_dct["truth_H2_mass"] = {}
plt_dct["truth_H_mass"] = {}
plt_dct["nlrjets"] = {}
plt_dct["H1_pt"] = {'range' : 0}
plt_dct["H1_eta"] = {}
plt_dct["H1_phi"] = {}
plt_dct["H1_mass"] = {}
plt_dct["H1_energy"] = {}
plt_dct["H2_pt"] = {}
plt_dct["H2_eta"] = {}
plt_dct["H2_phi"] = {}
plt_dct["H2_mass"] = {}
plt_dct["H2_energy"] = {}
plt_dct["HH_pt"] = {}
plt_dct["HH_eta"] = {}
plt_dct["HH_phi"] = {}
plt_dct["HH_mass"] = {}
plt_dct["HH_energy"] = {}
plt_dct["lrj_2_valid"] = {}
plt_dct["lrj_2_pt"] = {}
plt_dct["lrj_2_eta"] = {}
plt_dct["lrj_2_phi"] = {}
plt_dct["lrj_2_mass"] = {}
plt_dct["lrj_2_phbb"] = {}
plt_dct["lrj_2_GN2Xv01_phbb"] = {}
plt_dct["lrj_2_phcc"] = {}
plt_dct["lrj_2_GN2Xv01_phcc"] = {}
plt_dct["lrj_2_ptop"] = {}
plt_dct["lrj_2_GN2Xv01_ptop"] = {}
plt_dct["lrj_2_pqcd"] = {}
plt_dct["lrj_3_valid"] = {}
plt_dct["lrj_3_pt"] = {}
plt_dct["lrj_3_eta"] = {}
plt_dct["lrj_3_phi"] = {}
plt_dct["lrj_3_mass"] = {}
plt_dct["lrj_3_phbb"] = {}
plt_dct["lrj_3_phcc"] = {}
plt_dct["lrj_3_ptop"] = {}
plt_dct["lrj_3_pqcd"] = {}



all_vars = ["runNumber",
"eventNumber",
"trigPassed_HLT_j420_a10_lcw_L1J100",
"trigPassed_HLT_j420_a10r_L1J100",
"trigPassed_HLT_j175_bmv2c2040_split",
"trigPassed_HLT_j225_bmv2c2060_split",
"trigPassed_HLT_2j35_bmv2c2060_split_2j35_L14J15p0ETA25",
"trigPassed_HLT_2j55_bmv2c2060_split_ht300_L14J15",
"trigPassed_HLT_j100_2j55_bmv2c2060_split",
"trigPassed_HLT_j150_bmv2c2060_split_j50_bmv2c2060_split",
"generatorWeight_NOSYS",
"PileupWeight_NOSYS",
"gen_and_pu_weight",
"truth_H1_pt",
"truth_H2_pt",
"truth_H_pt",
"truth_H1_eta",
"truth_H2_eta",
"truth_H_eta",
"truth_H1_phi",
"truth_H2_phi",
"truth_H_phi",
"truth_H1_mass",
"truth_H2_mass",
"truth_H_mass",
"nlrjets",
"H1_pt",
"H1_eta",
"H1_phi",
"H1_mass",
"H1_energy",
"H2_pt",
"H2_eta",
"H2_phi",
"H2_mass",
"H2_energy",
"HH_pt",
"HH_eta",
"HH_phi",
"HH_mass",
"HH_energy",
"lrj_2_valid",
"lrj_2_pt",
"lrj_2_eta",
"lrj_2_phi",
"lrj_2_mass",
"lrj_2_phbb",
"lrj_2_GN2Xv01_phbb",
"lrj_2_phcc",
"lrj_2_GN2Xv01_phcc",
"lrj_2_ptop",
"lrj_2_GN2Xv01_ptop",
"lrj_2_pqcd",
"lrj_2_GN2Xv01_pqcd",
"lrj_2_GN2Xv01_50",
"lrj_2_GN2Xv01_55",
"lrj_2_GN2Xv01_60",
"lrj_2_GN2Xv01_65",
"lrj_2_GN2Xv01_70",
"lrj_2_GN2Xv01_75",
"lrj_2_GN2Xv01_80",
"lrj_2_GN2Xv01_85",
"lrj_3_valid",
"lrj_3_pt",
"lrj_3_eta",
"lrj_3_phi",
"lrj_3_mass",
"lrj_3_phbb",
"lrj_3_GN2Xv01_phbb",
"lrj_3_phcc",
"lrj_3_GN2Xv01_phcc",
"lrj_3_ptop",
"lrj_3_GN2Xv01_ptop",
"lrj_3_pqcd",
"lrj_3_GN2Xv01_pqcd",
"lrj_3_GN2Xv01_50",
"lrj_3_GN2Xv01_55",
"lrj_3_GN2Xv01_60",
"lrj_3_GN2Xv01_65",
"lrj_3_GN2Xv01_70",
"lrj_3_GN2Xv01_75",
"lrj_3_GN2Xv01_80",
"lrj_3_GN2Xv01_85",
"lrj_4_valid",
"lrj_4_pt",
"lrj_4_eta",
"lrj_4_phi",
"lrj_4_mass",
"lrj_4_phbb",
"lrj_4_GN2Xv01_phbb",
"lrj_4_phcc",
"lrj_4_GN2Xv01_phcc",
"lrj_4_ptop",
"lrj_4_GN2Xv01_ptop",
"lrj_4_pqcd",
"lrj_4_GN2Xv01_pqcd",
"lrj_4_GN2Xv01_50",
"lrj_4_GN2Xv01_55",
"lrj_4_GN2Xv01_60",
"lrj_4_GN2Xv01_65",
"lrj_4_GN2Xv01_70",
"lrj_4_GN2Xv01_75",
"lrj_4_GN2Xv01_80",
"lrj_4_GN2Xv01_85",
"lrj_5_valid",
"lrj_5_pt",
"lrj_5_eta",
"lrj_5_phi",
"lrj_5_mass",
"lrj_5_phbb",
"lrj_5_GN2Xv01_phbb",
"lrj_5_phcc",
"lrj_5_GN2Xv01_phcc",
"lrj_5_ptop",
"lrj_5_GN2Xv01_ptop",
"lrj_5_pqcd",
"lrj_5_GN2Xv01_pqcd",
"lrj_5_GN2Xv01_50",
"lrj_5_GN2Xv01_55",
"lrj_5_GN2Xv01_60",
"lrj_5_GN2Xv01_65",
"lrj_5_GN2Xv01_70",
"lrj_5_GN2Xv01_75",
"lrj_5_GN2Xv01_80",
"lrj_5_GN2Xv01_85",
"srj_0_valid",
"srj_0_pt",
"srj_0_eta",
"srj_0_phi",
"srj_0_mass",
"srj_1_valid",
"srj_1_pt",
"srj_1_eta",
"srj_1_phi",
"srj_1_mass",
"srj_2_valid",
"srj_2_pt",
"srj_2_eta",
"srj_2_phi",
"srj_2_mass",
"srj_3_valid",
"srj_3_pt",
"srj_3_eta",
"srj_3_phi",
"srj_3_mass",
"srj_4_valid",
"srj_4_pt",
"srj_4_eta",
"srj_4_phi",
"srj_4_mass",
"srj_5_valid",
"srj_5_pt",
"srj_5_eta",
"srj_5_phi",
"srj_5_mass",
"H1_GN2Xv01_phbb",
"H1_GN2Xv01_phcc",
"H1_GN2Xv01_ptop",
"H1_GN2Xv01_pqcd",
"H2_GN2Xv01_phbb",
"H2_GN2Xv01_phcc",
"H2_GN2Xv01_ptop",
"H2_GN2Xv01_pqcd",
"H1_GN2Xv01_Disc",
"H2_GN2Xv01_Disc",
"H1_GN2Xv01_50",
"H2_GN2Xv01_50",
"H1_GN2Xv01_55",
"H2_GN2Xv01_55",
"H1_GN2Xv01_60",
"H2_GN2Xv01_60",
"H1_GN2Xv01_65",
"H2_GN2Xv01_65",
"H1_GN2Xv01_70",
"H2_GN2Xv01_70",
"H1_GN2Xv01_75",
"H2_GN2Xv01_75",
"H1_GN2Xv01_80",
"H2_GN2Xv01_80",
"H1_GN2Xv01_85",
"H2_GN2Xv01_85",
"VBFj1_pt",
"VBFj1_eta",
"VBFj1_phi",
"VBFj1_mass",
"VBFj1_energy",
"VBFj2_pt",
"VBFj2_eta",
"VBFj2_phi",
"VBFj2_mass",
"VBFj2_energy",
"VBFjj_mass",
"VBFjj_DeltaEta",
"PassVBFJets",
"X_hhBoostedVBF",
"X_hhBoostedGGF"]
