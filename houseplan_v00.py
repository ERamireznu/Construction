import pandas as pd       
import turtle  
def rects(lis00):
    height = 2.40
    skk = turtle.Turtle()
    skk.speed(0)
    skk.penup()
    for i, x in enumerate(lis00):        
        skk.goto(x[0],x[1])
        skk.pendown()
        for j in range(2):
            skk.forward(x[2]) 
            skk.left(90)
            skk.forward(x[3])
            skk.left(90)
                                    
        skk.penup()
        skk.goto(x[0]+int(x[2]*0.5),x[1]+int(x[3]*0.5))
        skk.pendown()
        skk.write(str(i+1))
        skk.penup()

    x_low = min([x[0] for x in lis00])        
    y_low = min([x[1] for x in lis00]) 
    #draw scale:
    skk.goto(x_low, y_low-120)
    skk.color('grey')
    skk.pendown()
    skk.right(90)
    skk.forward(5*esc)
    skk.left(90)
    skk.forward(100*esc)
    skk.left(90)
    skk.forward(5*esc)
    skk.penup()
    skk.goto(x_low-30*esc, y_low-135*esc)
    skk.pendown()    
    skk.write('1m')
    skk.hideturtle()
    Res = []

    #calc data:
    for i, x in enumerate(lis00):
        Area = (x[2]*0.01*x[3]*0.01)*((1/esc)**2)
        Perim = 2*(x[2]+x[3])*0.01*(1/esc)
        SupV = Perim*height
        Res.append((i+1, round(Area,2), round(Perim,2), round(SupV,2)))

    TotArea = sum([x[1] for x in Res])
    TotPerim = sum([x[2] for x in Res])
    TotSupV = sum([x[3] for x in Res])
    Res.append(('All', TotArea, TotPerim, TotSupV))
    df = pd.DataFrame(Res, columns = ('#','Area[m2]','Perim[mL]','SupV[m2]'))    
    print(df.to_string(index=False))
    turtle.done()

# Create a screen object
screen = turtle.Screen()

##subdivisions of a place: (x, y, long x, long y)
#ex.: depto lazo:
sbdvs = [(0,0,372,273),(380,0,198,138),(380,148,198,125),(292,273,80,57),(292,330,80,215),
         (380,283,198,126),(380,419,198,129),(0,281,284,250),(0,553,680,276),(680,553,97,265),
         (0,837,81,151),(81,837,63,93),(144,837,402,151),(546,837,134,158)]
global esc
esc = 1
sbdvs_esc = [(int(x[0]*esc),int(x[1]*esc),x[2]*esc,x[3]*esc) for x in sbdvs]        

desp = [-500,-500]
sbdvs2 = [(x[0]+desp[0],x[1]+desp[0],x[2],x[3])for x in sbdvs]

#canvas size:
cnv_wi = max([x[0]+x[2] for x in sbdvs])+300
cnv_he = max([x[1]+x[3] for x in sbdvs])+300
screen.screensize(cnv_wi, cnv_he)
#set coordinates:
screen.setworldcoordinates(-150, -150, cnv_wi, cnv_he)
print(f"Canvas (width, height): {cnv_wi}, {cnv_he}")

rects(sbdvs)

