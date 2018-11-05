# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 14:41:23 2018

@author: Tsende
"""

import numpy as np
import matplotlib.pyplot as plt

L = np.arange(0,5,0.1)
GVD = 36*1e-30
GDD = GVD*L
T_in = 4*1e-15
T_out = T_in*np.sqrt(1+(4*np.log(2)*(GDD/(T_in)**2))**2)

plt.style.use('dark_background')


plt.semilogy(L,T_out/1e-15, 'white')
plt.xlabel('Material thickness (mm)')
plt.ylabel('Pulse duration (fs)')
plt.title('Dispersion effect on pulse duration')
plt.grid(which='both',linestyle='-.', linewidth='0.5', color='grey')

##ax.set_xticks(xmajor_ticks)                                                       
##ax.set_xticks(xminor_ticks, minor=True)                                           
#ax.set_yticks(ymajor_ticks)                                                       
#ax.set_yticks(yminor_ticks, minor=True)                                           

# and a corresponding grid                                                       

#plt.grid(which='both')                                                            

# or if you want differnet settings for the grids:                               
#ax.grid(which='minor', alpha=0.2)                                                
#ax.grid(which='major', alpha=0.5)

plt.savefig("Dispersion effect.png", dpi=600)