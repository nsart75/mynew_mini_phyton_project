import numpy as np 
import matplotlib.pyplot as plt
def plots(X , Y ):
    return np.sin(np.sqrt(X**2 + Y**2))
x = np.linspace(-6 , 6 , 30)
y = np.linspace(-6 , 6 , 30)
x , y = np.meshgrid(x , y)
z = plots(x , y )
fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.contour3D(x , y , z , 50 , cmap = 'binary')
plt.show()
