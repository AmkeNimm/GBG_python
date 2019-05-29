
import matplotlib.pyplot as plt
import numpy as np
import time
import pandas as pn
import scipy.io as spi
import matlab.engine as mle

filepath = ['/home/amke/Documents/projects/modelling-package/experiment-SACLA/SACLA2015_elisa/DATA']    #alternative: ['./']
filename = ['H20_long.mat']


eng = mle.start_matlab()
expData = eng.load('H20_long.mat')
qmat = eng.getfield(expData, 'q')
tmat = eng.getfield(expData, 'Delays')
dS_expmat = eng.getfield(expData, 'AllTTDelay')

q = np.asarray(qmat)
t = np.asarray(tmat)
dS_exp = np.asarray(dS_expmat)
dS_exp_t = np.transpose(dS_exp)

plt.figure()
cp = plt.contourf(q[0], t[0], dS_exp_t, levels=15, vmin=-0.7, vmax=0.7)
plt.colorbar(cp)
plt.title('scattering')
plt.xlabel('q (Å^{-1})')
plt.ylabel('t (fs)')
plt.show()
