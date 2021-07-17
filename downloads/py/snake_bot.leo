<?xml version="1.0" encoding="utf-8"?>
<!-- Created by Leo: http://leoeditor.com/leo_toc.html -->
<leo_file xmlns:leo="http://leoeditor.com/namespaces/leo-python-editor/1.1" >
<leo_header file_format="2"/>
<globals/>
<preferences/>
<find_panel_settings/>
<vnodes>
<v t="yen.20210717224944.1"><vh>@settings</vh>
<v t="yen.20210717224944.2"><vh>@data qt-gui-plugin-style-sheet</vh></v>
<v t="yen.20210717224944.3"><vh>@string initial_split_orientation = horizontal</vh></v>
</v>
<v t="yen.20210717225048.1"><vh>About </vh></v>
<v t="yen.20210717233015.1"><vh>20210717 修改</vh></v>
<v t="yen.20210717224533.1"><vh>@clean snake_bot.py</vh>
<v t="yen.20210717225032.1"><vh>Declarations (snake_bot.py)</vh></v>
<v t="yen.20210717225032.2"><vh>class cube(object)</vh>
<v t="yen.20210717225032.3"><vh>cube(object).__init__</vh></v>
<v t="yen.20210717225032.4"><vh>cube(object).move</vh></v>
<v t="yen.20210717225032.5"><vh>cube(object).draw</vh></v>
</v>
<v t="yen.20210717225032.6"><vh>class snake(object)</vh>
<v t="yen.20210717225032.7"><vh>snake(object).__init__</vh></v>
<v t="yen.20210717225032.8"><vh>snake(object).move</vh></v>
<v t="yen.20210717225032.9"><vh>snake(object).reset</vh></v>
<v t="yen.20210717225032.10"><vh>snake(object).addCube</vh></v>
<v t="yen.20210717225032.11"><vh>snake(object).draw</vh></v>
</v>
<v t="yen.20210717225032.12"><vh>drawGrid (snake_bot.py)</vh></v>
<v t="yen.20210717225032.13"><vh>drawScore (snake_bot.py)</vh></v>
<v t="yen.20210717225032.14"><vh>drawPressKeyMsg (snake_bot.py)</vh></v>
<v t="yen.20210717225032.15"><vh>redrawWindow (snake_bot.py)</vh></v>
<v t="yen.20210717225032.16"><vh>randomSnack (snake_bot.py)</vh></v>
<v t="yen.20210717225032.17"><vh>showGameOverScreen (snake_bot.py)</vh></v>
<v t="yen.20210717225032.18"><vh>checkForKeyPress (snake_bot.py)</vh></v>
<v t="yen.20210717225032.19"><vh>best_first_search (snake_bot.py)</vh></v>
<v t="yen.20210717225032.20"><vh>manhattan_dis (snake_bot.py)</vh></v>
<v t="yen.20210717225032.21"><vh>main (snake_bot.py)</vh></v>
</v>
</vnodes>
<tnodes>
<t tx="yen.20210717224533.1">@others
@language python
@tabwidth -4
</t>
<t tx="yen.20210717224944.1"></t>
<t tx="yen.20210717224944.2">QSplitter::handle {
    background-color: #CAE1FF; /* lightSteelBlue1 */
}

QStackedWidget {
    /* background-color:lightpink; */
    border-color: red;
    padding: 0px;
    /* border-width: 0px; */
    /* background-color: yellow; */
}

QSplitter {
    border-color: white;
    background-color: white;
    border-style: solid;
}

QTreeWidget {
    /* These apply to the selected item, but not to editing items.*/
    background-color: #ffffec; /* Leo's traditional tree color */
    selection-color: black; /* was white */
    selection-background-color: lightgrey;
    /* font-family: SansSerif; */
    /*font-family: DejaVu Sans Mono;*/
    font-family:YaHei Mono;
    /* 標題字型大小設定 */
    font-size: 22px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal, italic,oblique */
 }

/* Headline edit widgets */
QTreeWidget QLineEdit {
    background-color: cornsilk;
    selection-color: white;
    selection-background-color: blue;
    /*font-family: DejaVu Sans Mono;*/    
    font-family:YaHei Mono;
    /* 沒有特別對應字型大小 */
    font-size: 22px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal, italic,oblique */
}

/* The log panes */
QTextEdit {
    background-color: #f2fdff;
    selection-color: red;
    selection-background-color: blue;
    /* font-family: Courier New; */
    font-family:YaHei Mono;
    /* log font 大小 */
    font-size: 22px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal, italic,oblique */
}

/* The body pane */
QTextEdit#richTextEdit {
    background-color: #fdf5f5; /* A kind of pink. */
    selection-color: white;
    selection-background-color: red;
    /*font-family: DejaVu Sans Mono;*/
    /* font-family: Courier New; */
    font-family:YaHei Mono;
    /* 內文字型大小 */
    font-size: 22px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal,italic,oblique */
}

QLabel {
    font-family:YaHei Mono;
    /* 下方的 Minibuffer 標題字型大小 */
    font-size: 22px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal,italic,oblique */
}

/* Editor labels */
QLineEdit#editorLabel {
    background-color: #ffffec;
    font-family:YaHei Mono;
    /* 沒有直接對應字型大小 */
    font-size: 22px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal,italic,oblique */
    border: 2px;
    margin: 2px;
}</t>
<t tx="yen.20210717224944.3">horizontal: body pane to the left
vertical: body pane on the botton</t>
<t tx="yen.20210717225032.1">import math, random, pygame, sys, copy

</t>
<t tx="yen.20210717225032.10">def addCube(self):
    tail = self.body[-1]
    dx, dy = tail.dirnx, tail.dirny

    for i in range(len(self.body)):
        if i:
            self.body[i].color = (255, 255, 255)

    if dx == 1 and dy == 0:
        self.body.append(cube((tail.pos[0]-1,tail.pos[1]),color=self.color))
    elif dx == -1 and dy == 0:
        self.body.append(cube((tail.pos[0]+1,tail.pos[1]),color=self.color))
    elif dx == 0 and dy == 1:
        self.body.append(cube((tail.pos[0],tail.pos[1]-1),color=self.color))
    elif dx == 0 and dy == -1:
        self.body.append(cube((tail.pos[0],tail.pos[1]+1),color=self.color))

    self.body[-1].dirnx = dx
    self.body[-1].dirny = dy
    

</t>
<t tx="yen.20210717225032.11">def draw(self, surface):
    for i, c in enumerate(self.body):
        if i == 0:
            c.draw(surface, True)
        else:
            c.draw(surface)


</t>
<t tx="yen.20210717225032.12">def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (236,240,241), (x,0),(x,w))
        pygame.draw.line(surface, (236,240,241), (0,y),(w,y))

</t>
<t tx="yen.20210717225032.13">def drawScore(score):
    score_font = pygame.font.SysFont('Raleway', 20, bold=True)
    score_surface = score_font.render('Score : ' + str(score), True, pygame.Color(153, 255, 51))
    score_rect = score_surface.get_rect()
    score_rect.topleft = (width-120, 10)
    win.blit(score_surface, score_rect)

</t>
<t tx="yen.20210717225032.14">def drawPressKeyMsg():
    press_font = pygame.font.SysFont('Raleway', 25)
    pressKeySurf = press_font.render('Press a key to play.', True, (255, 255, 255))
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.midtop = (250, 350)
    win.blit(pressKeySurf, pressKeyRect)

</t>
<t tx="yen.20210717225032.15">def redrawWindow(lose = False):
    win.fill((0,0,0))
    s.draw(win)
    snack.draw(win,food=True)
    if (not(lose)):
        drawGrid(width,rows, win)
    drawScore(len(s.body)-1)
    pygame.display.update()


</t>
<t tx="yen.20210717225032.16">def randomSnack(rows, item):

    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) &gt; 0:
            continue
        else:
            break
        
    return (x,y)

</t>
<t tx="yen.20210717225032.17">def showGameOverScreen():
    gameOverFont = pygame.font.SysFont("courier new", 150)
    gameSurf = gameOverFont.render('Game', True, pygame.Color(255, 255, 255))
    overSurf = gameOverFont.render('Over', True, pygame.Color(255, 255, 255))
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (width / 2, 10)
    overRect.midtop = (width / 2, gameRect.height + 10 + 25)

    win.blit(gameSurf, gameRect)
    win.blit(overSurf, overRect)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress()

    while True:
        if checkForKeyPress():
            pygame.event.get() 
            return

</t>
<t tx="yen.20210717225032.18">def checkForKeyPress():
    if len(pygame.event.get(pygame.QUIT)) &gt; 0:
        pygame.quit()
        sys.exit()
    keyUpEvents = pygame.event.get(pygame.KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()
    return keyUpEvents[0].key

</t>
<t tx="yen.20210717225032.19">def best_first_search():
    global rows, s, snack, visited
    curr_posx = s.body[0].pos[0]
    curr_posy = s.body[0].pos[1]
    nodes = [] # 0: left, 1: right, 2: up, 3: down
    p = ((curr_posx-1)%rows,curr_posy)
    nodes.append(('left', manhattan_dis((curr_posx-1,curr_posy),snack.pos,size=rows), p))
    p = ((curr_posx+1)%rows,curr_posy)
    nodes.append(('right', manhattan_dis((curr_posx+1,curr_posy),snack.pos,size=rows), p))
    p = (curr_posx,(curr_posy-1)%rows)
    nodes.append(('up', manhattan_dis((curr_posx,curr_posy-1),snack.pos,size=rows), p))
    p = (curr_posx,(curr_posy+1)%rows)
    nodes.append(('down', manhattan_dis((curr_posx,curr_posy+1),snack.pos,size=rows), p))
    if set(nodes[:][2])&lt;= set(list(map(lambda z:z.pos,s.body))):
        s.move()
        return
    i = 0 
    print()
    best = []
    dist = []
    for p in nodes:
        prio = 0
        if (len(s.body)&gt;2):
            temp = [((curr_posx+1)%rows,(curr_posy+1)%rows),((curr_posx+1)%rows,(curr_posy-1)%rows)]
            if set(temp) &lt;= set(list(map(lambda z:z.pos,s.body))):
                if p[0]=="right":
                    prio += 1
                elif (p[0]=="up" and s.curr_dir=="right" and s.last_dir=="up") or (p[0]=="down" and s.curr_dir=="right" and s.last_dir=="down"):
                    prio += 1
            temp = [((curr_posx-1)%rows,(curr_posy+1)%rows),((curr_posx-1)%rows,(curr_posy-1)%rows)]
            if set(temp) &lt;= set(list(map(lambda z:z.pos,s.body))):
                if p[0]=="left":
                    prio += 1
                elif (p[0]=="up" and s.curr_dir=="left" and s.last_dir=="up") or (p[0]=="down" and s.curr_dir=="left" and s.last_dir=="down"):
                    prio += 1
            temp = [((curr_posx+1)%rows,(curr_posy+1)%rows),((curr_posx-1)%rows,(curr_posy+1)%rows)]
            if set(temp) &lt;= set(list(map(lambda z:z.pos,s.body))):
                if p[0]=="down":
                    prio += 1
                elif (p[0]=="left" and s.curr_dir=="down" and s.last_dir=="left") or (p[0]=="right" and s.curr_dir=="down" and s.last_dir=="right"):
                    prio += 1
            temp = [((curr_posx+1)%20,(curr_posy-1)%rows),((curr_posx-1)%rows,(curr_posy-1)%rows)]
            if set(temp) &lt;= set(list(map(lambda z:z.pos,s.body))):
                if p[0]=="up":
                    prio += 1
                elif (p[0]=="left" and s.curr_dir=="up" and s.last_dir=="left") or (p[0]=="right" and s.curr_dir=="up" and s.last_dir=="right"):
                    prio += 1
            cy = 0
            if curr_posy &gt; rows-4 and curr_posy &lt; rows-1:
                cy = rows-1 - curr_posy
            elif curr_posy &lt; rows-3:
                cy = 3
            bottom = [q for q in list(map(lambda z:z.pos,s.body)) if q[0]==curr_posx and q[1]-curr_posy &lt; cy and curr_posy&lt;q[1]]
            for i in range(3-cy):
                if (curr_posx,i) in list(map(lambda z:z.pos,s.body)): bottom.append((curr_posx,i))
            print("bottom " + str(bottom))    
            cy = 0
            if curr_posy &gt; 0 and curr_posy &lt; 3:
                cy = curr_posy
            elif curr_posy &gt; 2:
                cy = 3
            top = [q for q in list(map(lambda z:z.pos,s.body)) if q[0]==curr_posx and curr_posy-q[1] &lt; cy and curr_posy&gt;q[1]]
            for i in range(rows-1,rows-4+cy,-1):
                if (curr_posx,i) in list(map(lambda z:z.pos,s.body)): top.append((curr_posx,i))
            print("top " + str(top))
            cx = 0
            if curr_posx &gt; 0 and curr_posx &lt; 3:
                cx = curr_posx
            elif curr_posx &gt; 2:
                cx = 3
            left = [q for q in list(map(lambda z:z.pos,s.body)) if q[1]==curr_posy and curr_posx-q[0] &lt; cx and curr_posx&gt;q[0]]
            for i in range(rows-1,rows-1+cx,-1):
                if (i,curr_posy) in list(map(lambda z:z.pos,s.body)): left.append((i,curr_posy))
            print("left " + str(left))
            cx = 0
            if curr_posx &gt; rows-4 and curr_posx &lt; rows-1:
                cx = rows-1 - curr_posx
            elif curr_posx &lt; rows-3:
                cx = 3
            right = [q for q in list(map(lambda z:z.pos,s.body)) if q[1]==curr_posy and q[0]-curr_posx &lt; cx and curr_posx&lt;q[0]]
            for i in range(3-cx):
                if (i,curr_posy) in list(map(lambda z:z.pos,s.body)): right.append((i,curr_posy))
            print("right " + str(right))
            temp = []
            if p[0] == "up":
                if len(top) and s.curr_dir != "down":
                    prio += len(top)            
                    for q in top:
                        temp.append(manhattan_dis((curr_posx,curr_posy),q,size=rows))
                    dist.append(("up",min(temp)))
            elif p[0] == "down":
                if len(bottom) and s.curr_dir != "up":
                    prio += len(bottom)
                    for q in bottom:
                        temp.append(manhattan_dis((curr_posx,curr_posy),q,size=rows))
                    dist.append(("down",min(temp)))
            elif p[0] == "left":
                if len(left) and s.curr_dir != "right":
                    prio += len(left)
                    for q in left:
                        temp.append(manhattan_dis((curr_posx,curr_posy),q,size=rows))
                    dist.append(("left",min(temp)))
            elif p[0] == "right":
                if len(right) and s.curr_dir != "left":
                    prio += len(right)
                    for q in right:
                        temp.append(manhattan_dis((curr_posx,curr_posy),q,size=rows))
                    dist.append(("right",min(temp)))
            if p[2] in list(map(lambda z:z.pos,s.body)):
                prio += 1
        best.append((p[0],p[1],p[2],prio))
    if len(dist):
        print(dist)
        mindist = min(dist, key=lambda t: t[1])
        print(mindist)
        temp = [x[0] for x in dist if x[1]==mindist[1]]
        print(temp)
        for j in temp:
            print(j)
            near = best.pop([y[0] for y in best].index(j))
            print(near)
            best.append((near[0],near[1],near[2],near[3]+1))
    best = sorted(best,key=lambda t: (t[3],t[1]))
    print(best)
    for p in best:
        print(i)
        if p[0] == "left" and s.curr_dir != "right" and p not in visited:
            print("A")
            s.move(control="left")
            visited.add(p)
            return
        elif p[0] == "right" and s.curr_dir != "left" and p not in visited:
            print("B")
            s.move(control="right")
            visited.add(p)
            return
        elif p[0] == "up" and s.curr_dir != "down" and p not in visited:
            print("C")
            s.move(control="up")
            visited.add(p)
            return
        elif p[0] == "down" and s.curr_dir != "up" and p not in visited:
            print("D")
            s.move(control="down")
            visited.add(p)
            return
        i+=1
    s.move()
        
</t>
<t tx="yen.20210717225032.2">class cube(object):
    rows = 30
    w = 600
    @others
</t>
<t tx="yen.20210717225032.20">def manhattan_dis(p,q,size=0):
    dx = min( abs( q[0] - p[0] ), size - abs( q[0] - p[0] ) )
    dy = min( abs( q[1] - p[1] ), size - abs( q[1] - p[1] ) )
    return dx + dy

</t>
<t tx="yen.20210717225032.21">def main():
    global width, rows, s, snack, win, visited
    pygame.init()
    width = 600
    rows = 30
    win = pygame.display.set_mode((width, width))
    pygame.display.set_caption('Snake Game Bot')
    startx = random.randint(0, rows-1)
    starty = random.randint(0, rows-1)
    s = snake((255,255,51), (startx,starty))
    snack = cube(randomSnack(rows, s), color=(255, 51, 51))
    flag = True
    cost = 0
    clock = pygame.time.Clock()
    visited = set({})
    
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        best_first_search()
        if s.body[0].pos == snack.pos:
            visited = set({})
            s.addCube()
            snack = cube(randomSnack(rows, s), color=(255, 51, 51))
        if s.body[0].pos in list(map(lambda z:z.pos,s.body[1:])):
            redrawWindow(lose = True)
            print('Score: ', len(s.body)-1)
            showGameOverScreen()
            startx = random.randint(0, rows-1)
            starty = random.randint(0, rows-1)
            s.reset((startx,starty))
            snack = cube(randomSnack(rows, s), color=(255, 51, 51))
        
            
        redrawWindow()

main()
</t>
<t tx="yen.20210717225032.3">def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
    self.pos = start
    self.dirnx = 1
    self.dirny = 0
    self.color = color

    
</t>
<t tx="yen.20210717225032.4">def move(self, dirnx, dirny):
    self.dirnx = dirnx
    self.dirny = dirny
    self.pos = ((self.pos[0] + self.dirnx)%self.rows, (self.pos[1] + self.dirny)%self.rows)

</t>
<t tx="yen.20210717225032.5">def draw(self, surface, eyes=False, food=False):
    dis = self.w // self.rows
    i = self.pos[0]
    j = self.pos[1]
    if food:
        centre = dis//2
        radius = 10
        pygame.draw.circle(surface, self.color, (i*dis+centre+1,j*dis+centre+1), radius)
    else:
        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1, dis-2, dis-2))
    if eyes:
        centre = dis//2
        radius = 3
        circleMiddle = (i*dis+centre-radius,j*dis+8)
        circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
        pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
        pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)
    



</t>
<t tx="yen.20210717225032.6">class snake(object):
    rows = 30
    body = []
    turns = {}
    @others
</t>
<t tx="yen.20210717225032.7">def __init__(self, color, pos):
    self.color = color
    self.head = cube(pos,color=(102,178,255))
    self.body.append(self.head)
    self.last_dir = ""
    self.curr_dir = "right"
    self.dirnx = 1
    self.dirny = 0

</t>
<t tx="yen.20210717225032.8">def move(self, control=""):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            break

    keys = pygame.key.get_pressed()
    if control != self.curr_dir:
        self.last_dir = self.curr_dir
        if control == "left":
            self.dirnx = -1
            self.dirny = 0
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            self.curr_dir = "left"

        elif control == "right":
            self.dirnx = 1
            self.dirny = 0
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            self.curr_dir = "right" 

        elif control == "up":
            self.dirnx = 0
            self.dirny = -1
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            self.curr_dir = "up"

        elif control == "down":
            self.dirnx = 0
            self.dirny = 1
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            self.curr_dir = "down"

        else:
            for key in keys:
                if keys[pygame.K_LEFT] and self.curr_dir != "left":
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                    self.curr_dir = "left"

                elif keys[pygame.K_RIGHT] and self.curr_dir != "right":
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                    self.curr_dir = "right"

                elif keys[pygame.K_UP] and self.curr_dir != "up":
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                    self.curr_dir = "up"

                elif keys[pygame.K_DOWN] and self.curr_dir != "down":
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                    self.curr_dir = "down"
    print(self.dirnx)
    print(self.dirny)
                
    for i, c in enumerate(self.body):
        p = c.pos[:]
        if p in self.turns:
            turn = self.turns[p]
            c.move(turn[0],turn[1])
            if i == len(self.body)-1:
                self.turns.pop(p)
        else:
            if c.dirnx == -1 and c.pos[0] &lt;= 0: # out of left bound
                c.pos = (self.rows-1, c.pos[1])
            elif c.dirnx == 1 and c.pos[0] &gt;= self.rows-1: # out of right bound
                c.pos = (0,c.pos[1])
            elif c.dirny == 1 and c.pos[1] &gt;= self.rows-1: # out of bottom bound
                c.pos = (c.pos[0], 0)
            elif c.dirny == -1 and c.pos[1] &lt;= 0: # out of top bound
                c.pos = (c.pos[0], self.rows-1)
            else: c.move(c.dirnx,c.dirny)

</t>
<t tx="yen.20210717225032.9">def reset(self, pos):
    self.head = cube(pos,color=(102,178,255))
    self.body = []
    self.body.append(self.head)
    self.turns = {}
    self.dirnx = 0
    self.dirny = 1


</t>
<t tx="yen.20210717225048.1">Paper:
    https://informatika.stei.itb.ac.id/~rinaldi.munir/Stmik/2019-2020/Makalah/stima2020k3-032.pdf
    
Github:
    https://github.com/mdarud/snake-bot/blob/master/snake.py
    
need PyGame to execute

for linux and mac 
    
    pip3 install pygame 
    
    or
    
for Windows
     
     pip install pygame</t>
<t tx="yen.20210717233015.1">將 rows 改為 30
width = 600

目前仍有三個地方必須設定 rows, 兩個地方設定 width
還需要改為單一設定, 並逐行說明程式語法, 並且套用到 Brython 版本.</t>
</tnodes>
</leo_file>
