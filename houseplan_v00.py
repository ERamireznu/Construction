import pandas as pd       
import turtle 
def dimens(tur0, sta_coords, col, st_dire, dimens_3, wri_coords, words):
    #(instance, (coords start x,y), color, start_direc, (dim1, dim2, dim3),
    #(coords write x,y),(writing, Tr/Fa, le/ri, font))
    #standard mode
    stx,sty = sta_coords[0],sta_coords[1]
    dim1, dim2, dim3 = dimens_3[0],dimens_3[1],dimens_3[2]
    wrx,wry = wri_coords[0],wri_coords[1]
    wor0,wor1,wor2,wor3 = words[0],words[1],words[2],words[3]
    set_head = {'east':0, 'north':90, 'west':180, 'south':270}
    tur0.setheading(set_head[st_dire.lower()])  
    
    tur0.goto(stx,sty)
    tur0.color(col)
    tur0.pendown()
    tur0.forward(dim1)
    tur0.left(90)
    tur0.forward(dim2)
    tur0.left(90)
    tur0.forward(dim3)
    tur0.penup()
    tur0.goto(wrx,wry)
    tur0.pendown()    
    tur0.write(wor0,wor1,wor2,wor3)
    tur0.penup()

def rects(lis00, hei=2.40, out_dims = True, intern_dims = True, show_rooms = True, calc_data = True):
    height = hei  #(m)
    skk = turtle.Turtle()
    skk.speed(0)
    skk.penup()
    for i, x in enumerate(lis00):        
        skk.goto(x[0],x[1])
        skk.pendown()
        skk.color('black')
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
    draw_wi = max([x[0]+x[2] for x in lis00])
    draw_he = max([x[1]+x[3] for x in lis00])
    if dim_max_horiz:   #draw max measures (horizontal)
        dimens(skk,(x_low, y_low-70),'blue','south',(5,draw_wi,5),(int(draw_wi*0.5), y_low-72),
               (f"{round(draw_wi*0.01, 2)}m", False,'left',('Arial',7,'normal')))
    if dim_max_vert:    #draw max measures (vertical)
        dimens(skk,(x_low-70, y_low),'blue','east',(5,draw_he,5),(x_low-130, int(draw_he*0.5)),
           (f"{round(draw_he*0.01, 2)}m", False,'left',('Arial',7,'normal')))    
    if draw_scale:
        dimens(skk,(x_low, y_low-120),'grey','south',(5,100,5),(x_low-30, y_low-135),
           ('1m', False,'left',('Arial',7,'normal')))
    
    skk.hideturtle()
    if calc data:
        Res = []
        for i, x in enumerate(lis00):
            Area = round((x[2]*0.01*x[3]*0.01), 2)
            Perim = round(2*(x[2]+x[3])*0.01, 1)
            SupV = round(Perim*height, 2)
            Res.append((i+1, x[2]/100, x[3]/100, Area, Perim, SupV))
        TotArea = round(sum([x[3] for x in Res]), 2)
        TotPerim = round(sum([x[4] for x in Res]), 1)
        TotSupV = round(sum([x[5] for x in Res]), 2)
        Res.append(('All', '-','-',TotArea, TotPerim, TotSupV))
        df = pd.DataFrame(Res, columns = ('#','Side 1[m]','Side 2[m]','Area[m2]','Perim[mL]','SupV[m2]'))    
        print(df.to_string(index=False))
    turtle.done()

#-----------------------------------------------------
##subdivisions of a place: (x, y, long x, long y)
#example: depto lazo:
sbdvs = [(0,0,372,273),(380,0,198,138),(380,148,198,125),(292,273,80,57),(292,330,80,223),
         (380,283,198,126),(380,419,198,129),(0,281,284,250),(0,553,680,276),(680,553,97,265),
         (0,837,81,151),(81,837,63,93),(144,837,402,151),(546,829,134,159)]

#-----------------------------------------------------
# Create a screen object
screen = turtle.Screen()
#canvas size:
cnv_wi = max([x[0]+x[2] for x in sbdvs])+300
cnv_he = max([x[1]+x[3] for x in sbdvs])+300
screen.screensize(cnv_wi, cnv_he)
#set coordinates:
screen.setworldcoordinates(-150, -150, cnv_wi, cnv_he)

rects(sbdvs)

