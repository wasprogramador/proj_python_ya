class Conversao:
    def velocidade():
        kmh = [75.4,30.6,120,32.8,20.8]
        mph = [round(x/1.61,2) for x in kmh]
        return mph 
    
    def temperatura():
        celsius = [45,30,12.5,32.6,50]
        fahrenheit = [round((x*1.8)+32,2) for x in celsius]
        x = 0
        while(x<6):
            print(celsius[x],"celsius são", fahrenheit[x])
            x += 1 
    def altura():
        metros = [5,10,20,35,70]
        pes = [round(x/0.3048,2) for x in metros]
        x = 0
        while(x<4):
            print(metros[x],"em pés são", pes[x])
            x += 1
    
    def idade():
        anos = [12,29,45,2,5,18]
        meses = [round(x*12,2) for x in anos]
        x = 0
        while(x<5):
            print(anos[x],"anos são", meses[x])
            x += 1 