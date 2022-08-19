from scipy import interpolate
import numpy as np
from matplotlib import pyplot as plt

# サンプルデータ作成
# x = np.linspace(0, 10, 11)
# xx = np.linspace(0, 10, 51)
# y = np.sin(x)
# yy = np.sin(xx)
# print('t', x)
# print('x', x)
# print('y', y)
# print('yy', yy)

# plt.figure(figsize=(12, 9))
# plt.plot(x, y, "o", label="x")
# # plt.figure(figsize=(12, 9))
# # plt.plot(x, yy, "o", label="x")
# plt.legend()
# plt.show()


def spline_interp(x, y, point):
    f = interpolate.interp1d(x, y,kind="cubic")
    X = np.linspace(x[0],x[-1],num=point,endpoint=True)
    Y = f(X)
    return X,Y

def spline_akama(x,y,point):
    f = interpolate.Akima1DInterpolator(x, y)
    X = np.linspace(x[0],x[-1],num=point,endpoint=True)
    Y = f(X)
    return X,Y

def spline_splprep(x,y,point,deg):
    tck,u = interpolate.splprep([x,y],k=deg,s=0)
    u = np.linspace(0,1,num=point,endpoint=True)
    spline = interpolate.splev(u,tck)
    return spline[0],spline[1]


x = [-5, 0, 1, 3, 4, 6]
y = [-4, 2, -2, -4, 0, 4]

a1, b1 = spline_interp(x, y, 100)
a2, b2 = spline_akama(x, y, 100)
a3, b3 = spline_splprep(x, y, 100, 3)


plt.plot(x, y, 'ro', label="controlpoint")
plt.plot(a1, b1, label="interp1d")
plt.plot(a2, b2, label="Akima1DInterpolator")
plt.plot(a3, b3, label="splprep")
plt.legend(loc='lower right')

plt.show()
