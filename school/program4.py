#Create a tuple of t1 integers and display it.
#Generate n terms of binocci series..


#---imports----
import statistics as stat



def createTuple(n):
    T = ()
    for  i in  range(0,n):
        x = int(input("Enter Number: "))
        T += (x,)
    return T

def fibinoci(n):
    T2 = (0,1)
    for i in range(0,n-2):
        x = T2[i] + T2[i+1]
        T2 += (x,)

    return T2

I = int(input("Enter Length of tuple: "))
T2 = fibinoci(I)
T1 = createTuple(I)
T3 = T1 + T2

print("Tuple 1: ",T1)
print("Tuple 2: ",T2)

###T3 Stats

mean = stat.mean(T3)
mode = stat.mode(T3)
median =  stat.median(T3)

print("Mean: ",mean)
print("Mode: ",mode)
print("Median: ",median)





