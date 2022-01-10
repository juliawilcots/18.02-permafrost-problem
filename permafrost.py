import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# set up variables
day = 24*60*60 # in seconds

z = np.linspace(0,20,100) # meters
# at first, use alpha = 0.2e-6, between soil and ice
alpha = 0.2e-6
omega = 2*np.pi/3.154e+7 # 365 days, 1 year
zw = np.sqrt(2*alpha/omega)
A = 5
year = 3.154e+7
time = np.arange(0,3.154e+7,24*60*60)

# Calculate temperatures at depth
Temps = np.zeros([len(z),len(time)])
for i,t in enumerate(time):
    T = 16*np.exp(-z/zw)*np.sin(omega * t -z/zw + 3*np.pi/2) -10
    Temps[:,i] = T

# Produce contour plot
plt.contourf(time/(60*60*24),z,Temps,30,cmap='RdBu',norm=mpl.colors.Normalize(vmin=-20, vmax=20))
plt.ylim([20,0])
c = plt.colorbar(label='Temperature ($^\circ$C)')
plt.xlabel('Day of year')
plt.ylabel('Depth (m)')
plt.title('alpha = %.2e' %alpha)
plt.savefig('contour_alpha_2e-7.png')
plt.show()


# Check contour plot with alpha = 1.0e-6 (ice):
alpha = 1.0e-6 # for last problem
zw = np.sqrt(2*alpha/omega)
# Calculate temperatures at depth
Temps = np.zeros([len(z),len(time)])
for i,t in enumerate(time):
    T = 16*np.exp(-z/zw)*np.sin(omega * t -z/zw + 3*np.pi/2) -10
    Temps[:,i] = T

# Produce contour plot
plt.contourf(time/(60*60*24),z,Temps,30,cmap='RdBu',norm=mpl.colors.Normalize(vmin=-20, vmax=20))
plt.ylim([20,0])
c = plt.colorbar(label='Temperature ($^\circ$C)')
plt.xlabel('Day of year')
plt.ylabel('Depth (m)')
plt.title('alpha = %.2e' %alpha)
plt.savefig('contour_alpha_1e-6.png')
plt.show()


# Change directory to save fig in:
#plt.savefig('../0FALL2021/contour.png')

####### Alaskan cities: #######
Tbarrow_midsummer = 16*np.sin(omega*(year/2)+3*np.pi/2)-10
print(Tbarrow_midsummer)
Tbettles_midsummer = 19*np.sin(omega*(year/2)+3*np.pi/2) - 3
print(Tbettles_midsummer)

zp_range = np.linspace(start = zw*(omega*time - np.pi/2), stop = zw*(omega*time + np.pi/2), num = 10)

months = np.arange(0,12) * (3.154e+7/12)

barrowF = np.array([-13.4, -14.2, -12.7, 1.8, 21.1, 35.6, 40.9, 39.0, 32.1, 17.2, 0.7, -7.8]) # deg F
barrow = (barrowF - 32) * (5/9)

# BEST FIT
Tbarrow = 16*np.sin(omega*time-1.7) -10

# FOR PROBLEM SET:
Tbarrow_use = 16*np.sin(omega*time+3*np.pi/2)-10

bettlesF = np.array([-10.0, -5.0, 4.4, 23.3, 44.4, 58.5, 59.7, 52.5, 40.6, 18.9, -1.0, -5.7]) # deg F
bettles = (bettlesF - 32) * (5/9)

# BEST FIT
Tbettles = 19*np.sin(omega*time-1.5) - 3
Tbettles_use = 19*np.sin(omega*time+3*np.pi/2) - 3

Tavg_barrow = np.mean(Tbarrow)
Tavg_bettles = np.mean(Tbettles)

fig, ax = plt.subplots(1,2,figsize=(12,4),sharey=True)

ax[0].plot(time/(24*60*60), Tbettles, c='k', label='Bettles, AK')
ax[0].set_title('Bettles, AK (67ºN)',fontsize=14)
ax[0].axhline(Tavg_bettles,label='avg annual temp.',color='r',ls='--')
ax[0].text(0,Tavg_bettles-2,'avg. annual temp.', color='r',fontsize=12)
ax[0].set_xlabel('day of year (starting mid-spring)', fontsize=14)
ax[0].set_ylabel('temp [deg C]', fontsize=14)
for label in (ax[0].get_xticklabels() + ax[0].get_yticklabels()):
    label.set_fontsize(14)
ax[0].grid(axis='y')


ax[1].plot(time/(24*60*60), Tbarrow, c='k', label='Utqiagvik, AK')
ax[1].set_title('Utqiagvik, AK (71ºN)',fontsize=14)
ax[1].axhline(Tavg_barrow,label='avg annual temp.',color='r',ls='--')
ax[1].text(0,Tavg_barrow-2,'avg. annual temp.', color='r',fontsize=12)
ax[1].set_xlabel('day of year (starting mid-spring)', fontsize=14)
for label in (ax[1].get_xticklabels() + ax[1].get_yticklabels()):
    label.set_fontsize(14)
ax[1].grid(axis='y')

plt.show()
