# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 21:27:43 2021

@author: dugue
"""

from qrun10 import *

# a=[['1Cs2SnCl6_Bi',{'unitcell_pbe0_soc': {'cbm': 2.95338024,
# 'vbm': -2.38414132},
# 'relax_grd_pbe0_soc': (2.70157, -170.98961),
# 'grdm1_pbe0_soc': {'vb': False,
# 's': 0.04944037,
# 'p': 3.73125418,
# 'cb': 3.74958017},
# 'relax_ex_cz_pbe0_soc': (2.7588566666666665, -167.37741),
# 'ex_at_grd_pbe0_soc': (2.70157, -167.30737),
# 'grd_at_ex_cz_pbe0_soc': (2.7588566666666665, -170.89175),
# 'relax_ex_cb_pbe0_soc': (2.5844966666666664, -168.18951),
# 'ex_cb_at_grd_pbe0_soc': (2.70157, -167.36352),
# 'grd_at_ex_cb_pbe0_soc': (2.5844966666666664, -170.09567),
# 'ex_vb_at_grd_m1_pbe0_soc': False,
# 'ex_vc_at_grd_m1_pbe0_soc': False,
# 'ex_at_grd_m1_pbe0_soc': (2.70157, -167.30779619),
# 'ex_cb_at_grd_m1_pbe0_soc': (2.70157, -167.2894702)} ] ,
# ['1KCl_Bi',{'unitcell_pbe0_soc': {'cbm': 4.14304064,
# 'vbm': -3.81710397},
# 'relax_grd_pbe0_soc': (0, -292.22226),
# 'grdm1_pbe0_soc': {'vb': -2.59447564,
# 's': False,
# 'p': 2.33571593,
# 'cb': 4.17688306},
# 'relax_ex_ez_pbe0_soc': (0.24723333333333342, -288.63279),
# 'relax_ex_cz_pbe0_soc': (-0.06251999999999969, -288.60601),
# 'grd_at_ex_ez_pbe0_soc': (0.24723333333333342, -291.84716),
# 'ex_at_grd_pbe0_soc': (0, -288.52044),
# 'grd_at_ex_cz_pbe0_soc': (-0.06251999999999969, -292.10461),
# 'ex_at_grd_m1_pbe0_soc': False,
# 'ex_cb_at_grd_m1_pbe0_soc': False} ] ,
# ['1KCl_Bi_next',
# {'relax_grd_pbe0_soc': (0, -283.15803),
# 'relax_ex_ez_pbe0_soc': (0.378, -279.80553),
# 'grd_at_ex_ez_pbe0_soc': (0.378, -282.56979),
# 'ex_at_grd_pbe0_soc': (0, -279.51552)}] ,
# ['1KCl_Bi_nearest',
# {'relax_grd_pbe0_soc': (0, -282.75922),
# 'relax_ex_ez_pbe0_soc': (0.398, -279.39353),
# 'grd_at_ex_ez_pbe0_soc': (0.398, -282.13304),
# 'ex_at_grd_pbe0_soc': (0, -279.09185)}] ,
# ['1Cs2NaYCl6_Bi',{'unitcell_pbe0_soc': {'cbm': 5.30404598,
# 'vbm': -2.633805},
# 'relax_grd_pbe0_soc': (2.6978766666666663, -217.09273),
# 'grdm1_pbe0_soc': {'vb': False,
# 's': -0.92275257,
# 'p': 2.86950413,
# 'cb': 5.60461592},
# 'relax_ex_cz_pbe0_soc': (2.7395333333333336, -213.35348),
# 'ex_at_grd_pbe0_soc': (2.6978766666666663, -213.30904),
# 'grd_at_ex_cz_pbe0_soc': (2.7395333333333336, -217.03661),
# 'ex_vb_at_grd_m1_pbe0_soc': False,
# 'ex_vc_at_grd_m1_pbe0_soc': False,
# 'ex_at_grd_m1_pbe0_soc': (2.6978766666666663, -213.3004733),
# 'ex_cb_at_grd_m1_pbe0_soc': (2.6978766666666663, -210.56536151)} ] ,
# ['1Cs2AgInCl6_Bi',{'ex_vb_at_grd_pbe0_soc':(2.67301,3.23+-173.46748),'unitcell_pbe0_soc': {'cbm': 3.04752896,
# 'vbm': -0.97949383},
# 'relax_grd_pbe0_soc': (2.67301, -173.46748),
# 'grdm1_pbe0_soc': {'vb': False,
# 's': 0.56780567,
# 'p': 3.88607628,
# 'cb': 3.95157254},
# 'relax_ex_cb_pbe0_soc': (2.6016266666666668, -170.65944),
# 'ex_cb_at_grd_pbe0_soc': (2.67301, -170.28953),
# 'grd_at_ex_cb_pbe0_soc': (2.6016266666666668, -173.07429),
# 'relax_ex_vb_pbe0_soc': (2.8580066666666664, -170.91217),
# 'grd_at_ex_vb_pbe0_soc': (2.8580066666666664, -172.39884),
# 'ex_vb_at_grd_m1_pbe0_soc': False,
# 'ex_vc_at_grd_m1_pbe0_soc': False,
# 'ex_at_grd_m1_pbe0_soc': (2.67301, -170.14920938999998),
# 'ex_cb_at_grd_m1_pbe0_soc': (2.67301, -170.08371313)} ] ,
# ['1Cs2NaYCl6_Sb',{'unitcell_pbe0_soc': {'cbm': 5.30404598,
# 'vbm': -2.633805},
# 'relax_grd_pbe0_soc': (0, -216.49867),
# 'grdm1_pbe0_soc': {'vb': False,
# 's': -0.20590912,
# 'p': 3.49135372,
# 'cb': 5.58734649},
# 'relax_ex_ez_pbe0_soc': (0.2689066666666666, -213.2863),
# 'relax_ex_cz_pbe0_soc': (-0.1477400000000002, -212.97476),
# 'grd_at_ex_ez_pbe0_soc': (0.2689066666666666, -215.90575),
# 'ex_at_grd_pbe0_soc': (0, -212.83255),
# 'grd_at_ex_cz_pbe0_soc': (-0.1415133333333336, -216.30725),
# 'ex_vb_at_grd_m1_pbe0_soc': False,
# 'ex_vc_at_grd_m1_pbe0_soc': False,
# 'ex_at_grd_m1_pbe0_soc': (0, -212.80140716),
# 'ex_cb_at_grd_m1_pbe0_soc': (0, -210.70541439000002)} ] ,
# ['1Cs2SnCl6_vcl_Bi',{'ex_cb_at_grd_pbe0_soc':(2.632476,4.13+-167.49527),'unitcell_pbe0_soc': {'cbm': 2.95338024,
# 'vbm': -2.38414132},
# 'relax_grd_pbe0_soc': (2.6324759999999996, -167.49527),
# 'grdm1_pbe0_soc': {'vb': False,
# 's': -0.47437459,
# 'p': 2.93483269,
# 'cb': 3.65985896},
# 'relax_ex_ez_pbe0_soc': (2.664046, -164.67042),
# 'grd_at_ex_ez_pbe0_soc': (2.664046, -167.02584),
# 'ex_at_grd_pbe0_soc': (2.6324759999999996, -164.17573),
# 'relax_ex_cb_pbe0_soc': (2.527642, -164.38448),
# 'grd_at_ex_cb_pbe0_soc': (2.527642, -166.45938),
# 'ex_vb_at_grd_m1_pbe0_soc': False,
# 'ex_vc_at_grd_m1_pbe0_soc': False,
# 'ex_at_grd_m1_pbe0_soc': (2.6324759999999996, -164.08606272),
# 'ex_cb_at_grd_m1_pbe0_soc': (2.6324759999999996, -163.36103645)} ] ,
# ["1Cs2KInCl6oh_Sb",{'unitcell_pbe0_soc': {'cbm': 3.63614871,
# 'vbm': -2.62780562},
# 'relax_grd_pbe0_soc': (0, -185.07925),
# 'relax_ex_ez_pbe0_soc': (0.21765999999999996, -181.56378),
# 'relax_ex_cz_pbe0_soc': (-0.11966666666666681, -181.33801),
# 'grd_at_ex_ez_pbe0_soc': (0.21773333333333333, -184.57274),
# 'ex_at_grd_pbe0_soc': (0, -181.22853),
# 'grd_at_ex_cz_pbe0_soc': (-0.11966666666666681, -184.91581),}],
# # 'relax_ex_cb_pbe0_soc': (0, -182.18265),
# # 'grd_at_ex_cb_pbe0_soc': (0, -183.12604)}],
# ["1Cs2NaInCl6_Bi",{'unitcell_pbe0_soc': {'cbm': 3.77793364,
# 'vbm': -2.12308402},
# 'relax_grd_pbe0_soc': (2.68561, -186.06305),
# 'relax_ex_cz_pbe0_soc': (2.72114, -182.24045),
# 'ex_at_grd_pbe0_soc': (2.68561, -182.20299),
# 'grd_at_ex_cz_pbe0_soc': (2.72114, -186.01608),
# 'relax_ex_cb_pbe0_soc': (2.5682933333333335, -182.0471),
# 'grd_at_ex_cb_pbe0_soc': (2.5682933333333335, -185.16788),
# 'ex_cb_at_grd_pbe0_soc': (2.68561, -181.15989868)}],
# ["1Rb3InCl6oh_Sb",{'unitcell_pbe0_soc': {'cbm': 3.24773793,
# 'vbm': -3.12202104},
# 'relax_grd_pbe0_soc': (0, -181.28723),
# 'relax_ex_ez_pbe0_soc': (0.21095333333333333, -177.66977),
# 'relax_ex_cz_pbe0_soc': (-0.11660000000000004, -177.45518),
# 'grd_at_ex_ez_pbe0_soc': (0.21095333333333333, -180.75952),
# 'ex_at_grd_pbe0_soc': (0, -177.34484),
# 'grd_at_ex_cz_pbe0_soc': (-0.11660000000000004, -181.12165),}],
# ["1Rb3InCl6c2h_Sb",{'unitcell_pbe0_soc': {'cbm': 3.24773793,
# 'vbm': -3.12202104},
# 'relax_grd_pbe0_soc': (0, -723.68482),
# 'relax_ex_ez_pbe0_soc': (0.368106667, -720.72914),
# 'grd_at_ex_ez_pbe0_soc': (0.368106667, -722.85577),
# 'ex_at_grd_pbe0_soc': (0, -720.06139),}],]
# 'relax_ex_cb_pbe0_soc': (0, -178.11286),
# 'grd_at_ex_cb_pbe0_soc': (0, -180.08867),}]]

# a=[["Bi(Cs)3+",{'relax_grd_pbe0_soc': (0, 0),
# 'relax_ex_ez_pbe0_soc': (0.368106667, 2.51),
# 'grd_at_ex_ez_pbe0_soc': (0.368106667, 2.51-1.3),
# 'ex_at_grd_pbe0_soc': (0, 3.49),}]]

a=[["Bi3+ with VNa",{'relax_grd_pbe0_soc': (0, 0),
'relax_ex_ez_pbe0_soc': (1, 3.41),
'grd_at_ex_ez_pbe0_soc': (1, 0.16),
'ex_at_grd_pbe0_soc': (0, 3.52),}]]

for i in a:
    if i[0]=='1Cs2NaYCl6_Bi':
        plot_cc3(i[1],i[0],2.65,2.8,-0.1,0.5,3.5,4.1,0.1)
    elif i[0]=='1KCl_Bi':
        plot_cc3(i[1],i[0],-0.15,0.35,-0.2,0.6,3.4,4.2,0.25)
    elif i[0]=='1KCl_Bi_nearest':
        plot_cc3(i[1],i[0],-0.05,0.45,-0.1,0.9,3,4,0.2)
        
    else:
        plot_cc2(i[1],i[0])