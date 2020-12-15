# will hero
import pygame
import random
import time
pygame.init()
pygame.display.set_caption('will hero')
S=pygame.display.set_mode((800,600))
print('please dont push ctrl+c')

# defs
def max(A):
    m=A[0]
    for i in range(len(A)):
        if A[i]>m:
            m=A[i]
    return m
def helpplayer(S,coin,info,gamemusic,gndpics,helmet,myFont,orc,_quit,sky,skycolor,tower,towerlevel):
    bigFont=pygame.font.Font(None,100)
    n=0
    while True:
        # events
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                return -1
            if i.type==pygame.KEYDOWN:
                pass
            if i.type==pygame.MOUSEBUTTONDOWN:
                if (i.pos[0]-765)**2+(i.pos[1]-30)**2<625:
                    return 0
        # updates
        # draws
        S.fill((150,200,255))
        pygame.draw.rect(S,(255,255,255),(0,0,200,800))
        pygame.draw.line(S,(0,0,0),(200,0),(200,799))
        for i in range(12):
            text=myFont.render(['orc','tower','','','','','','','','','',''][i], True, (0,0,0))
            S.blit(text,(10,10+50*i))
            pygame.draw.line(S,(0,0,0),(0,50*(i+1)),(199,50*(i+1)))
        text=bigFont.render(['orc','tower','','','','','','','','','',''][n], True, (70,70,70))
        S.blit(text,(230,20))
        S.blit(_quit,(740,5))
        pygame.display.update()
def ouch(S,coin,info,gamemusic,gndpics,helmet,myFont,orc,_quit,sky,skycolor,tower,towerlevel):
    t0=time.time()
    dt=0
    pygame.mixer.Sound('ouch.ogg').play()
    while dt<2:
        # events
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return -1
        # updates
        t1=time.time()
        dt=t1-t0
        # draws
        pygame.display.update()
    gamemusic.stop()
    return 0
def play(S,coin,info,gamemusic,gndpics,helmet,myFont,orc,_quit,sky,skycolor,tower,towerlevel):
    def barkhord(v1,v2,size1,size2):
        m1=size1**2
        m2=size2**2
        v=(m1*v1+m2*v2)/(m1+m2)
        return(v+(v-v1)/3,v+(v-v2)/3)
    global best
    global coins
    effect_cape=0
    enities=[[1,240,300,0,20,350,0]]#type,x,y,vx,vy,y_knight,lvl_knight
    gamemusic.play()
    gnds=[0,0,-10,0,-10,0,0]
    gnd_modes=[2,1,-1,3,-1,2,0]
    lvl_knight_soon=0
    nfor=1
    ffor=0.0
    player_id=0
    sizes=(30,50)
    scr=0
    skytar=[0,170,255]
    x=240
    xgnd=0
    xscreen=0
    ygnd=0
    yscreen=0
    t0=time.time()
    tmusic=gamemusic.get_length()
    while True:
        # events
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                return -1
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_SPACE:
                    nfor=nfor+1
                    time.sleep(0.02)
                if i.key==pygame.K_s:
                    coins=coins+1000
                if i.key==pygame.K_q:
                    if scr>best:
                        best=scr
                    return 0
        # updates
        t1=time.time()
        dt=t1-t0
        t0=t1
        tmusic=tmusic-dt
        if tmusic<0:
            gamemusic.play()
            tmusic=gamemusic.get_length()
        if dt>0.1:
            dt=0.1
        effect_cape=effect_cape-250*dt
        if effect_cape<0:
            effect_cape=0
        i=0
        while i<len(enities):
            if enities[i][1]<-100 or enities[i][2]>600 or enities[i][1]>960+xgnd+160:
                if enities[i][0]==1:
                    if scr>best:
                        best=scr
                    gamemusic.stop()
                    return 3
                if i<player_id:
                    player_id=player_id-1
                enities.pop(i)
            else:
                for j in range(i):
                    if enities[i][1]<enities[j][1]:
                        a=enities[i]
                        enities[i]=enities[j]
                        enities[j]=a
                        if enities[i][0]==1:
                            player_id=i
                        if enities[j][0]==1:
                            player_id=j
                i=i+1
        for i in range(len(enities)):
            a=gnds[int((enities[i][1]-xgnd)/160)]
            enities[i][4]=enities[i][4]+150*dt
            enities[i][1]=enities[i][1]+enities[i][3]*dt
            enities[i][2]=enities[i][2]+enities[i][4]*dt
            if a!=-10 and enities[i][2]>enities[i][5] and enities[i][2]<=50+enities[i][5]:
                enities[i][4]=-150
            if a!=-10:
                enities[i][5]=enities[player_id][5]+sizes[0]-sizes[enities[i][0]-1]-50*a
            for j in range(i):
                a=enities[i][1]+sizes[enities[i][0]-1]>enities[j][1]
                a=a and enities[j][1]+sizes[enities[j][0]-1]>enities[i][1]
                a=a and enities[j][2]+sizes[enities[j][0]-1]>enities[i][2]
                if a and enities[i][2]+sizes[enities[i][0]-1]>enities[j][2]:
                    f1=2*enities[i][1]+sizes[enities[i][0]-1]>2*enities[j][1]+sizes[enities[j][0]-1]
                    f2=2*enities[i][2]+sizes[enities[i][0]-1]>2*enities[j][2]+sizes[enities[j][0]-1]
                    if f1:
                        a=enities[j][1]+sizes[enities[j][0]-1]-enities[i][1]
                    else:
                        a=enities[i][1]+sizes[enities[i][0]-1]-enities[j][1]
                    if f2:
                        b=enities[j][2]+sizes[enities[j][0]-1]-enities[i][2]
                    else:
                        b=enities[i][2]+sizes[enities[i][0]-1]-enities[j][2]
                    if a>b:
                        if f2 and i==player_id or not f2 and j==player_id:
                                return 3
                        enities[i][4],enities[j][4]=barkhord(enities[i][4],enities[j][4]
                                                             ,sizes[enities[i][0]-1],sizes[enities[j][0]-1])
                        if f2:
                            enities[i][2]=enities[i][2]+b/2
                            enities[j][2]=enities[j][2]-b/2
                        else:
                            enities[j][2]=enities[j][2]+b/2
                            enities[i][2]=enities[i][2]-b/2
                    else:
                        enities[i][3],enities[j][3]=barkhord(enities[i][3],enities[j][3]
                                                             ,sizes[enities[i][0]-1],sizes[enities[i][0]-1])
                        if f1:
                            enities[i][1]=enities[i][1]+a/2
                            enities[j][1]=enities[j][1]-a/2
                        else:
                            enities[j][1]=enities[j][1]+a/2
                            enities[i][1]=enities[i][1]-a/2
        while i<len(enities):
            if enities[i][1]<-100 or enities[i][2]>600 or enities[i][1]>960+xgnd+160:
                if enities[i][0]==1:
                    if scr>best:
                        best=scr
                    gamemusic.stop()
                    return 3
                if i<player_id:
                    player_id=player_id-1
                enities.pop(i)
            else:
                for j in range(i):
                    if enities[i][1]<enities[j][1]:
                        a=enities[i]
                        enities[i]=enities[j]
                        enities[j]=a
                        if enities[i][0]==1:
                            player_id=i
                        if enities[j][0]==1:
                            player_id=j
                i=i+1
        lvl_knight_here=0
        a=gnds[int((enities[player_id][1]-xgnd)/160)]
        if a!=-10:
            ygnd=ygnd-a*50
            lvl_knight_here=a
            enities[player_id][5]=enities[player_id][5]-50*a
        for i in range(7):
            if gnds[i]!=-10:
                gnds[i]=gnds[i]-lvl_knight_here
        if enities[player_id][2]>50+enities[player_id][5] and enities[player_id][4]<0:
            enities[player_id][4]=-enities[player_id][4]
        b=(enities[player_id][5]-350)*(1-0.85**dt)
        for i in range(len(enities)):
            enities[i][5]=enities[i][5]-b
        ygnd=ygnd-b
        for i in range(len(enities)):
            enities[i][2]=enities[i][2]-b
        yscreen=yscreen-b/20
        if ffor>0:
            a=7.5*dt
            if a>ffor:
                a=ffor
                enities[player_id][3]=enities[player_id][3]-600
            ffor=ffor-a
        if nfor>0 and ffor==0:
            nfor=nfor-1
            ffor=1.0
            enities[player_id][3]=600
            scr=scr+1
            if enities[player_id][2]<350:
                enities[player_id][2]=enities[player_id][2]-15
            if skycolor==skytar:
                skytar[2]=random.randint(150,255)
                skytar[0]=random.randint(50,skytar[2]*2//3)
                skytar[1]=random.randint(skytar[2]//4,skytar[2]*2//3)
            for i in range(3):
                if skycolor[i]<skytar[i]:
                    skycolor[i]=skycolor[i]+1
                if skycolor[i]>skytar[i]:
                    skycolor[i]=skycolor[i]-1
            effect_cape=70
        if gnds[6]!=-10:
            lvl_knight_soon=gnds[6]
        if enities[player_id][1]>240:
            a=100*(int(enities[player_id][1])-160)//80*dt
            for i in range(len(enities)):
                enities[i][1]=enities[i][1]-a
            xgnd=xgnd-a
            xscreen=xscreen-a/20
        if xgnd<-160:
            xgnd=xgnd+160
            gnds.pop(0)
            gnd_modes.pop(0)
            if gnds[5]!=-10:
                if random.randint(0,6)<=1:
                    gnds.append(gnds[5])
                    gnd_modes.append(0)
                else:
                    gnds.append(-10)
                    gnd_modes[5]=gnd_modes[5]+1
                    gnd_modes.append(-1)
            else:
                gnds.append(lvl_knight_soon+random.randint(-1,1))
                gnd_modes.append(2)
            if gnd_modes[-1]!=-1:
                enities.append([2,960+xgnd+random.randint(0,159),300+ygnd-50*gnds[-1],0,20,330+ygnd-50*gnds[-1],0])
        xscreen=xscreen%1000
        yscreen=yscreen%800
        # draws
        S.fill(skycolor)
        for i in range(-1,2):
            for j in range(-1,2):
                S.blit(sky,(xscreen+1000*i,yscreen+800*j))
        for i in range(len(enities)):
            a=[0,helmet,orc][(enities[i][0])]
            S.blit(a,(enities[i][1],enities[i][2]))
        pygame.draw.rect(S,(255,255,0),(enities[player_id][1]-effect_cape,enities[player_id][2]+5,effect_cape,20))
        for i in range(7):
            if gnds[i]!=-10:
                S.blit(gndpics[gnd_modes[i]],(160*i+xgnd,377-50*gnds[i]+ygnd))
        S.blit(myFont.render(str(scr),False,((128+skycolor[0])%256,(128+skycolor[1])%256,(128+skycolor[2])%256)),(400,0))
        pygame.display.update()
def ScreenGUI(S,coin,info,gamemusic,gndpics,helmet,myFont,orc,_quit,sky,skycolor,tower,towerlevel):
    global best
    global coins
    y=300
    vy=20
    t0=time.time()
    while True:
        # events
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                done=True
                return -1
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_SPACE:
                    return 1
                if i.key==pygame.K_s:
                    coins=coins+1000
            if i.type==pygame.MOUSEBUTTONDOWN:
                if (i.pos[0]-764)**2+(i.pos[1]-29)**2<577:
                    return 4
        # updates
        t1=time.time()
        dt=t1-t0
        t0=t1
        if dt>0.1:
            dt=0.1
        vy=vy+150*dt
        y=y+vy*dt
        if y>350:
            vy=-150
        textb=myFont.render('BEST '+str(best),True,(255,255,255))
        textc=myFont.render(str(coins),True,(255,255,255))
        # draws
        S.fill(skycolor)
        S.blit(sky,(0,0))
        S.blit(helmet,(240,y))
        for i in range(4):
            if i!=2:
                pygame.draw.rect(S,(255,150,0),(160*i,377,160,40))
        S.blit(textb,(0,40))
        S.blit(textc,(700,55))
        S.blit(coin,(650,45))
        S.blit(info,(740,5))
        pygame.display.update()
def shop(S,coin,info,gamemusic,gndpics,helmet,myFont,orc,_quit,sky,skycolor,tower,towerlevel):
    tower1=pygame.transform.scale(tower,(100,100))
    tower2=pygame.transform.scale(tower,(200,200))
    bigFont=pygame.font.Font(None,50)
    hugeFont=pygame.font.Font(None,60)
    f=0
    while True:
        # events
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                return -1
            if i.type==pygame.MOUSEBUTTONDOWN:
                if (i.pos[0]-765)**2+(i.pos[1]-30)**2<625:
                    return 0
                if i.pos[0]>=10 and i.pos[0]<190 and i.pos[1]>=430 and i.pos[1]<482:
                    print('upgrade')
        # updates
        if f==0:#tower
            pic=tower2
            text='towerlevel'
        text=bigFont.render(text,True,(220,220,220))
        text3=hugeFont.render('upgrade',True,(0,0,0))
        # draws
        S.fill((127,212,255))
        pygame.draw.rect(S,(25,55,76),(0,0,200,600))
        S.blit(pic,(0,0))
        S.blit(text,(10,200))
        S.blit(_quit,(740,5))
        S.blit(tower1,(300,100))
        pygame.draw.rect(S,(70,60,51),(10,430,180,52))
        S.blit(text3,(15,432))
        pygame.display.update()
    return 3

# variables
data=open('data.txt')
best=int(data.readline()[:-1])
coin=pygame.image.load('coin.png')
coins=int(data.readline()[:-1])
towerlevel=int(data.readline()[:-1])
data.close()
gamemusic=pygame.mixer.Sound('music.ogg')
gndpics=[]
for i in range(1,5):
    gndpics.append(pygame.image.load('gnd'+str(i)+'.png'))
info=pygame.image.load('info.png')
helmets=[]
for i in['chicken']:
    helmets.append(pygame.image.load(i+'.png'))
helmn=0
mainloops=[ScreenGUI,play,shop,ouch,helpplayer]
myFont=pygame.font.Font(None,40)
orc=pygame.image.load('orc.png')
_quit=pygame.image.load('quit.png')
sky=pygame.image.load('sky2.png')
skycolor=[0,170,255]
tower=pygame.image.load('tower.png')

# main loop
condition=0
while condition!=-1:
    condition=mainloops[condition](S,coin,info,gamemusic,gndpics,helmets[helmn],myFont,orc,_quit,sky,skycolor,tower,towerlevel)
data=open('data.txt','w')
data.write(str(best)+'\n'+str(coins)+'\n'+str(towerlevel)+'\n')
data.close()
pygame.quit()
