from tkinter import *
from numpy import array

def Replay():
    global conteneur,message
    try:
        conteneur.delete("all")
        conteneur.pack_forget()  
        message.configure(text="Have a nice Game !! ")
        initTheGame()
        rePlay.configure(text="Replay")
    except:
        initTheGame()
        rePlay.configure(text="Replay")
def NewGame():
    
    global someoneWin, whoWin, PlayTime,FristPlayer,FristPlayerScore
    global FristPlayer1, FristPlayerScore1, SecondPlayer, SecondPlayerScore1, SecondPlayer1,SecondPlayerScore
    global score, playerNow, xList, oList
    someoneWin=False
    whoWin=""
    PlayTime=0
    FristPlayer="x"
    FristPlayerScore=0
    
    FristPlayer1.set("player 1 :"+FristPlayer+" : ")
    FristPlayerScore1.set(str(FristPlayerScore))
    
    SecondPlayer="o"
    SecondPlayerScore=0

    SecondPlayer1.set("player 2 :"+SecondPlayer+" : ")
    SecondPlayerScore1.set(str(SecondPlayerScore))

    score={"FristPlayer":{"role":FristPlayer,"score":FristPlayerScore}, "SecondPlayer":{"role":SecondPlayer,"score":SecondPlayerScore}}
    playerNow="o"
    
    xList=[]
    oList=[]
    Replay()
    
def createImage(x, y):
    global playerNow, someoneWin, whoWin, PlayTime, resized_x_img, resized_o_img, resized_im
    if not someoneWin and PlayTime == 9:
        message.configure(text=whoWin + " Null !!")
    elif not someoneWin and PlayTime < 9:
        if playerNow == "x":
            conteneur.create_image(x - 50, y - 50, image=resized_x_img, anchor='nw')
        else:
            conteneur.create_image(x - 57, y - 60, image=resized_o_img, anchor='nw')
    else:
        message.configure(text=whoWin + " Won !!")
        #conteneur.create_image(200, 200, image=resized_im, anchor='nw')


def fixPointer(x,y):
    if x < 126 and y <126:
        return (64,64,"00")
    if x < 126 and y > 133 and  y < 268:
        return (64,200,"01")
    if x < 126 and y > 270:
        return (64,335,"02")
    
    if x > 126 and x < 270 and y <126:
        return (200,64,"10")
    if x > 270  and y <126:
        return (330,64,"20")
    #ddd
    if x > 126 and x<270 and y > 270:
        return (200,330,"12")
    if x > 270  and y >270:
        return (330,330, "22")
    if x > 126 and x < 270 and y >126 and y <270:
        return (200,200,"11")

    if x > 270  and y >126:
        return (330,200,"21")

def serachDispo(x,y):
    global arrDetails
    for elem in arrDetails :
        if elem["x"]==x and elem["y"]==y:
            return  False
    return True
def miniTest(l,x,y,z):
    s=0
    for i in l:
        if i==str(x):
            s+=1
        if i==str(y):
            s+=1
        if i==str(z):
            s+=1
    return s==3

def checkLists():
    global xList, oList
    if miniTest(xList,'00','11','22'):
        conteneur.create_line(50,50,350,350,fill="red",width=3)
        #print('1')
        #print('x win')
        return True
    if miniTest(xList,'20','11','02'):
        conteneur.create_line(350,50,50,350,fill="red",width=3)
        #print('x win')
        #print('2')
        return True
    if miniTest(xList,'00','01','02'):
        conteneur.create_line(50,50,50,350,fill="red",width=3)
        #print('x win')
        #print('3')
        return True
    if miniTest(xList,'10','11','12'):
        conteneur.create_line(200,50,200,350,fill="red",width=3)
        #print('x win')
        #print('4')
        return True
    if miniTest(xList,'20','21','22'):
        conteneur.create_line(350,50,350,350,fill="red",width=3)
        #print('x win')
        #print('5')
        return True
    if miniTest(xList,'00','10','20'):
        conteneur.create_line(50,50,350,50,fill="red",width=3)
        #print('x win')
        #print('6')
        return True
    if miniTest(xList,'01','11','21'):
        conteneur.create_line(50,200,350,200,fill="red",width=3)
        #print('x win')
        #print('7')
        return True
    if miniTest(xList,'02','12','22'):
        conteneur.create_line(50,350,350,350,fill="red",width=3)
        #print('x win')
        #print('8')
        return True

    
    if miniTest(oList,'00','11','22'):
        conteneur.create_line(50,50,350,350,fill="red",width=3)
        #print('o win')
        #print('1')
        return True
    if miniTest(oList,'20','11','02'):
        conteneur.create_line(350,50,50,350,fill="red",width=3)
        #print('o win')
        #print('2')
        return True
    if miniTest(oList,'00','01','02'):
        conteneur.create_line(50,50,50,350,fill="red",width=3)
        #print('o win')
        #print('3')
        return True
    if miniTest(oList,'10','11','12'):
        conteneur.create_line(200,50,200,350,fill="red",width=3)
        #print('o win')
        #print('4')
        return True
    if miniTest(oList,'20','21','22'):
        conteneur.create_line(350,50,350,350,fill="red",width=3)
        #print('o win')
        #print('5')
        return True
    if miniTest(oList,'00','10','20'):
        conteneur.create_line(50,50,350,50,fill="red",width=3)
        #print('o win')
        #print('6')
        return True
    if miniTest(oList,'01','11','21'):
        conteneur.create_line(50,200,350,200,fill="red",width=3)
        #print('o win')
        #print('7')
        return True
    if miniTest(oList,'02','12','22'):
        conteneur.create_line(50,350,350,350,fill="red",width=3)
        #print('o win')
        #print('8')
        return True
    return False

def somOneWon():
    global arrDetails ,playerNow, xList, oList
    ch=""
    lx=[]
    lo=[]
    for elem in arrDetails:
        
        if elem["playerNow"]=="x":
            lx.append(elem["index"])
        else:
            lo.append(elem["index"])
    if playerNow == "x":
        xList=lx
    else: oList=lo
    
    return checkLists()
    
def onClick(event):
    chaine.configure(text="Clic détecté en X = " + str(event.x) + ", Y = " + str(event.y))
    global playerNow, arrDetails ,PlayTime, someoneWin, whoWin, resized_im
    global FristPlayerScore, FristPlayer, SecondPlayer, SecondPlayerScore
    global FristPlayerScore1, FristPlayer1, SecondPlayer1, SecondPlayerScore1
    x,y,z=fixPointer(event.x,event.y)
    if someoneWin:
        message.configure(text=whoWin+" won !!")
    elif(serachDispo(x,y)):
        message.configure(text="")
        createImage(x,y)
        arrDetails[PlayTime]={"playerNow":playerNow,"nom":str,"x":x,"y":y,"index":z}
        
        if somOneWon()==True:
            someoneWin = True
            whoWin = playerNow

            #conteneur.create_image(115 , 115, image=resized_im, anchor='nw')
            #print("x")

            if whoWin==FristPlayer:
                FristPlayerScore+=1
                FristPlayerScore1.set(str(FristPlayerScore))#dddddddddddddddd
                try:
                    SecondPlayerScore1.set(str(SecondPlayerScore))#dddddddddddddddd
                except:
                    NewGame()
            else:
                SecondPlayerScore+=1
                try:
                    SecondPlayerScore1.set(str(SecondPlayerScore))#dddddddddddddddd
                except:
                    NewGame()
            message.configure(text=playerNow+" won !! ")
            cadre = conteneur.bind( "<Button-1>", None )  
            
        else:
            PlayTime+=1
            if  playerNow == "x":
                playerNow = "o"
            else :
                playerNow = "x"
        if not someoneWin  and PlayTime >=9:
            message.configure(text=whoWin+" Null !!")
            whoWin="null"
        
        
    else:
        message.configure(text="u cant")
        #print(arrDetails)
def initTheGame():
    global  arrDetails, PlayTime, cadre, someoneWin, whoWin, FristPlayer, SecondPlayer,playerNow, xList,oList, conteneur
    global  FristPlayerScore,FristPlayerScore1,SecondPlayerScore1
    global  SecondPlayerScore
    someoneWin=False
    whoWin=""
    PlayTime=0
    FristPlayer="x"
    SecondPlayer="o"
    FristPlayerScore=FristPlayerScore
    #print(FristPlayer," : ",FristPlayerScore)

    FristPlayer1.set("player 1 :"+FristPlayer+" : ")
    FristPlayerScore1.set(str(FristPlayerScore))

    
    SecondPlayerScore=SecondPlayerScore
    #print(SecondPlayer," : " ,SecondPlayerScore)

    SecondPlayer1.set("player 2 :"+SecondPlayer+" : ")
    SecondPlayerScore1.set(str(SecondPlayerScore))
    #print(SecondPlayer)
    score={"FristPlayer":{"role":FristPlayer,"score":FristPlayerScore}, "SecondPlayer":{"role":SecondPlayer,"score":SecondPlayerScore}}
    playerNow="o"
    xList=[]
    oList=[]

    details={"playerNow":str,"nom":str,"x":float,"y":float,"index":""}
    arrDetails=array(([details]*3)*3)
    
    conteneur = Canvas(xo, bg="black", width=400, height=400)

    conteneur.create_line(133.3, 0, 133.3, 400, fill='red', width=5)
    conteneur.create_line(266.7, 0, 266.7, 400, fill='red', width=5)

    conteneur.create_line(0, 133.3, 400, 133.3, fill='red', width=5)
    conteneur.create_line(0, 266.7, 400, 266.7, fill='red', width=5)

    cadre = conteneur.bind("<Button-1>", onClick)


    
    conteneur.pack()

if __name__=="__main__":
    xo = Tk()
    xo.geometry("400x550")
    xo.title("wajih")
    x_img = PhotoImage(file="C:/Users/wajih/OneDrive/Bureau/Python 2/Tic_tac_toex.svg.png")
    resized_x_img = x_img.subsample(x_img.width() // 107, x_img.height() // 105)

    o_img = PhotoImage(file="C:/Users/wajih/OneDrive/Bureau/Python 2/Tic_tac_toeo.svg.png")
    resized_o_img = o_img.subsample(o_img.width() // 104, o_img.height() // 105)

    im = PhotoImage(file="C:/Users/wajih/OneDrive/Bureau/Python 2/giphy.gif")
    resized_im = im.subsample(im.width() //200, im.height() //150)
    someoneWin=False
    whoWin=""
    PlayTime=0
    FristPlayer="x"
    FristPlayerScore=0
    
    FristPlayer1=StringVar(value="player 1 :"+FristPlayer+" : ")
    FristPlayerScore1=StringVar(value=str(FristPlayerScore))
    
    SecondPlayer="o"
    SecondPlayerScore=0

    SecondPlayer1=StringVar(value="player 2 :"+SecondPlayer+" : ")
    SecondPlayerScore1=StringVar(value=str(SecondPlayerScore))

    score={"FristPlayer":{"role":FristPlayer,"score":FristPlayerScore}, "SecondPlayer":{"role":SecondPlayer,"score":SecondPlayerScore}}
    playerNow="o"

    xList=[]
    oList=[]
    chaine = Label(xo,text="Welcome to wajih's game")
    chaine.pack()
    message = Label(xo,text="Have a nice Game !! ")
    message.pack()
    rePlay = Button(xo,text="Start",command=Replay)
    rePlay.pack()
    result=Frame(xo,bg='green',width=200,height=80)
    p1=Label(result,textvariable=FristPlayer1,bg='green')
    p1.grid(row=0,column=0)
    s1=Label(result,textvariable=FristPlayerScore1,bg='green')
    s1.grid(row=0,column=1)
    v1=Label(result,text=" |  ")
    v1.grid(row=0,column=2)
    p2=Label(result,textvariable=SecondPlayer1,bg='red')
    p2.grid(row=0,column=3)
    s2=Label(result,textvariable=SecondPlayerScore1,bg='red')
    s2.grid(row=0,column=4)
    result.pack()
    MenuBar=Menu(xo)
    Menu_XO=Menu(MenuBar,tearoff=0)
    MenuBar.add_cascade( label = " Menu " , menu=Menu_XO )
    Menu_XO.add_command( label="New game" , command = NewGame ) 
    xo.config (menu = MenuBar)

    xo.mainloop()
