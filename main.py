import netCDF4 as nc
import numpy as np
import scipy.io as sio

# a wrfout file
fn = '/home/chang-hsin/plumes/nbl.air.h2.5/wrfout/wrfout_d01_0001-01-01_00:35:00'
# import the file to python
ds = nc.Dataset(fn)

# print(ds)

# print(ds.variables)

# print the information
print(ds.variables['U'])

# u1=ds['U'][:]
# print(u1.shape)
u1 = ds['U'][0:2, 0, 0, 0]
print(u1)

# type(u1)
# print(u1[1:5,1,1,1])

# arr = np.arrange(9) # 1d array of 9 numbers
# arr = arr.reshape((3, 3))  # 2d array of 3x3

# sio.savemat('/home/chang-hsin/plumes/temp.mat', mdict={'u1': u1})
