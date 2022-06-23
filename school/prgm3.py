#Program 3 : List Processing
#A program to accept a list of values to a L and pass to two  user defined function : To perform following functio:
#1) Swap 1st half of elements to second half.
#2)swap Adjacent elements.

def swapHalf(L):
    cHalf = int(len(L)/2)
    L[:cHalf],L[cHalf::1] = L[cHalf::1] ,L[:cHalf]
    return L

def swapAdj(L):
    for i in range(0,len(L),2):
        L[i],L[i+1] = L[i+1] ,L[i]
    return L
    
while True:
    print("-----------------Menu----------------")
    print("1) Swap first Half with second Half of List")
    print("2) Swap with Adjacent elements of List")
    opt = int(input(">> Enter your Option: "))
    
    if opt == 1:
        l = list(eval(input(">> Enter List: ")))
        print("Before Swap: ",l)
        L = swapHalf(l)
        print("After Swap: ",L)
    elif opt == 2:
        l = list(eval(input(">> Enter List {Need Even no.of Elements}: ")))
        print("Before Swap: ",l)
        L = swapAdj(l)
        print("After Swap: ",L)
    else:
        print("...:Thank You:...")
        break


    
