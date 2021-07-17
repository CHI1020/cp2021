# 從 browser 導入 document 並設為 doc
from browser import document as doc
# 使用者可以透過 window 當作介面使用其他 Javascript 功能
from browser import html, window
# 用於定時執行特定函式
import browser.timer
# 導入數學模組
import math
# 導入亂數模組
from random import random, randint
 
def update_score(new_score):
    global high_score
    score_doc.innerHTML = "Score: " + str(new_score)
    if new_score > high_score:
        high_score_doc.innerHTML = "High Score: " + str(new_score)
        high_score = new_score
        
def eat(px, py, ax, ay):
    global xv, yv, pre_pause, paused
    # (px, py) go to (ax, ay) through incremented xv, yv
    if ax != px or ay != py:
        if ax > px and not paused:
            xv = 1
            yv = 0
        if ax < px and not paused:
            xv = -1
            yv = 0
        if ay > py and not paused:
            xv = 0
            yv = 1
        if ay < py and not paused:
            xv = 0
            yv = -1

    '''
    if ax > px and not paused:
        xv = 0
        yv = -1
    if ay < py and not paused:
        xv = -1
        yv = 0          
    if ay > py and not paused:
        xv = 1
        yv = 0 
    '''
            
def game():
    global px, py, tc, gs, ax, ay, trail, tail, score
    # px 為 snake 第一個點的 x 座標, 增量值為 xv
    px += xv
    py += yv
    # 允許穿越四面牆, 以 tc 表示牆面座標極限
    # 若 px 為負值則設定為 tc -1, 表示 tc 為 x 方向 limit
    # x 座標方向的穿牆設定
    if px < 0:
        px = tc-1
    if px > tc-1:
        px = 0
    # y 座標方向的穿牆設定
    if py < 0:
        py = tc-1
    if py > tc-1:
        py = 0
    ctx.fillStyle = "black"
    # 畫布填入黑色
    ctx.fillRect(0, 0, canvas.width, canvas.height)
    # snake 為 lime 色
    ctx.fillStyle = "lime"
    # trail 為數列, 代表 snake 各節 [x,y] 座標
    # trail = [[x0,y0], [x1, y1], [x2, y2]...]
    # gs 為方塊邊長 pixel 數
    for i in range(len(trail)):
        # https://developer.mozilla.org/zh-TW/docs/Web/API/Canvas_API/Tutorial/Drawing_shapes
        # fillRect(x, y, width, height)
        ctx.fillRect(trail[i][0]*gs, trail[i][1]*gs, gs-2, gs-2)
        # 若 snake 第一節座標 (px, py)  穿過身體任一節, 則 score 歸零
        if trail[i][0] == px and trail[i][1] == py:
            score = score if paused else 0
            # snake reset 為五節
            tail = 5
    # trail 數列以碰到的 [px, py] 座標數列插入作為第一節
    trail.insert(0, [px, py])
    while len(trail) > tail:
        # pop() 內建移除數列最後一個 element
        trail.pop()
    # ax, ay 為紅點座標
    # 當 snake 第一節座標[px, py] 與紅色食物座標 [ax, ay] 重合
    # 則 tail 增量, 即多一節且得分加 1, 然後食物座標 [ax, ay] 重新以亂數定位
    if ax == px and ay == py:
        tail += 1
        ax = math.floor(random()*tc)
        ay = math.floor(random()*tc)
        score += 1
    # [ax, ay] is known here
    # [px, py] is where the head of the snake
    # xv needed to be incremented from px to ax first
    # and yv needed to be incremented from py to ay
    eat(px, py, ax, ay)
    # 更新計分顯示
    update_score(score)
    ctx.fillStyle = "red"
    ctx.fillRect(ax*gs, ay*gs, gs-2, gs-2)
   
def key_push(evt):
    global xv, yv, pre_pause, paused
    key = evt.keyCode
    # 37 is left arrow key
    # 74 is j key
    if key == 74 and not paused:
        xv = -1
        yv = 0
    # 38 is up arrow key
    # 73 is i key
    elif key == 73 and not paused:
        xv = 0
        yv = -1
    # 39 is right arrow key
    # 76 is l key
    elif key == 76 and not paused:
        xv = 1
        yv = 0
    # 40 is down arrow key
    # 77 is m key
    elif key == 77 and not paused:
        xv = 0
        yv = 1
    # 32 is pause key
    # 80 is p key
    elif key == 80:
        temp = [xv, yv]
        xv = pre_pause[0]
        yv = pre_pause[1]
        pre_pause = [*temp]
        paused = not paused
   
def show_instructions(evt):
        window.alert("keys to control: i=up, m=down, j=left, l=right, p=pause")
       
# 利用 html 建立 canvas 超文件物件
canvas = html.CANVAS(width = 600, height = 600)
canvas.id = "game-board"
brython_div = doc["brython_div"]
brython_div <= canvas
   
score_doc = html.DIV("score")
score_doc.id = "score"
brython_div <= score_doc
   
high_score_doc = html.DIV("high-score")
high_score_doc.id = "high-score"
brython_div <= high_score_doc
   
button = html.BUTTON("Keys to control")
button.id = "instructions-btn"
brython_div <= button
   
score = 0
high_score = 0
   
px = py = 10
# gs*tc = canvas width and height
gs = 20
tc = 30
ax = ay = 15
xv = yv = 0
trail = []
tail = 5
   
pre_pause = [0,0]
paused = False
ctx = canvas.getContext("2d")
doc.addEventListener("keydown", key_push)
instructions_btn = doc["instructions-btn"]
instructions_btn.addEventListener("click", show_instructions)
browser.timer.set_interval(game, 1000/15)