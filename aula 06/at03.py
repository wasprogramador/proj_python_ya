kg = [1,5,10,20,30,40,70,80,100,200]
T = [(x*10)for x in kg]
L = [(x*1.6) for x in kg]
M = [(x*3.71) for x in kg]
Mer = [(x*3.7) for x in kg]
print("{:<10}{:<10}{:<10}{:<10}{:<10}")
for x in range(0,len(kg),1):
    print("{:<10}{:<10}{:<10}{:<10}{:<10}".format(x+1,T[x],L[x],M[x],Mer[x]))