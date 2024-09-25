kelvin = [274.15,283.15,293.15,297.15,303.15,307.15,313.15,269.15,263.15,309.15]
C = [(x-273.15)for x in kelvin]
F = [round((x-273.15)*(9/5+32),2) for x in kelvin]
print("{:<9}{:<9}{:<10}{:<10}".format("N°","Kelvin","Celsius","Fahrenheint"))
for x in range(0,len(kelvin),1):
    print("{:<9}{:<9}{:<10}{:<10}".format(x+1,kelvin[x],C[x],F[x]))
