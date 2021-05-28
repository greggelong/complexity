
import matplotlib.pyplot as plt

# Suppose we are using the logistic equation to describe the population of rabbits on an island.
# How would we interpret a population of ?
# the population is at 70 percent of the annihilation population

def popfun(r,x):
    # logistic map equation from feldman module 3 dynamic systems and chaos
    return r*x*(1-x)


def plotit(x, y, z, w):   # x is turns, y is running total, z is total per turn
    #plt.plot(x,y,color='green',linestyle='dashed',marker='o',markerfacecolor='blue')

    #plt.plot(x , y)
    #plt.axis(0,max(x),0,max(y))
    global r
   
   
    figure, axis = plt.subplots(2)
  
    # For average
    axis[0].plot(x, y, marker=".")
    axis[0].set_ylim([0,1]) # make sure the y axis is the same
    axis[0].set_title("logistic plot1 with r = %5.3f and seed = %5.3f" %(r,y[0]))
      
    # For total over all
    axis[1].plot(z, w, marker=".")
    axis[1].set_ylim([0,1]) # make sure the y axis is the same
    axis[1].set_title("logistic plot2 with r= %5.3f and seed = %5.3f" %(r,w[0]))
    
    plt.show()

r= 3.77  #set r value 2-4
x1=0.2  # initial seed
x2=0.4  # initalseed
pltx1=[0]
pltx2=[0]
plty1=[x1] # list 1 to be plotted alog the y axis
plty2 =[x2] # list 2 to be plotted along the y axis
print(0,x1,x2) #seed1
for i in range(1,100):
    newx1 = popfun(r,x1)
    newx2 = popfun(r,x2)
    pltx1.append(i)
    plty1.append(x1)
    pltx2.append(i)
    plty2.append(x2)
    print(i,newx1, i,newx2)
    x1 = newx1
    x2 = newx2
    
    
plotit(pltx1,plty1,pltx2,plty2)    
    
 
