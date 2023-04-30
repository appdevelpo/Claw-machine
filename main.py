from vpython import box,sphere,vec,quad,vertex,radians,compound,cylinder,rate 
from numpy import sin,arcsin,pi,arange,linspace
compo = box(pos = vec(0,0,0),size=vec(5,1,0.6))
compo1 = box(pos=vec(3,0,-0.8),size=vec(2,1,0.6))
compo1.rotate (angle = radians(45),axis=vec(0,1,0))
claw1 = compound([compo,compo1],pos=vec(4,0,0),)
claw1.rotate(angle = radians(90),axis=vec(0,1,0))
claw2 = claw1.clone(pos=(vec(-2,-2*3**0.5,0)))
claw2.rotate(angle=radians(240),axis=vec(0,0,1))
claw3 = claw2.clone(pos=(vec(-2,2*3**0.5,0)))
claw3.rotate(angle=radians(240),axis=vec(0,0,1))
claw1.rotate(angle=radians(-45),axis=vec(0,1,0))
claw3.rotate(angle=radians(45),axis=vec(3**.5,1 ,0))
claw2.rotate(angle=radians(45),axis=vec(-3**.5,1,0))
q = sphere(pos = vec(0,0,2),radius=3)
rod = cylinder(pos=vec(0,0,1.5),axis= vec(0,0,8),radius = 3)
claw= compound([claw1,claw2,claw3,rod,q],pos =vec(0,0,0))
# rod0 = cylinder(pos=vec())
# cube = box(pos= vec(-1.5,-1.5,9.5),size = vec(3,3,3))
for t in arange(0,90,.1):
    claw1.rotate(angle=radians(5),axis = vec(0,1,0),origin = vec(0,0,13))
    # claw1.pos=vec(t,0,0)
    rate(100)

# =============================================================================
# p = []
# # for i in range(2):
# #     for j in range(2):
# #         for k in range(2):
# #             p.append(pos = vec(i,j,k))
# # p = [vertex(pos = vec(i,j,k)) for i in range(2) for j in range(2) for k in range(2)]
# o1 = [[0,0,0],[0,4,0],[1,4,0],[1,0,0]]
# def coor_to_vec(coor):
#     return [vertex(pos = vec(coor[i][0],coor[i][1],coor[i][2])) for i in range(len(coor))]
# claw = quad(vs = p)
# s = quad(vs = coor_to_vec(o1))
# =============================================================================
#%%
from vpython import box,sphere,vec,quad,vertex,radians,compound,cylinder,rate 
from numpy import sin,arcsin,pi,arange,linspace,exp,cos
from time import time
import matplotlib.pyplot as plt 
import keyboard
compo = box(pos = vec(0,0,0),size=vec(5,1,0.6))
compo1 = box(pos=vec(3,0,-0.8),size=vec(2,1,0.6))
compo1.rotate (angle = radians(45),axis=vec(0,1,0))
claw1 = compound([compo,compo1],pos=vec(4,0,0),)
claw1.rotate(angle = radians(90),axis=vec(0,1,0))
claw2 = claw1.clone(pos=(vec(-2,-2*3**0.5,0)))
claw2.rotate(angle=radians(240),axis=vec(0,0,1))
claw3 = claw2.clone(pos=(vec(-2,2*3**0.5,0)))
claw3.rotate(angle=radians(240),axis=vec(0,0,1))
claw1.rotate(angle=radians(-45),axis=vec(0,1,0))
claw3.rotate(angle=radians(45),axis=vec(3**.5,1 ,0))
claw2.rotate(angle=radians(45),axis=vec(-3**.5,1,0))
q = sphere(pos = vec(0,0,2),radius=3)
rod = cylinder(pos=vec(0,0,1.5),axis= vec(0,0,8),radius = 3)
claw= compound([claw1,claw2,claw3,rod,q],pos =vec(0,0,0))
#=============================================================================#
g = 9.8 
b = 0.23
theta0 = 0
theta1 = 0
t = 0
v = 0
v_y = 0
m = .3
dt = .1
r = 13
x = r*sin(theta0)
y = r*sin(theta1)
print(x,y)
X = []
Y= []
F_x,F_y = 0,0
prev_theta0 = 0
prev_theta1 = 0
prev_milis = 0 
tau = 1
j,k,l,p =0,0,0,0
x_claw,y_claw,vx_claw,vy_claw = 0,0,0,0
T = 2000
force_list = [(3.5/tau)*exp(-(j/tau)) for j in arange(0,200,.1)]
swi = 0
while t<T:
    
    a = (-g*x/r-b*v/m+F_x)
    v += a*dt
    x += v*dt
    theta0 = x/r
    a_y = -g*y/r-b*v_y/m+F_y
    v_y += a_y*dt
    y += v_y*dt
    theta1 = y/r
    claw.rotate(angle=(theta0- prev_theta0),axis = vec(0,1,0),origin = vec(0,0,13))
    claw.rotate(angle=-(theta1- prev_theta1),axis = vec(1,0,0),origin = vec(0,0,13))
    rate(100)
    Y.append(y)
    X.append(x)
    t += dt
    prev_theta0=theta0  
    prev_theta1 = theta1 
    claw.pos = vec(x_claw,y_claw,0)
    cur_milis = time()*1000
    if cur_milis - prev_milis < 200:
        # F_x,F_y = 0,0
        vx_claw,vy_claw = 0,0
        continue
    if keyboard.is_pressed("space") or swi==1:
        F_x,F_y = 0,0
        swi = 1
        r +=.2
        claw.pos = vec(x_claw,y_claw,-(r-13)*cos(theta0))
        b = 0.01
        if r > 1000:
            break
        continue
    elif keyboard.is_pressed("up"):
        if j==0:
            k,l,p = 0,0,0
        
        # F_y = 3
        F_x = 0
        F_y = force_list[j]
        j += 1
        # print(j)
        # print("up")
    elif keyboard.is_pressed("down"):
        if k==0:
            j,l,p = 0,0,0
        F_y = -force_list[k]
        # F_y =-3
        # print(F_y)
        F_x = 0
        k+=1
    elif keyboard.is_pressed("left"):
        if l==0:
            j,k,p = 0,0,0
        F_y = 0
        F_x = -force_list[l]
        l+=1
    elif keyboard.is_pressed("right"):
        if p == 0:
            j,k,l = 0,0,0
        F_y = 0
        F_x = force_list[p]
        p+=1
    else:
        F_y = 0
        F_x = 0
    vx_claw += F_x/m*dt*2
    x_claw += vx_claw*dt*2
    vy_claw += F_y/m*dt*2
    y_claw += vy_claw*dt*2
    
    
    prev_milis = cur_milis
