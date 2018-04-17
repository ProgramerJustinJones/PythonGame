from gamelib import *
game = Game(1000, 900, "Archer Hero",3)
bk = Image("bk.png", game)
bk2 = Image("bk.png", game)


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
mage = Image("sorcerer.png",game,use_alpha=False)
Mhealth = Image("health.png",game,use_alpha=False)
fire = Image("fire.png",game)
fire2 = Image("fire.png",game)
boss1 = Image("Dragon.png",game)
boss1health = Image("health.png",game,use_alpha=False)
button = Image("button.png",game,use_alpha=False)






             

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
boss1health.resizeBy(-60)


x = randint(-1300,1400)
y = randint(-1300,1400)
knight.moveTo(x,y)
Earcher.moveTo(x,y)
mage.moveTo(x,y)
boss1.moveTo(x,y)
boss1.health = 1000

#Start Screen
game.over = False
while not game.over:
    game.processInput()

    
    bk.draw()
    button.draw()

    if button.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
    
    game.update(30)

game.over = False

    

game.over = False
game.setBackground(bk)
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
    boss1health.moveTo(boss1.x,boss1.y-150)
    health.moveTo(100,100)
    crosshair.moveTo(mouse.x,mouse.y)



        
    knight.moveTowards(hero,3)
    Earcher.moveTowards(hero,0)
    boss1.moveTowards(hero,0)
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
        
    if game.score >= 3 and game.score <= 10:
        Earcher.draw()
        Earcher.moveTowards(hero,2)
    if game.score >= 5 and game.score <= 10:
        mage.draw()
        mage.moveTowards(hero,2)
    if mouse.LeftClick:
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
 

    if game.time <=0:
        game.time +=4
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
        if game.score >=5:
            fire.draw()
            mark3.draw()
            mark3.visible = True
            mark3.moveTo(hero.x,hero.y)
            fire.moveTo(mage.x,mage.y)
            f = fire.angleTo(mark3)
            fire.rotateTo(f)
            fire.rotateTowards(mark3)
            fire.forward(8)
            fire.move()


 
                
                
            

        
    if fire.collidedWith(hero,"circle"):
        fire.moveTo(mage.x,mage.y)
        fire.visible is False

        

                     
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
    if mark3.visible is True:
        fire.angleTo(mark3)
        fire.forward(8)
        fire.move()

                     

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
    game.drawText("Dragon Health: " + str(boss1.health),boss1health.x-100,boss1health.y)

    if hero.health <=0:
        game.over = True
        hero.health = 0
    if Earcher.health <=0:
        x = randint(-1300,1400)
        y = randint(-1300,1400)
        Earcher.moveTo(x,y)
        Earcher.health +=100
        Ahealth.resizeTo(75,75)
        RP = randint(1,5)
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
        
    if fire.collidedWith(hero,"circle"):
        fire.moveTo(mage.x,mage.y)
        hero.health -=30
        health.resizeBy(-30)
        mark3.visible = False



    
        
    if mark.visible is False:
        arrow.moveTo(hero.x,hero.y)
        
    crosshair.draw()
    
    game.displayScore(health.x-30,health.y+85)  
    game.displayTime(5000,5000)
    game.update(60)
    
game.quit()
