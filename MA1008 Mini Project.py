# Done by: Yap Zhen Yan 16/4/2021
import turtle

# open text files
ladderfile = open("ladder.txt", "r")
datafile = open("data.txt", "r")

players = []
for l in ladderfile:
    l = l.replace("\n", '')
    players.append(l)

info = []
for d in datafile:
    d = d.replace("\n", '')
    info.append(d)
ladderfile.close()
datafile.close()

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


s = turtle.Screen()
s.tracer(0)
s.setup(1230,653)

t = turtle.Turtle()
t1 = turtle.Turtle() #ranking
t2 = turtle.Turtle() #error box
t3 = turtle.Turtle() #pending challenge
tq = turtle.Turtle() #queries turtle
tc = turtle.Turtle() #last 2 challenge turtle
t.ht()
t1.ht()
t2.ht()
t3.ht()
tq.ht()
tc.ht()

#title
t.penup()
t.goto(-400, 300)
t.pendown()
t.pen(pencolor = "black", fillcolor = "yellow", speed = 0)
t.begin_fill()
for i in range(2):
    t.fd(700)
    t.rt(90)
    t.fd(50)
    t.rt(90)
t.end_fill()
t.penup()
t.goto(-60, 262)
t.pendown()
t.write("Welcome to Badminton League", align="center", font=("Arial",20,"bold"))
s.update()

#select action 
t.penup()
t.goto(50,200)
t.pendown()
t.pen(pencolor = "red", pensize = 3, fillcolor = "black", speed = 0)
t.begin_fill()
for i in range(2):
    t.fd(320)
    t.rt(90)
    t.fd(30)
    t.rt(90)
t.end_fill()
s.update()
t.penup()
t.goto(215,175)
t.pendown()
t.pen(pencolor = 'white', pensize = 3, speed =0)
t.write("Select Action", align="center", font=("Arial",13,"bold"))
s.update()

#categories of select action
t.penup()
t.goto(50,170)
t.pendown()
t.pen(pencolor = "red", fillcolor = "black", speed = 0)
t.begin_fill()
N = 0
for i in range(3):
    t.fd(160)
    t.rt(90)
    t.fd(30 + N)
    t.rt(90)
    t.fd(160)
    t.rt(90)
    t.fd(30 + N)
    t.rt(90)
    N+=30
t.end_fill()
s.update()
t.penup()
t.goto(55,145)
t.pendown()
t.pen(pencolor = 'white', pensize = 3, speed =0)
t.write("1. Issue Challenge", align="left", font=("Arial",12,"normal"))

t.penup()
t.goto(55,115)
t.pendown()
t.pen(pencolor = 'white', pensize = 3, speed =0)
t.write("3. Withdraw", align="left", font=("Arial",12,"normal"))

t.penup()
t.goto(55,85)
t.pendown()
t.pen(pencolor = 'white', pensize = 3, speed =0)
t.write("5. Query", align="left", font=("Arial",12,"normal")) 

t.penup()
t.goto(210,170)
t.pendown()
t.pen(pencolor = "red", fillcolor = "black", speed = 0)
t.begin_fill()
N = 0
for i in range(2):
    t.fd(160)
    t.rt(90)
    t.fd(30 + N)
    t.rt(90)
    t.fd(160)
    t.rt(90)
    t.fd(30 + N)
    t.rt(90)
    N+=30
t.end_fill()

t.penup()
t.goto(220,145)
t.pendown()
t.pen(pencolor = 'white', pensize = 3, speed =0)
t.write("2. Record Result", align="left", font=("Arial",12,"normal"))

t.penup()
t.goto(220,115)
t.pendown()
t.pen(pencolor = 'white', pensize = 3, speed =0)
t.write("4. Join", align="left", font=("Arial",12,"normal"))
s.update()

#pop-up dialogue box 
def the_msg(message):
    tq.clear()
    t2.ht()
    t2.penup()
    t2.goto(-400,210)
    t2.pendown()
    t2.pen(pencolor = "blue", fillcolor = "cyan", speed = 0)
    t2.begin_fill()
    for i in range(2):
        t2.fd(400)
        t2.rt(90)
        t2.fd(100)
        t2.rt(90)
    t2.end_fill()
    t2.penup()
    t2.goto(-180, 140)  
    t2.pendown()
    t2.pen(pencolor = "red",pensize = 3, speed = 0)
    return t2.write(message, align="center", font=("Arial",13,"bold"))
    s.update()

#pending challenges
t.penup()
t.goto(50,0)
t.pendown()
t.pen(pencolor = "red", fillcolor = "chartreuse", speed = 0)
t.begin_fill()
for i in range(2):
    t.fd(450)
    t.rt(90)
    t.fd(30)
    t.rt(90)
t.end_fill()
t.penup()
t.goto(275,-25)
t.pendown()
t.pen(pencolor = 'black', pensize = 3, speed =0)
t.write("Pending Challenges", align="center", font=("Arial",12,"bold"))
s.update()

#last 2 matches box
t.penup()
t.goto(50,-130)
t.pendown()
t.pen(pencolor = 'red', fillcolor = 'gold', pensize = 3, speed = 0)
n = 0
l = 0
t.begin_fill()
for i in range(3):
    t.fd(550)
    t.rt(90)
    t.fd(30 + n)
    t.rt(90)
    t.fd(550)
    t.rt(90)
    t.fd(30 + n)
    t.rt(90)
    n += 30
t.end_fill()
t.penup()
t.goto(188, -160)
t.pendown()
t.rt(90)
t.fd(60)
t.penup()
t.goto(320, -160)
t.pendown()
t.fd(60)
t.penup()
t.goto(420, -160)
t.pendown()
t.fd(60)
s.update()

while True:
    t1.clear()
    t3.clear()
    tc.clear()
    
    #rank
    t1.ht()
    t1.penup()
    t1.goto(-600, 200)  
    t1.pendown()
    t1.pen(pencolor = "red", pensize = 3, speed = 0)
    n = 0
    for j in range(len(players)):  
        t1.fd(30)
        t1.rt(90)
        t1.fd(30 + n)
        t1.rt(90)
        t1.fd(30)
        t1.rt(90)
        t1.fd(30 + n)
        t1.rt(90)
        n += 30
        
    #ladder
    t1.penup()
    t1.goto(-570, 200)  
    t1.pendown()
    t1.pen(pencolor = "red", pensize = 3, speed = 0)
    n = 0
    x = 0
    for j in range(len(players)):
        t1.fd(150)
        t1.rt(90)
        t1.fd(30 + n)
        t1.rt(90)
        t1.fd(150)
        t1.rt(90)
        t1.fd(30 + n)
        t1.rt(90)
        n += 30
    for j in range(len(players)):
        t1.penup()
        t1.goto(-585, 170 + x)
        t1.pendown()
        t1.pen(pencolor = "blue", pensize = 3, speed = 0)
        t1.write(j+1, align = 'center', font = ("Arial",12,"normal"))
        t1.penup()
        t1.goto(-550, 170 + x)
        t1.pendown()
        t1.write(players[j], align = 'left', font = ("Arial",12,"normal"))
        x -= 30
    s.update()
    
    #pending challenge
    g = 0
    count = 0
    for i in range(len(info)):
        d = info[i].split("/")
        if "+" in info[i][0]:
            continue
        if "-" in info[i][0]:
            continue
        if d[3] != "" :
            continue
        count += 1
        split = info[i].split('/')
        for h in range(1):
            t3.penup()
            t3.goto(80, -60 + g)
            t3.pendown()
            t3.pen(pencolor = "blue", pensize = 3, speed = 0)
            t3.write(split[0], align = 'left', font = ("Arial",12,"normal"))
            t3.penup()
            t3.goto(250, -60 + g)
            t3.pendown()
            t3.write(split[1], align = 'left', font = ("Arial",12,"normal"))
            t3.penup()
            t3.goto(400, -60 +g)
            t3.write(split[2], align = 'left', font = ("Arial",12, "normal"))
            g -= 30
    counts = count
    t3.penup()
    t3.goto(50,-30)
    t3.pendown()
    t3.pen(pencolor = 'red', fillcolor = 'green', speed = 0)
    t3.begin_fill()
    M = 0
    for i in range(counts):
        t3.fd(450)
        t3.rt(90)
        t3.fd(30 + M)
        t3.rt(90)
        t3.fd(450)
        t3.rt(90)
        t3.fd(30 + M)
        t3.rt(90)
        M += 30
    t3.end_fill

    Z=0
    t3.penup()
    t3.goto(50,-30)
    t3.pendown()
    t3.pen(pencolor = 'red', pensize = 3, speed = 0)
    for f in range(counts):
        t3.fd(160)
        t3.rt(90)
        t3.fd(30 + Z)
        t3.rt(90)
        t3.fd(160)
        t3.rt(90)
        t3.fd(30 + Z)
        t3.rt(90)
        Z += 30
    t3.penup()
    t3.goto(50,-30)
    t3.pendown()
    Z = 0
    for f in range(counts):
        t3.fd(330)
        t3.rt(90)
        t3.fd(30 + Z)
        t3.rt(90)
        t3.fd(330)
        t3.rt(90)
        t3.fd(30 + Z)
        t3.rt(90)
        Z += 30
    s.update()

    #last 2 challenge box
    list = []
    for i in range(len(info)):
        d = info[i].split("/")
        if "+" in info[i][0]:
            continue
        if "-" in info[i][0]:
            continue
        if d[3] == "" :
            continue
        list.append(info[i])
    s1 = list[-1].split("/")
    s2 = list[-2].split("/")
    tc.pen(pencolor = "black", pensize = 3, speed = 0)
    tc.penup()
    tc.goto(320, -160)
    tc.write("Last 2 Completed Challenges", align = 'center', font = ("Arial",13,"bold"))
    tc.pendown()
    m = 0
    for z in range(len(s1)):
        tc.penup()
        tc.goto(60 + m, -190)
        tc.pendown()
        tc.write(s1[z], align = 'left', font = ("Arial",12,"normal")) 
        m += 133
    m = 0
    for z in range(len(s2)):
        tc.penup()
        tc.goto(60 + m,-220)
        tc.pendown()
        tc.write(s2[z], align = 'left', font = ("Arial",12,"normal")) 
        m += 133
    s.update()
    Action = turtle.textinput("Select Action: ", "1, 2, 3, 4, 5")
    while True:
        t2.clear()
        if Action == '4':
            name = turtle.textinput("Join", "Please enter your name (CW Lee):")
            join_date = turtle.textinput("Join", "Please enter join date (dd-mm-yyyy):") 
            datesplit = join_date.split("-")
            try:
                if (join_date[2] == "-" and join_date[5] == "-" and (1 <= int(datesplit[0]) <= months[int(datesplit[1])-1]) and datesplit[0].isdigit() and datesplit[1].isdigit() and datesplit[2].isdigit() and (len(datesplit[1]) == 2) and (1 <= int(datesplit[1]) <=12) and (len(datesplit[0]) == 2) and len(datesplit[2]) == 4) == True : 
                    join = "+" + name + "/" + join_date
                    info.append(join)        #update data file
                    players.append(name)     #update ladder file
                    break
                else:
                    message = "ERROR!\nInvalid Input!\nWrong date!"
                    the_msg(message)
                    break
            except:
                message = "ERROR!\nInvalid Input!\nWrong date!"
                the_msg(message)
                break

        if Action == '3':
            name = turtle.textinput("Withdraw", "Please enter withdrawal's name (CW Lee): ")
            withdraw_date = turtle.textinput("Withdraw", "Please enter withdrawal date (dd-mm-yyyy): ") 
            datesplit = withdraw_date.split("-")
            try:
                if (withdraw_date[2] == "-" and withdraw_date[5] == "-" and (1 <= int(datesplit[0]) <= months[int(datesplit[1])-1]) and datesplit[0].isdigit() and datesplit[1].isdigit() and datesplit[2].isdigit() and (len(datesplit[1]) == 2) and (1 <= int(datesplit[1]) <=12) and (len(datesplit[0]) == 2) and len(datesplit[2]) == 4) == True :
                    withdraw = "-" + name +  " " + str(players.index(name)+1) + "/" + withdraw_date
                    info.append(withdraw)   #update data file
                    players.remove(name)        #update ladder file
                    break
                else:
                    message = "ERROR!\nInvalid Input!\nWrong date!"
                    the_msg(message)
                    break
            except:
                message = "ERROR!\nInvalid Input!\nName not in the list!"
                the_msg(message)
                break

        if Action == '1':
             name1 = turtle.textinput("Issue Challenge", "Please enter challenger name: ")
             name2 = turtle.textinput("Issue Challenge", "Please enter challenged name: ")
             try:
                 if 0<(players.index(name1) - players.index(name2)) <= 3: #Valid Challenge
                     challenge_date = turtle.textinput("Issue Challenge", "Please enter date of challenge (dd-mm-yyyy): ") 
                     datesplit = challenge_date.split("-")
                     if (challenge_date[2] == "-" and challenge_date[5] == "-" and (1 <= int(datesplit[0]) <= months[int(datesplit[1])-1]) and datesplit[0].isdigit() and datesplit[1].isdigit() and datesplit[2].isdigit() and (len(datesplit[1]) == 2) and (1 <= int(datesplit[1]) <=12) and (len(datesplit[0]) == 2) and len(datesplit[2]) == 4) == True :
                         challenge = name1 + " " + str(players.index(name1)+1) + "/" + name2 + " " + str(players.index(name2)+1) + "/" + challenge_date + "/"
                         info.append(challenge) #update data file
                         break
                     else:
                         message = "ERROR!\nInvalid Input!\nWrong date!"
                         the_msg(message)
                         break
                 else:                    
                     message= "Invalid Challenge!\nYou can only challenged\nup to 3 places above you!"
                     the_msg(message)
                     break                
             except:
                 message = "Error!\nInvalid Challenge!\nName is not registered!"
                 print(message)
                 the_msg(message)
                 break

        if Action == '2':
            name1 = turtle.textinput("Record Result", "Please enter challenger name: ")
            name2 = turtle.textinput("Record Result", "Please enter challenged name: ")
            challenge_date = turtle.textinput("Record Result", "Please enter date of challenge (dd-mm-yyyy): ")
            challenge = name1 + " " + str(players.index(name1)+1) + "/" + name2 + " " + str(players.index(name2)+1) + "/" + challenge_date + "/"
            scores = turtle.textinput("Record Result", "Enter the score (xx-yy xx-yy xx-yy) based on the number of matches played: ")
            #insert score
            try:
                pos = info.index(challenge)
                info[pos]= challenge + scores   #update data file
            except ValueError:
                message = "Error!\nInvalid challenge!\n(Wrong challenge date\nor Wrong name!)"
                the_msg(message)
                break
            #outcome of match
            match_score = scores.split()
            win = 0
            lose = 0
            for i in range(len(match_score)):
                indv_score = match_score[i].split('-')
                if int(indv_score[0]) > int(indv_score[1]):
                    win += 1
                else:
                    lose +=1
            if win == 2: #changes to ranking  #update ladder file
                players.remove(name1)
                players.insert(players.index(name2), name1)
                break
            else: #ranking remains the same
                break
            
        if Action == '5':
            #query box
            tq.clear()
            tq.ht()
            tq.penup()
            tq.goto(-400, 200)
            tq.pendown()
            tq.pen(pencolor = 'black', fillcolor = 'mistyrose', speed = 0)
            tq.begin_fill()
            for i in range(2):
                tq.fd(440)
                tq.rt(90)
                tq.fd(502)
                tq.rt(90)
            tq.end_fill()
            
            tq.penup()
            tq.goto(-180, 170)
            tq.pendown()
            tq.pen(pencolor = "black", pensize = 3, speed = 0)
            tq.write("Queries", align = 'center', font = ("Arial", 13, "bold", 'underline'))                     
            msg = ["a) Order of ladder on a specific date", "b) Data of a specific challenge based on names of players", "c) Data of a specifc challenge based on the date", "d) List of matches a player has played", "e) Most Active player", "f) Least Active Player", "g) List of matches played in a specific date range"]
            for i in range(7):
                tq.penup()
                tq.goto(-380, 170 + g)
                tq.pendown()
                tq.pen(pencolor = "black", pensize = 3, speed = 0)
                tq.write(msg[i], align = 'left', font = ("Arial",12,"normal"))
                g -= 30
            s.update()

            Query = turtle.textinput("Select Query", "a, b, c, d, e, f, g ")
            
            tq.clear()
            tq.penup()
            tq.goto(-400, 200)
            tq.pendown()
            tq.pen(pencolor = 'black', fillcolor = 'mistyrose', speed = 0)
            tq.begin_fill()
            for i in range(2):
                tq.fd(440)
                tq.rt(90)
                tq.fd(520)
                tq.rt(90)
            tq.end_fill()
            
            tq.penup()
            tq.goto(-380, 170)
            tq.pendown()
            
            if Query == 'a': #order of ladder on a specific date
                new_ladder = players.copy()
                date = turtle.textinput("Order of ladder","Please enter the date (dd-mm-yyyy): ")  
                c = 0
                datesplit = date.split("-")
                try:
                    if ((date[2] == "-") and (date[5] == "-") and 1 <= int(datesplit[0]) <= months[int(datesplit[1])-1] and (datesplit[0].isdigit()) and (datesplit[1].isdigit()) and datesplit[2].isdigit() and (len(datesplit[1]) == 2) and 1 <= int(datesplit[1]) <=12 and len(datesplit[0]) == 2 and len(datesplit[2])==4) == True :
                        for j in range(len(info)):
                            split = info[j].split('/')
                            if (len(split) == 4) and (date in split[2]):
                                start_index = info.index(info[j])
                            if (len(split) == 2) and (date in split[1]):
                                start_index = info.index(info[j])
  
                        for i in range((len(info)-1),(start_index), -1):
                            split2 = info[i].split('/')   

                            if "+" in split2[0][0]:
                                replace = split2[0].replace("+", "")
                                new_ladder.remove(replace)
                        
                            if "-" in split2[0][0]:
                                split3 = split2[0].split(" ") 
                                x = len(split3[2])
                                replace = (split2[0].replace("-", "").replace(split2[0][-x-1::1], ""))
                                new_ladder.insert((int(split3[2])-1), replace)                    

                            if (len(split2) == 4) and (split2[3] != ""): #challenge took place
                                scoresplit = split2[3].split(" ")  
                                win = 0
                                lose = 0
                                for i in range(len(scoresplit)):
                                    indv_score = scoresplit[i].split('-')   
                                    if int(indv_score[0]) > int(indv_score[1]):
                                        win += 1
                                    else:
                                        lose += 1
                                firstsplit = split2[0].split(" ")
                                length = len(firstsplit[2])
                                if win == 2: #change the ranking
                                    replace = split2[0].replace(split2[0][-length-1::1], "")
                                    new_ladder.remove(replace) #remove challenger from ranking
                                    new_ladder.insert((int(firstsplit[2])-1), replace) #add to challenger inside the ladder at correct pos.                        
    
                            if (len(split2) == 4) and (split2[3] == ""): #pending challenge #forfeit
                                firstsplit = split2[0].split(" ")
                                length = len(firstsplit[2])
                                replace = split2[0].replace(split2[0][-length-1::1], "")
                                new_ladder.remove(replace)   #remove challenger from ranking
                                new_ladder.insert((int(firstsplit[2])-1), replace) #add to challenger inside the ladder at correct pos.

                        tq.penup()
                        tq.goto(-200,200)
                        tq.pendown()
                        message = "Ranking on " + date
                        tq.write(message, align = 'center', font = ("Arial", 13, "bold"))
                        for i in range(len(new_ladder)):
                            tq.penup()
                            tq.goto(-280,170 + c)
                            tq.pendown()
                            message = str(int(new_ladder.index(new_ladder[i])) + 1) + ") " + new_ladder[i]
                            tq.write(message, align = 'left', font = ("Arial",12,"normal"))
                            c -= 30
                            s.update()                
                        break
                    else:
                        message= "ERROR!\nInvalid Input!\nWrong date!"
                        the_msg(message)
                        break
                except:
                    message = "Invalid Input!"
                    the_msg(message)
                    break
                        
            
            if Query == 'b': #data of a specific challenge based on the names of the players (1 name or 2 name?)
                name1 = turtle.textinput("Data of specific challenge", "Please enter the name of the player: ")
                name2 = turtle.textinput("Data of specific challenge", "Please enter the name of the second player: ")
                data = []
                c = 0
                for i in range(len(info)):
                    d = info[i].split("/")
                    if name1 in info[i]:
                        if "+" in info[i][0]:
                            continue
                        if "-" in info[i][0]:
                            continue
                        if d[3] == "":
                            continue
                        if name2 not in info[i]:
                            continue
                        data.append(info[i])
                message = "Challenge between " + name1 + " and " + name2 + " : "
                tq.write(message, align = 'left', font = ("Arial",13,"bold")) 
                for j in range(len(data)):
                    tq.penup()
                    tq.goto(-390,140 + c)
                    tq.pendown()
                    tq.write(data[j-1], align = 'left', font = ("Arial",12,"normal"))
                    c -= 30
                s.update()
                break
            
            if Query == 'c': #data of a specific challenge based on the date
                date = turtle.textinput("Data of specific challenge", "Please enter the date (dd-mm-yyyy): ") 
                datesplit = date.split("-")
                try:
                    if ((date[2] == "-") and (date[5] == "-") and 1 <= int(datesplit[0]) <= months[int(datesplit[1])-1] and (datesplit[0].isdigit()) and (datesplit[1].isdigit()) and datesplit[2].isdigit() and (len(datesplit[1]) == 2) and 1 <= int(datesplit[1]) <=12 and len(datesplit[0]) == 2 and len(datesplit[2])==4) == True :                        
                        message = "Data on " + date + " :"
                        tq.penup()
                        tq.goto(-180, 170)
                        tq.pendown()
                        tq.write(message, align = 'center', font = ("Arial",13,"underline","bold"))
                        list = []
                        n = 0
                        for i in range(len(info)):
                            d = info[i].split("/")
                            if date in info[i]:
                                if "+" in info[i][0]:
                                    continue
                                if "-" in info[i][0]:
                                    continue
                                if d[3]== "":
                                    continue
                                list.append(info[i])
                        for i in range(len(list)):
                            tq.penup()
                            tq.goto(-380,140 + n)
                            tq.pendown()
                            tq.write(list[i], align = 'left', font = ("Arial",12,"normal"))
                            n -= 30
                        s.update()
                        break
                    else:
                        message = "Error!\nInvalid Date Input"
                        the_msg(message)
                        break
                except:
                    message = "Error!\nInvalid Input"
                    the_msg(message)
                    break
                    
            if Query == 'd': #the list of matches a player has played, with all the associated data
                name = turtle.textinput("List of matches played", "Please enter the name of the player: ")
                message = "List of matches played by " + name + " :"
                tq.penup()
                tq.goto(-180, 170)
                tq.pendown()
                tq.write(message, align = 'center', font = ("Arial",13,"underline","bold"))
                list = []
                n = 0
                for i in range(len(info)):
                    d = info[i].split("/")
                    if name in info[i]:
                        if "+" in info[i][0]:
                            continue
                        if "-" in info[i][0]:
                            continue
                        if d[3]== "":
                            continue
                        list.append(info[i])
                for i in range(len(list)):
                    tq.penup()
                    tq.goto(-380,140 + n)
                    tq.pendown()
                    tq.write(list[i], align = 'left', font = ("Arial",12,"normal"))
                    n -= 30
                s.update()
                break


            if Query == 'e': #the most active player (most matches)
                t1.clear()
                match = {}
                for i in range(len(info)):
                    d = info[i].split("/")
                    if "+" in info[i][0]:
                        continue
                    if "-" in info[i][0]:
                        continue
                    if d[3] == "":
                        continue
                    name1 = ''.join([j for j in d[0] if not j.isdigit()])
                    name2 = ''.join([n for n in d[1] if not n.isdigit()])
                    #no. of matches played by each player
                    if name1 not in match:
                        match[name1] = 0
                    if name2 not in match:
                        match[name2] = 0
                    if name1 in match:
                        match[name1] += 1
                    if name2 in match:
                        match[name2] += 1

                all_values = match.values()
                max_value = max(all_values) 
                z =[name for name, num in filter(lambda item: item[1] == max_value, match.items())]
                for m in range(len(z)):
                    message = "Most active player : " + str(z[m])
                    tq.write(message, align = 'left', font = ("Arial",12, "normal"))#turtle screen
                    s.update()
                break

            if Query == 'f': #the least active player (least matches)
                match = {}
                for i in range(len(info)):
                    d = info[i].split("/")
                    if "+" in info[i][0]:
                        continue
                    if "-" in info[i][0]:
                        continue
                    if d[3] == "":
                        continue
                    name1 = ''.join([j for j in d[0] if not j.isdigit()])
                    name2 = ''.join([n for n in d[1] if not n.isdigit()])

                    if name1 not in match:
                        match[name1] = 0
                    if name2 not in match:
                        match[name2] = 0
                    if name1 in match:
                        match[name1] += 1
                    if name2 in match:
                        match[name2] += 1

                all_values = match.values()
                min_value = min(all_values)
                z =[name for name, num in filter(lambda item: item[1] == min_value, match.items())]
                for m in range(len(z)):
                    message = "Least Active Player : " + str(z[m])
                    tq.write((message), align = 'left', font = ("Arial",12, "normal"))                
                break

            if Query == 'g': #list of matches played in a specific date range
                start_date = turtle.textinput("Matches Played", "Please enter start date (dd-mm-yyyy): ") 
                end_date = turtle.textinput("Matches played", "Please enter end date (dd-mm-yyyy) :") 
                datesplit1 = start_date.split("-")
                datesplit2 = end_date.split("-")
                matches = []
                try:
                    if ((start_date[2] == "-") and (start_date[5] == "-") and (end_date[2] == "-") and (end_date[5] == "-") and 1 <= int(datesplit1[0]) <= months[int(datesplit1[1])-1] and 1 <= int(datesplit2[0]) <= months[int(datesplit2[1])-1] and (datesplit1[0].isdigit()) and (datesplit1[1].isdigit()) and (datesplit2[0].isdigit()) and (datesplit2[1].isdigit()) and datesplit1[2].isdigit() and (len(datesplit1[1]) == 2) and datesplit2[2].isdigit() and (len(datesplit2[1]) == 2) and 1 <= int(datesplit1[1]) <=12 and len(datesplit1[0]) == 2 and len(datesplit1[2])==4 and 1 <= int(datesplit2[1]) <=12 and len(datesplit2[0]) == 2 and len(datesplit2[2])==4) == True :
                        for i in range(len(info)):
                            d = info[i].split("/")
                            if "+" in info[i][0]:
                                continue
                            if "-" in info[i][0]:
                                continue
                            matches.append(info[i])
                        for j in range(len(matches)):
                            split = matches[j].split('/')
                            if start_date in split[2]:
                                start_index = matches.index(matches[j])
                            if end_date in split[2]:
                                end_index = matches.index(matches[j])
                        tq.penup()
                        tq.goto(-240, 170)
                        tq.pendown()
                        message = "From " + str(start_date) + " to " + str(end_date)
                        tq.write(message, align = 'center', font = ('Arial', 13, 'bold', 'underline'))
                        n = 0
                        for x in range(start_index, end_index + 1):
                            tq.penup()
                            tq.goto(-395,140 + n)
                            tq.pendown()
                            n -= 30
                            tq.write(matches[x], align = 'left', font = ('Arial', 12, 'normal')) 
                        s.update()
                        break
                    else:
                        message = "Error!\nInvalid Date Input"
                        the_msg(message)
                        break
                except:
                    message = "Error!\nInvalid Input"
                    the_msg(message)
                    break
        else:
            break

        
    ladderfile = open('ladder.txt', 'w')    
    for n in range(len(players)):
        print(players[n], file = ladderfile)
    ladderfile.close()

    datafile = open('data.txt', 'w') 
    for m in range(len(info)):
        print(info[m], file = datafile)
    datafile.close()
  
