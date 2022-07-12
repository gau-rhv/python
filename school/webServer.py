import py_compile
import math
import zer0x9

numbers = [x * 5 for x in range(2000, 2100)]
results = []

print('[======Menu=====] \n[1]Pattern one \n[2]Pattern two \n[3]Pattern three \n[4]Pattern four \n[5]Pattern five \n[6]Exit')
opt = int(input("Choose your Pattern: "))
if opt == 1:
    n = ()
    print(zer0x9.p1(n))

elif opt == 2:
    n = ()
    print(zer0x9.p1(n))

elif opt == 3:
    n = ()
    print(zer0x9.p3(n))

elif opt ==4:
    n = ()
    print(zer0x9.p4)

elif opt ==5:
    n = ()
    print(zer0x9.dph(n))

elif opt ==9:
    n = ()
    print(zer0x9.test(n))

elif opt == 6:
    print("Programme Ending :D")
    zer0x9.progress_bar(0, len(numbers))
    for i, x in enumerate(numbers):
        results.append(math.factorial(x))
        zer0x9.progress_bar(i + 1, len(numbers))
    exit
    

    


