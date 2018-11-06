import random
import sys

escape=False
enemy=False
eturn=False
turn=False
inventory = []
action=0
phealth=100
ferralAdvhealth=80
#ferralAdv is Ferral Adventurer 

class player(object):
    def __init__(self, health, name):
         self.health = phealth
         self.name = name
class sword(object):
    def __init__(self, name, damage=10):
         self.name = 'Sword'
         self.damage = damage
class hammer(object):
    def __init__(self, name, damage=10):
         self.name = 'War Hammer'
         self.damage = damage
class staff(object):
    def __init__(self, name, damage=10):
         self.name = 'Staff of Flames'
         self.damage = damage
class ferralAd(object):
    def __init__(self, health, name):
         self.health = phealth
         self.name = foe1

#battle:
#This is the Player's turn:
while enemy==True and eturn==False:
    turn==True
    while turn==True:
        print(bops)
        move=input('')
        if move=='s':
            print ('(You strike the'+foe1+'with your'+primary+'!)')
            print ('('+foe1+'took 20 damage,'+foe1+'has',ferralAdvhealth,'HP left!)')
            input('')
            ferralAdvhealth-20
            eturn==True
            turn==False
        elif move=='r' and escape==False:
            print (nrun)
            input('')
            eturn==True
            turn==False
        elif move=='r' and escape==True:
            print('(You got away)')
            input('')
        elif phealth<=0:
            print ('('+name+'has been defeated')
            input ('')
            print ('try again')
            input ('')
            sys.exit()
            enemy==False
        break
#This is the enemy's turn:
while enemy==True and eturn==True:
    if ferralAdvhealth>0:
        print (+foe1+'Attacks you with his claws')
        phealth-20
        print ('(You took 20 damage, you have',phealth,'HP left!)')
        input('')
        eturn==False
    elif ferralAdvhealth<=0:
        print ('('+foe1+'has been defeated!)')
        escape=False
        enemy=False
        eturn=False
        turn=False
    break

bops='(To attack your opponet hit s.  To try to run away press r.)'
#Battle controls
nrun='(you got away).'
#nrun states why you can't run away from the battle
print ('?: Oh no! It seems you are trapped in a dark and scary maze!!!')
print ('??: NOOOOOOOOOOOOOO!')
print ('Press enter to start!(hint: press enter to progress dialog)')
input ('')
print ('?: Hi, I am Paul, I woke up one day trapped in this cave, just like you.')
print ('And I had to play this horrible game, just like you.')
input ('')
print ('Paul: I died here, and my spirit is cursed to forever roam these caverns.')
print ('But I might just be able to break the curse if I guide someone out of this cave alive')
input ('')
print ('Paul: Many have tried to get out, none have succeeded.')
print ('But I was the first...')
print ('The first failure.')
input ('')
action=action+1
while action==1:
    print ('So, what is your name?')
    name=input('')
    if name=='':
        action=action+0
    else:
        action=action-1
print ('Paul: Well then '+name+' it seems we have a long-')
print ('?:*reeeeeeeeee*')
input ('')
print (''+name+': What was that?!')
input ('')
print ('We have to go, Now!')
input ('')
print ('...')
input ('')
print ('...')
input ('')
print ('Paul: No no no no no! Dead end!')
input ('')
print ('Its too dark in here to see anything, pick up that lumber and strike it against the cavern wall to make a fire!')
print ('[lumber added to inventory]')
inventory.append('lumber')
input ('')
action=action+1
while action==1:
    print ('(hint: press s and hit enter to strike)')
    strike=input('')
    if strike=='s':
        action=action-1
        print ('Paul: Good, we can see...')
    else:
        action=action+0
inventory.remove('lumber')
inventory.append('torch')
print ('[Lumber removed from inventory]')
print ('[Torch added]')
input ('')
print ('...')
input('')
print ('Narrator: You look down only to realize you have been standing on a pile bones.')
print ('Paul: GAH!!!')
input ('')
print ('Paul: Sorry, it startles me every time. Sometimes people are luckey enough to wake up in the cave with weapons, maybe you can find some.')
print ('Narrator: you dig through the bones until you find a long sword, a war hammer, and a strange looking stick.')
print ('?:*reeeeeeeee*')
print ("Paul: It's coming!")
print ('Hurry, pick a weapon!')
print ('Narrator: You notice that behind you are, what appears to be, three different passage ways...')
input ('')
print ('Each of which are blocked.')
print ("Paul: What are you staring at?  It's getting closer!")
print ('Narrator: Will you choose the sword and cut your enemies down one by one?(press 1)')
print ('Or maybe you will choose the war hammer and beat in their skulls?(press 2)')
print ('Or I guess you could choose that weird stick if you really wanted too...(press 3)')
while True:
    choice=input('')
    if choice=='1':
        primary = 'sword'
        print ('[Sword added]')
        inventory.append('sword')

    elif choice=='2':
        primary = 'hammer'
        print ('[War Hammer added]')
        inventory.append('hammer')

    elif choice=='3':
        primary = 'staff'
        print ('[Staff of Flames added]')
        inventory.append('Staff of Flames')

    break

print ("Paul: It's here... ")
input ('')
print ("Paul: He's here!!")
input ('')
print("""                              
                              ________      
                           __/        \__
			   \|  - __ -  |/
			     \  (  )  /
		       _______\______/_______
		      (     _____  _____     )			     		      
		      |	 | |  .  ||  .  | |  |
		      |	 | |_____||_____| |  |
		      |  | \  |__||__|  / |  |
		      |  |  \ |__||__| /  |  |
		      |  |  | |__||__| |  |  |
		      |  |  |__________|  |  |
		     ////\ /   |    |   \ /\\\\\\\\
		    ////  /   /|    |\   \  \\\\\\\\	   
			  \   \|/\/\|/   / 
			   \   \    /   /
                            \/\/    \/\/\
""")
print ('(FERRAL ADVENTURER has appeared!)')
input('')
enemy=True
escape=True
nrun="Paul: What are doing!  Can't you see we're cornered?!"
foe1='FERRAL ADVENTURER'


print ('Paul: Yeet')
input('')
