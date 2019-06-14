#import packages

import matplotlib.pyplot as plt
import numpy as np
import time
import pandas as pn
#import scipy.io as spi
import matlab.engine as mle

#define data path
filepath = ['/home/amke/Documents/projects/modelling-package/experiment-SACLA/SACLA2015_elisa/DATA']    #alternative: ['./']
filename = ['H20_long.mat']

#load matlab file
eng = mle.start_matlab()
expData = eng.load('H20_long.mat')
qmat = eng.getfield(expData, 'q')
tmat = eng.getfield(expData, 'Delays')
dS_expmat = eng.getfield(expData, 'AllTTDelay')

#define q range and time range
q_min = [1]
q_max = [5]
t_min = [-10]
t_max = [100000]


#cut data according to defined q and time range
q_old = np.asarray(qmat)
q = q_old[(q_old>q_min)&(q_old<q_max)]
t_old = np.asarray(tmat)
t = t_old[(t_old>t_min)&(t_old<t_max)]
dS_exp = np.asarray(dS_expmat)
q_mask =(q_old>q_min)&(q_old<q_max)
t_mask = (t_old>t_min)&(t_old<t_max)
dS_exp = np.delete(dS_exp, np.where(q_mask == False), 0)
dS_exp = np.delete(dS_exp, np.where(t_mask == False), 1)
dS_exp_t = np.transpose(dS_exp)

#set parameters for sine fourier transform
R = np.linspace(1,15,396)
alpha = 0.5

#function for sine fourier transform
def sineFourier(inp, q, R, alpha):
    dR = R[2] - R[1]
    dq = q[2] - q[1]
    pi = 3.14159265359
    expterm = np.exp(-q**2*(alpha**2))
    dS = inp
    dPr = np.zeros((np.size(R,0),np.size(dS,1)))
    for i in range(0, np.size(R, 0)-1):
        whole_term = np.transpose(np.tile(q,(np.size(dS,1),1))) * dS * np.transpose(np.tile(np.sin(q*R[i-1]),(np.size(dS,1),1))) * np.transpose(np.tile(expterm,( np.size(dS,1),1))) * dq
        
        dPr[i,:] = R[i] / 2 / (pi**2)*sum(whole_term)
        
    return dPr
        
#do sine fourier transform
dPr = sineFourier(dS_exp, q, R, alpha)


#plot data
plt.figure()
cp = plt.contourf( q,t, dS_exp_t, levels=15)
plt.colorbar(cp)
plt.title('scattering')
plt.xlabel('q (Å^{-1})')
plt.ylabel('t (fs)')
plt.show()

plt.figure()
cp = plt.contourf(R, t, np.transpose(dPr), levels=15)
plt.colorbar(cp)
plt.title('scattering')
plt.xlabel('R (Å)')
plt.ylabel('t (fs)')
plt.show()
