from gamelib import *
game = Game(800, 600, "Archer Hero",3)
bk = Image("bk.png", game)
bk2 = Image("bk.png", game)
game.setMusic("music.mp3")
game.playMusic()


arrow2 = Image("arrow.png",game,use_alpha=False)
mark2 = Image("crosshair.png",game,use_alpha=False)
mark3 = Image("crosshair.png",game,use_alpha=False)
mark4 = Image("crosshair.png",game,use_alpha=False)
arrow = Image("arrow.png",game,use_alpha=False)
mark = Image("crosshair.png",game,use_alpha=False)
crosshair = Image("crosshair.png",game,use_alpha=False)
hero = Image("archer.png",game,use_alpha=False)
knight = Image("knight.png",game,use_alpha=False)
health = Image("health.png",game,use_alpha=False)
Khealth = Image("health.png",game,use_alpha=False)
Ahealth = Image("health.png",game,use_alpha=False)
Earcher = Image("Earcher.png",game,use_alpha=False)
mage = Image("mage.png",game,use_alpha=False)
Mhealth = Image("health.png",game,use_alpha=False)
title = Image("title.png",game,use_alpha=False)
fire = Image("fire.png",game)
fire2 = Image("fire.png",game)
button = Image("button.png",game,use_alpha=False)
start = Image("start.png",game,use_alpha=False)




bowshoot=Sound("bowshoot.ogg",1)







             

bk.resizeTo(1000,900)
Earcher.resizeBy(-60)
mage.resizeBy(-60)
arrow.resizeBy(-50)
arrow2.resizeBy(-60)
mark2.resizeBy(-99)
mark3.resizeBy(-99)
mark4.resizeBy(-99)
mark.resizeBy(-99)
fire.resizeBy(-90)
fire2.resizeBy(-95)
crosshair.resizeBy(-70)
hero.resizeBy(-50)
knight.resizeBy(-60)
health.resizeBy(-50)
Ahealth.resizeBy(-80)
Khealth.resizeBy(-80)
Mhealth.resizeBy(-80)
start.resizeBy(-50)




x = randint(-1300,1400)
y = randint(-1300,1400)
knight.moveTo(x,y)
Earcher.moveTo(x,y)
mage.moveTo(x,y)



#Start Screen
game.over = False
while not game.over:
    game.processInput()

    title.moveTo(button.x,button.y-160)
    bk.draw()
    button.draw()
    title.draw()
    f = Font(black,25,black,"Comic Sans MS")
    game.drawText("Use the Arrow Keys to Move!Use your mouse to aim and left click to shoot!",75,870,f)


    if button.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
    
    game.update(60)

game.over = False
#start.moveTo()
start.moveTo(start.x,start.y+200)
while not game.over:
    game.processInput()
    bk.draw()
    
    game.drawText("You are a magical archer! You have been injured in a war.",80,100,f)
    game.drawText("The rest of your army abandond you and retreated without",80,125,f)
    game.drawText("you. You wake up after passing out from the injury you were",80,150,f)
    game.drawText("given throughout the war. Now that your wounds are healed",80,175,f)
    game.drawText("The enemy has noticed you and are sending small groups of",80,200,f)
    game.drawText("their forces in your direction. You must survive as long as",80,225,f)
    game.drawText("you can until your army notices you,and rescues you",80,250,f)
    start.draw()
    
    if start.collidedWith(mouse) and mouse.LeftClick:
        game.over = True

    

    game.update(60)
    



game.over = False
game.setBackground(bk)
x = randint(-1300,1400)
y = randint(-1300,1400)

knight.moveTo(x,y)
mage.moveTo(x,y)
Earcher.moveTo(x,y)
hero.health +=30
health.resizeBy(30)
arrow.visible = False
while not game.over:
    game.processInput()
    mouse.visible = False
    bk.draw()
    health.draw()
    hero.draw()
    knight.draw()
    Khealth.draw()
    Ahealth.draw()
    Khealth.moveTo(knight.x,knight.y-90)
    Ahealth.moveTo(Earcher.x,Earcher.y-90)
    Mhealth.moveTo(mage.x,mage.y-90)
    health.moveTo(100,100)
    crosshair.moveTo(mouse.x,mouse.y)

        
    knight.moveTowards(hero,3)
    Earcher.moveTowards(hero,0)
    mage.moveTowards(hero,0)
    arrow.speed +=5
    arrow2.speed -=150
    
    if keys.Pressed[K_w] or keys.Pressed[K_UP]:
        hero.y -=4
    if keys.Pressed[K_a] or keys.Pressed[K_LEFT]:
        hero.x -=4
    if keys.Pressed[K_s] or keys.Pressed[K_DOWN]:
        hero.y +=4
    if keys.Pressed[K_d] or keys.Pressed[K_RIGHT]:
        hero.x +=4
        
    if game.score >= 3:
        Earcher.draw()
        Earcher.moveTowards(hero,2)
    if game.score >= 5:
        mage.draw()
        mage.moveTowards(hero,2)
    if mouse.LeftClick:
        bowshoot.play()
        arrow.draw()
        mark.draw()      
        mark.visible = True
        arrow.visible = True
        arrow.moveTo(hero.x,hero.y)
        mark.moveTo(mouse.x,mouse.y)
        a = arrow.angleTo(mark)
        arrow.rotateTo(a)
        arrow.rotateTowards(mark)
        arrow.forward(20)
        arrow.move()

        
    if game.time <= 0 and game.score >=3:
        arrow2.draw()
        mark2.draw()
        mark2.visible = True
        mark2.moveTo(hero.x,hero.y)
        arrow2.moveTo(Earcher.x,Earcher.y)
        a2 = arrow2.angleTo(mark2)
        arrow2.rotateTo(a2)
        arrow2.rotateTowards(mark2)
        arrow2.forward(4)
        arrow2.move()
        game.time +=4
    if game.score >=5:
        fire.draw()
        fire.visible = True
        fire.moveTowards(hero,3)
        fire.rotateTowards(hero)

        

        
    if fire.collidedWith(hero,"circle"):
        fire.moveTo(mage.x,mage.y)
        fire.visible is False
        hero.health -=30
        health.resizeBy(-30)
                     
    if arrow2.collidedWith(hero,"circle"):
       arrow2.moveTo(Earcher.x,Earcher.y)
       arrow2.visible is False
       
    if mark.visible is True:
        arrow.angleTo(mark)
        arrow.move()
        arrow.forward(4)
    if mark.visible is False:
        arrow.visible = False
        
    if mark2.visible is True:    
        arrow2.angleTo(mark2)
        arrow2.forward(7)
        arrow2.move()

    if fire.collidedWith(arrow,"circle"):
        fire.moveTo(mage.x,mage.y)
        fire.visible = False

                     

    if knight.collidedWith(hero,"rectangle"):
        health.resizeBy(-10)
        hero.health -=10
        x = randint(-1300,1400)
        y = randint(-1300,1400)
        knight.moveTo(x,y)
    if mage.collidedWith(hero,"rectangle"):
        health.resizeBy(-30)
        hero.health -=30
        x = randint(-1300,1400)
        y = randint(-1300,1400)
        mage.moveTo(x,y)
    if mage.collidedWith(arrow):
        mage.health -=20
        Mhealth.resizeBy(-20)
        mark.visible = False

    if mage.health <=0:
        x = randint(-1300,1400)
        y = randint(-1300,1400)
        mage.moveTo(x,y)
        mage.health += 100
        Mhealth.resizeTo(75,75)
        game.score +=1
        
        
        
        
    if Earcher.collidedWith(hero,"rectangle"):
        health.resizeBy(-5)
        hero.health -=5
        x = randint(-1300,1400)
        y = randint(-1300,1400)
        Earcher.moveTo(x,y)
        
    if Earcher.collidedWith(arrow):
        Earcher.health -=20
        Ahealth.resizeBy(-20)
        
        mark.visible = False
        
    game.drawText("Health: " + str(hero.health),55,90)

    if hero.health <=0:
        Earcher.visible = False
        mage.visible = False
        knight.visible = False
        arrow2.visible = False
        fire.visible = False
        game.wait(K_SPACE)

        game.over = True
        hero.health = 0
    if Earcher.health <=0:
        x = randint(-1300,1400)
        y = randint(-1300,1400)
        Earcher.moveTo(x,y)
        Earcher.health +=100
        Ahealth.resizeTo(75,75)
        game.score +=1
        
    if knight.health <=0:
        x = randint(-1300,1400)
        y = randint(-1300,1400)
        knight.moveTo(x,y)
        knight.health +=100
        Khealth.resizeTo(75,75)
        game.score +=1
        
    if arrow.collidedWith(knight):
        knight.health -=15
        Khealth.resizeBy(-15)
        mark.visible = False
    
    if arrow2.collidedWith(hero,"circle"):
        arrow2.moveTo(Earcher.x,Earcher.y)
        hero.health -=20
        health.resizeBy(-20)
        mark2.visible = False
        
    if mark.visible is False:
        arrow.moveTo(hero.x,hero.y)
        
    crosshair.draw()
    
    game.displayScore(health.x-30,health.y+75)  
    game.displayTime(5000,5000)
    game.update(60)

    
    
game.quit()
    
game.quit()
game.update(60)
    
game.quit()



