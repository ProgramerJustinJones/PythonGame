from gamelib import *
game = Game(1000, 900, "Archer Hero",3)
bk = Image("bk.png", game)
game.setBackground(bk)

arrow2 = Image("arrow.png",game,use_alpha=False)
mark2 = Image("crosshair.png",game,use_alpha=False)
arrow = Image("arrow.png",game,use_alpha=False)
mark = Image("crosshair.png",game,use_alpha=False)
crosshair = Image("crosshair.png",game,use_alpha=False)
hero = Image("archer.png",game,use_alpha=False)
knight = Image("knight.png",game,use_alpha=False)
health = Image("health.png",game,use_alpha=False)
Earcher = Image("Earcher.png",game,use_alpha=False)

bk.resizeTo(1000,900)
Earcher.resizeBy(-60)
arrow.resizeBy(-50)
arrow2.resizeBy(-60)
mark2.resizeBy(-99)
mark.resizeBy(-99)
crosshair.resizeBy(-30)
hero.resizeBy(-50)
knight.resizeBy(-60)
health.resizeBy(0)

knight.moveTo(800,800)
Earcher.moveTo(700,700)

while not game.over:
    game.processInput()
    mouse.visible = False
    bk.draw()
    health.draw()
    Earcher.draw()
    hero.draw()
    knight.draw()
    crosshair.draw()
    
    health.moveTo(100,100)
    crosshair.moveTo(mouse.x,mouse.y)
    Earcher.move(bounce = True)
        
    arrow2.rotateTowards(mark2)
    knight.moveTowards(hero,2)

    Earcher.setSpeed(4,240)

    arrow.speed +=10
    
    if keys.Pressed[K_w] or keys.Pressed[K_UP]:
        hero.y -=4
    if keys.Pressed[K_a] or keys.Pressed[K_LEFT]:
        hero.x -=4
    if keys.Pressed[K_s] or keys.Pressed[K_DOWN]:
        hero.y +=4
    if keys.Pressed[K_d] or keys.Pressed[K_RIGHT]:
        hero.x +=4

    if mouse.LeftClick:
        arrow.draw()
        mark.draw()      
        mark.visible = True
        arrow.moveTo(hero.x,hero.y)
        mark.moveTo(mouse.x,mouse.y)
        a = arrow.angleTo(mark)
        arrow.rotateTo(a)
        arrow.rotateTowards(mark)
        arrow.forward(20)
        arrow.move()

        
    if game.time <= 0:
        arrow2.draw()
        mark2.draw()
        mark2.visible = True
        mark2.moveTo(hero.x,hero.y)
        arrow2.moveTo(Earcher.x,Earcher.y)
        game.time +=4
                     
    if arrow2.collidedWith(hero):
       arrow2.moveTo(Earcher.x,Earcher.y)
       arrow2.visible is False
       
    if mark2.collidedWith(arrow2):
        mark2.visible = False

    
        

        
    if mark.visible is True:
        arrow.angleTo(mark)
        arrow.move()
        arrow.forward(4)
        
    if mark2.visible is True:    
        arrow2.moveTowards(mark2,5)

    if knight.collidedWith(hero,"rectangle"):
        health.resizeBy(-10)
        hero.health -=10
        x = randint(1000,1200)
        y = randint(900,1100)
        knight.moveTo(x,y)
        
    if Earcher.collidedWith(hero,"rectangle"):
        health.resizeBy(-5)
        hero.health -=5
        x = randint(0,1000)
        y = randint(0,900)
        Earcher.moveTo(x,y)
        
    if Earcher.collidedWith(arrow):
        x = randint(0,1000)
        y = randint(0,900)
        Earcher.moveTo(x,y)
        mark.visible = False
        
    game.drawText("Health: " + str(hero.health),65,90)

    if hero.health <=0:
        game.over = True
        hero.health = 0
        
    if arrow.collidedWith(knight):
       x = randint(0,1000)
       y = randint(0,900)
       knight.moveTo(x,y)
       mark.visible = False
    
    if arrow2.collidedWith(hero,"rectangle"):
        arrow2.moveTo(Earcher.x,Earcher.y)
        hero.health -=20
        health.resizeBy(-20)
        mark2.visible = False
        
    if mark.visible is False:
        arrow.moveTo(hero.x,hero.y)
        
    game.displayTime(5000,5000)
    game.update(60)
    
game.quit()
