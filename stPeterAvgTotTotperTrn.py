import matplotlib.pyplot as plt
import random
import math

turns = [0]
totalTurn = [0]
total = [0]
runAvg = [0]
coin = ["H","T"]
counter = 0 # global counter which will be appended into turns

def plotit(x, y, z, w):   # x is turns, y is running total, z is total per turn
    #plt.plot(x,y,color='green',linestyle='dashed',marker='o',markerfacecolor='blue')

    #plt.plot(x , y)
   # plt.axis(0,max(x),0,max(y))
   
   
    figure, axis = plt.subplots(3)
  
    # For average
    axis[0].plot(x, y)
    axis[0].set_title("average over turns")
      
    # For total over all
    axis[1].plot(x, w)
    axis[1].set_title("total over all turns")
    
    
    # For total each turn
    axis[2].plot(x, z)
    axis[2].set_title("total over each turn")
    plt.show()



def taketurn():
    global turns, total, totalTurn, coin, counter
    counter = counter + 1
    turns.append(counter)
    turnTotal =2
    show = ""
    
    # flip a coin if heads get 2 dollars if tails turn total mult by 2
    
    while not show == "H":
        
        show = random.choice(coin)
        #print(show, turnTotal)
        if show == "H":
            
            newTotal = total[-1] + turnTotal
            total.append(newTotal)
            totalTurn.append(turnTotal)
            avg = total[-1]/ counter  # average is total for that turn divided by num of turns
            runAvg.append(avg)
           # print("you win ", turnTotal, counter, " your total is", total[-1], "avg ",runAvg[-1])
        else:
            turnTotal = turnTotal * 2
            

for i in range(10000):
    taketurn()
    
    
#print(turns,total)
plotit(turns, runAvg, totalTurn, total)
print(max(totalTurn), math.log(max(totalTurn),2))
    