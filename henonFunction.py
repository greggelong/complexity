import matplotlib.pyplot as plt


def henon(a=1.4,b=0.3,x=0.2,y=0.2):
    global lx,ly

    for i in range(1,3000):
        xnew = 1+y-a*x**2
        ynew = b*x
        #print(i,xnew,ynew)
        lx.append(xnew)
        ly.append(ynew)
        
        x =xnew
        y =ynew
    
    
# initalize lists for plotting
lx = []
ly = []

henon(1.4,0.3,0.2,0.2) #henon(a,b,x,y)


plt.scatter(lx,ly, marker=".", alpha=0.2)
plt.show()
