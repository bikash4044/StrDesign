import numpy as np
import math
'''
This programs aims at design of drainage sturcture for subsurface pipe drainage system.
Use this program specifically when you need to find the spacing between the drainage pipes
'''

print('''
Consider,
W = depth of drainbase from ground surface(m)
D = depth of impervious layer from drainbase(m)
H = depth of water table from from ground surface(m)
h = height of water table from drain base(m)
    => W = h+H
k1 = hydraulic conductivity of soil above drainbase(m/day)
k2 = hydraulic conductivity of soil below drainbase(m/day)
    => in some cases, k1=k2 might happen
q = design discharge from a pipe(m/day)
''')

print("\n\n\n")
D = input("Enter depth(m) of impervious layer form  drainbase: ")
r = input("Enter the radius of the drain pipe: ")
u=r*math.pi
k1 = input("Enter hydraulic conductivity(m/day) of soil above drain base: ")
k2 = input("Enter hydraulic conductivity(m/day) of soil below drain base: ")
h = input("Enter height of water table from drain base: ")
q = input("Enter discharge(m/day) through the pipe: ")

while(True):
    L = input("Enter length spacing(m) to start with: ")
    L2=0
    d=0
    if(D>L/4):
        d = D/(((8*D*math.log(D/u))/(L*math.pi))+1)
    else:
        d = (np.pi*L)/(8*math.log(L/u))

    L2 = math.sqrt((8*k2*d*h/q)+(4*k1*h*h/q))
    print(f"For L={L}m, the value we get L={L2}m")
    if(abs(L-L2)<=1):
        break
    else:
        print(f"Improve the drainage spacing. difference is {abs(L-L2)}m")

print(f"You may proceed with the design. Difference is {abs(L-L2)}m")
