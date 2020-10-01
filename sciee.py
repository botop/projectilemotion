#this is a program to compare multiple path of projections of objects at different velocities
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
adegrees,angles,tans,sins,coss,zl,tl,xmaxl,ymaxl=[],[],[],[],[],[],[],[],[]

u=int(input("enter the velocity of object.(in m/s). "))
inp=int(input("how many angles of projection you want to compare?"))
for i in range(1,inp+1):
    adegree=int(input(f"{i}. enter the angle of projection in degrees. "))
    adegrees.append(adegree)
    a=adegree*np.pi/180
    tana=np.tan(a)
    sina=np.sin(a)
    cosa=np.cos(a)
    
    z=2*u*u*cosa**2
    t=(2*u*sina/9.8)
    xmax=(t)*u*cosa
    ymax=(t/2)*u*sina-(9.8*(t/2)**2)/2
   
    angles.append(a)
    tans.append(tana)
    sins.append(sina)
    coss.append(cosa)
    zl.append(z)
    tl.append(t)
    xmaxl.append(xmax)
    ymaxl.append(ymax)



for j in range(inp):
    x=np.arange(0,xmaxl[j]+10,0.1)
    y = x*tans[j]-x*x*9.8/zl[j]

    plt.xlim(0,int(max(xmaxl)+100))
    plt.ylim(0,int(max(ymaxl)+100))
    plt.plot(x,y,label=f"{adegrees[j]} degree projection")
plt.xlabel("distance travelled by object")
plt.ylabel("height gained by object")

plt.legend()
plt.show()
