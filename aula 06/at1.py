M = [10,20,30,40,50,60,70,80,90,100]
pol = [(x*39.37) for x in M]
pes = [(x/0.3048) for x in M]
jar = [(x*1.094) for x in M]
m_nal = [(x/1852) for x in M]
print("{:<9}{:<16}{:<20}{:<20}{:<20}{:<20}".format("N°","M","pol","pes","jar","m_nal"))
for x in range(0,len(M),1):
    print("{:<9}{:<16}{:<20}{:<20}{:<20}{:<20}".format(x+1,M[x],pol[x],pes[x],jar[x],m_nal[x]))

  