'''
Created on 2018/11/30

@author: Taichi
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

N=500#粒子数
Lx=10.0#x軸の長さ
Ly=20.0#y軸の長さ
Lz=20.0#z軸の長さ
R=1.0#平均粒子径
R_sigma=0.4#粒子の標準偏差(対数正規分布)

#2粒子間の距離を計算
def distance3D(x1,y1,z1,x2,y2,z2):
    return np.sqrt(pow((x1-x2),2)+pow((y1-y2),2)+pow((z1-z2),2))

def distance2D(x1,y1,x2,y2):
    return np.sqrt(pow((x1-x2),2)+pow((y1-y2),2))
#粒子のPoisiton
def random_position():
    return np.random.rand(1)
#粒子の距離
def radius():
    #return R #単分散粒子
    #return R*(np.random.rand(1))#標準正規分布(平均0, 標準偏差1)
    return (np.random.normal(R,R_sigma,1))#標準正規分布(平均R,標準偏差)
    #return (np.random.lognormal(R,R_sigma, 1))#対数正規分布*修正必要
#粒子を表すクラス。インスタンス変数として粒子の位置と半径(x,y,z,r)を持つ
#class P_3D:
#    def __init__(self,xx,yy,zz,rr):
#        self.x = xx
#        self.y = yy
#        self.z = zz
#        self.r = rr
class P_2D:
    def __init__(self,xx,yy,rr):
        self.x = xx
        self.y = yy
        self.r = rr

#粒子の配列
List_particle=[]
#粒子を作る
for i in range(N*1000):
    print(i)
    xp=Lx*random_position()[0]
    yp=Ly*random_position()[0]
    #zp=Lz*random_position()[0]
    rp=radius()
    #position=P_3D(xp,yp,zp,rp)#3次元
    position=P_2D(xp,yp,rp)#2次元
    if((xp-rp)<0):
        pass
    else:
        if((xp+rp)>Lx):
            pass
        else:
            if((yp-rp)<0):
                pass
            else:
                if((yp+rp)>Ly):
                    pass
                else:
                    #2次元の場合
                    if(len(List_particle)==0):
                        List_particle=List_particle+[position]
                    else:
                        okFlag=True
                        for ii in range(len(List_particle)):
                            if((distance2D(xp, yp, List_particle[ii].x, List_particle[ii].y))<(rp+List_particle[ii].r)):
                                okFlag=False
                                break
                        if(okFlag==True):
                            List_particle=List_particle+[position]
                        else:
                            pass
                        
                    
                    #3次元の場合
                    #if((zp-rp)<0):3次元の場合
                    #    pass
                    #else:
                    #    if((zp+rp)>Lz):3次元の場合
                    #        pass
                    #    else:
                    #        if(len(List_particle)==0):
                    #            List_particle=List_particle.append(position)
                    #        else:
                    #            okFlag=True
                    #            for ii in range(len(List_particle)):
                    #                if((distance3D(xp, yp, zp,List_particle[ii].x, List_particle.y,List_particle.z))>(rp+List_particle.r)):
                    #                    okFlag=False
                    #                    break
                    #                if(okFlag==True):
                    #                    List_particle=List_particle+[position]
                    #                else:
                    #                    pass
    if(len(List_particle)>=N):
        break


fig = plt.figure()
ax = plt.axes()
circle=[]
#粒子を使う
for i in range(N):
    c = patches.Circle(xy=(List_particle[i].x, List_particle[i].y), radius=List_particle[i].r, fc='r', ec='r')
    ax.add_patch(c)

ax.plot()

ax.set_xlim([0, Lx])
ax.set_ylim([0, Ly])
#plt.axes().set_aspect('equal', 'datalim')
ratio=Lx/Ly
aspect = (1/ratio) *(ax.get_xlim()[1] - ax.get_xlim()[0]) / (ax.get_ylim()[1] - ax.get_ylim()[0])
ax.set_aspect(aspect)
plt.grid()
plt.show()
        