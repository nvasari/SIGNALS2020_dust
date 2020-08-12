'''
Clever calculator for dust stuff.

Natalia@UFSC - 30/Aug/2018
'''

# --------------------------------------------------------------------
def get_labels(ps='stix'):
    
    labels = {
        'a'                     : r'$a$'                                                                                                        ,
        'log_a'                 : r'$\log\; e^\tau$'                                                                                            ,
        'at_flux'               : r'$\langle \log t_\star \rangle \;\mathrm{[yr]}$'                                                             ,
        'AV_Balmer'             : r'$A_V^\mathrm{neb} \;\mathrm{[mag]}$'                                                                        ,
        'dZ'                    : r'$\Delta\log \mathrm{O/H}$'                                                                                  ,
        'D4000'                 : r'$D_n(4000)$'                                                                                                ,
        'dr_max_R50'            : r'$R_\mathrm{max}/R_{50}$'                                                                                    ,
        'El_EW_6563'            : r'$W_\mathrm{H\alpha}^\mathrm{obs} \;\mathrm{[\AA]}$'                                                         ,
        'El_F_6563'             : r'$F_\mathrm{H\alpha}^\mathrm{obs} \;\mathrm{[10^{-17} erg s^{-1} cm^{-2}]}$'                                 ,
        'f_LHa_dr_good'         : r'$f_{L_\mathrm{IFS}}(\mathrm{spx}\; A/N > 2)$'                                                               ,
        'HaHb'                  : r'$\log \mathrm{H\alpha}/\mathrm{H\beta}$'                                                                    ,
        'LHa_I/LHa_G'           : r'$L_\mathrm{IFS}/L_\mathrm{G}$'                                                                              ,
        'LHa_ISF/LHa_G'         : r'$L_\mathrm{SF}/L_\mathrm{G}$'                                                                               ,
        'LHa_I/LHa_Gp'          : r'$L_\mathrm{IFS}/L_\mathrm{G}^\prime$'                                                                       ,
        'LHa_Gp/LHa_G'          : r'$L_\mathrm{G}^\prime/L_\mathrm{G}$'                                                                         ,
        'LHa_obs_Gp/LHa_obs_G'  : r'$L_\mathrm{G,obs}^\prime/L_\mathrm{G,obs}$'                                                                 ,
        'LHb_obs_Gp/LHb_obs_G'  : r'$L_\mathrm{G\beta,obs}^\prime/L_\mathrm{G\beta,obs}$'                                                       ,
        'LHa_G'                 : r'$L(\mathrm{H\alpha})_\mathrm{G} \;\mathrm{[L_\odot]}$'                                                      ,
        'LHa_Gp'                : r'$L_\mathrm{G}^\prime$'                                                                                      ,
        'LHa_obs'               : r'$L(\mathrm{H\alpha})_\mathrm{G,obs} \;\mathrm{[L_\odot]}$'                                                  ,
        'LHa_obs/Mcor'          : r'$L(\mathrm{H\alpha})_\mathrm{G,obs}/M_\mathrm{\star,G} \;\mathrm{[L_\odot \, M_\odot^{-1}]}$'               ,
        'Lobn'                  : r'$L_\mathrm{\lambda=5635\,\normalsize\AA} \;\mathrm{[L_\odot \;\AA^{-1}]}$'                                  ,
        'linHaHb_int'           : r'$(\mathrm{H\alpha}/\mathrm{H\beta})_\mathrm{int}$'                                                          ,
        'linS2Ha'               : r'[S {\scshape ii}]/$\mathrm{H\alpha}$'                                                                       ,
        'log a/a_ave'           : r'$\log\, e^{\tau_\mathrm{j}}/ \langle e^{\tau_\mathrm{j}} \rangle$'                                          ,
        'log_FHb_ave'           : r'$\log \, \langle F_\mathrm{H\beta} \rangle$ [erg s$^{-1}$ cm$^{-2}$]'                                       ,
        'log_LHa'               : r'$\log L_\mathrm{H\alpha} \;\mathrm{[L_\odot]}$'                                                             ,
        'log_LHa_G'             : r'$\log L_\mathrm{G}$'                                                                                        ,
        'log_LHa_Gp'            : r'$\log L_\mathrm{G}^\prime$'                                                                                 ,
        'log LHa/LHa_ave'       : r'$\log\, l_\mathrm{j}^\mathrm{obs}/ \langle l^\mathrm{obs} \rangle$'                                         ,
        'log LHa_dr/LHa_ave_dr' : r'$\log\, l_\mathrm{j}^\mathrm{obs} e^{\tau_\mathrm{j}}/ \langle l^\mathrm{obs} \rangle e^{\tau_\mathrm{G}}$' ,
        'log_SFR_Ha'            : r'$\log \mathrm{SFR} \;\mathrm{[M_\odot yr^{-1}]}$'                                                           ,
        'log_surfHa_ave'        : r'$\log \Sigma_\mathrm{H\alpha} / \langle \Sigma_\mathrm{H\alpha} \rangle$'                                   ,
        'SurfMass'              : r'$\Sigma_\mathrm{M_\star} \;\mathrm{[M_\odot\, kpc^{-2}]}$'                                                  ,
        'surfHa'                : r'$\Sigma_\mathrm{H\alpha} \;\mathrm{[L_\odot\, kpc^{-2}]}$'                                                  ,
        'log_surfHa'            : r'$\log \Sigma_\mathrm{H\alpha} \;\mathrm{[L_\odot\, kpc^{-2}]}$'                                             ,
        'log_surfHa_dr'         : r'$\log \Sigma_\mathrm{H\alpha}^\mathrm{dr} \;\mathrm{[L_\odot\, kpc^{-2}]}$'                                 ,
        'log_WHa'               : r'$\log W_\mathrm{H\alpha} \;\mathrm{[\AA]}$'                                                                 ,
        'log_WHa_dr'            : r'$\log W_\mathrm{H\alpha}^\mathrm{dr} \;\mathrm{[\AA]}$'                                                     ,
        'Mcor'                  : r'$M_\mathrm{\star} \;\mathrm{[M_\odot]}$'                                                                    ,
        'pixel_scale_pc'        : r'Sampling [pc]'                                                                                              ,
        'q'                     : r'$q$'                                                                                                        ,
        'R_V'                   : r'$R_V$'                                                                                                      ,
        'sig'                   : r'$\sigma$'                                                                                                   ,
        'sig_u'                 : r'$\sigma_u$'                                                                                                 ,
        }
    
    if (ps != 'minion'):
        labels = {k: r'$\mathdefault{%s}$' % v.replace('$', '').replace('\log', '\log\,') for k, v in labels.items()}

    return labels
# --------------------------------------------------------------------
