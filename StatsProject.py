_author_ = 'ArmanT & CristianF'

import tkinter as tk
#from tkinter import font
import random
# import pyglet
# from threading import Thread

def center(root):
    root.update_idletasks()
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    size = tuple(int(_) for _ in root.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    root.geometry("%dx%d+%d+%d" % (size + (x, y)))

def randomizeColor(): #color, mainBg, mainWindow
    color = "#%06x" % random.randint(0x707070, 0xFFFFFF)
    label.config(bg=color)
    root.config(bg=color)
    instructions.config(bg=color)
    credits.config(bg=color)

def flowchart(answer):
    randomizeColor()
    randomizePicture()
    if answer == "I\'m ready!" or answer == "Restart":
        label.config(text="You are a man by the name of Allan Valerio. You are a math teacher by day,"
                          "\nand an adventurer by night (though it's day right now)."
                          "\nYou're at what seems to be a broken bridge over a deep and treacherous river."
                          "\nWhat do you do?", font="default 20")
        firstButton.config(text='Attempt to cross (failure rate = 65%)')
        secondButton.pack(side="bottom", fill="both")
        firstButton.pack_forget()
        firstButton.pack(side="bottom", fill='both')
        label.pack_forget()
        label.pack(side="bottom")
        secondButton.config(text='Wade the water (failure rate = 75%)')
    elif answer == "Attempt to cross (failure rate = 65%)":
        label.config(text="You are successful."
                          "\nYou walk a short distance until you arrive at a large castle at the edge"
                          "\nof what looks to be a humble village."
                          "\nYou see the king walking around for some reason."
                          "\nIt seems like he needs help with reading some map."
                          "\nWhat do you do?")
        firstButton.config(text="Attempt to read the thing yourself")
        secondButton.config(text="Find someone who can read it")
    elif answer == "Wade the water (failure rate = 75%)":
        label.config(text="You fail."
                          "\nAs you're tumbling through the river, you look for something you can grab.")
        firstButton.config(text="Grab a branch! (failure rate = 20%)")
        secondButton.config(text="Grab a log! (failure rate = 65%)")
    elif answer == "Grab a branch! (failure rate = 20%)":
        label.config(text="You grab onto the branch and hoist yourself up onto the land."
                          "\nYou see a huge forest in front of you"
                          "\nJust before you're able to feel at peace with the beautiful forest"
                          "\nyou hear some scary rustling that sound surprisingly like a vicious pie chart"
                          "\n(which is odd because you're not supposed to know what abstract ideas"
                          "\nsound like)"
                          "\nWhat do you do?")
        firstButton.config(text="Run away!")
        secondButton.config(text="Hide")
    elif answer == "Run away!":
        label.config(text="You start dodging and weaving through the trees in the forest, in attempt"
                          "\nto run away from the scary, scary sound"
                          "\nUnfortunately, the rustling sound gets closer and closer"
                          "\nWhat do you do?")
        firstButton.config(text="Keep running")
        secondButton.config(text="Stop")
    elif answer == "Hide":
        label.config(text="You decide to lie down in some large bushes near a tree, and stay as still"
                          "\nas possible.")
        firstButton.config(text="Continue......")
        secondButton.config(text="Continue......")
    elif answer == "Keep running":
        label.config(text="You are able to finally outrun the rustling sounds, and you end up running"
                          "\nso far through the forest that you end up in a town."
                          "\nYou have reason to believe that this is the town in which you were"
                          "\nsent in the first place to take a census in."
                          "\nYou pull out the question sheet out of your inventory but it is soaked")
        firstButton.config(text="Continue....")
        secondButton.config(text="Continue....")
    elif answer == "Stop":
        label.config(text="You summon up the courage to stop and wait for the rustling to come."
                          "\nIt gets closer and closer, and you see a shadowy figure darting through"
                          "\nthe trees."
                          "\nTo your amazing surprise, it's your neighbor, St. Dev. He embraces you"
                          "\nwith great joy.")
        firstButton.config(text="Continue.....")
        secondButton.config(text="Continue.....")
    elif answer == "Continue......":
        label.config(text="\nThe sound gets closer and closer, and you see a shadowy figure darting through"
                          "\nthe trees."
                          "\nTo your amazing surprise, it's your neighbor, St. Dev. He embraces you"
                          "\nwith great joy.")
        firstButton.config(text="Continue.....")
        secondButton.config(text="Continue.....")
    elif answer == "Continue.....":
        label.config(text="St. Dev says, \"Where've you been?! The whole town thought you were dead!\""
                          "\nI'm going to take you home before you get hurt or something, because"
                          "\nthere's a standard deviation of 1 in the chance of dead here with a"
                          "\nmean of 0.99"
                          "\nSo your kind neighbor takes you home, and you have some cookies"
                          "\nGAME OVER.")
        firstButton.config(text="Restart")
        secondButton.config(text="Restart")
    elif answer == "Continue....":
        label.config(text="You have a 95% confidence interval that you remember the questions correctly"
                          "\nWhat do you do?")
        firstButton.config(text="Conduct the survey")
        secondButton.config(text="Go back home")
    elif answer == "Go back home":
        label.config(text="You go back home, thinking that you've had enough fun for today."
                          "\nGAME OVER.")
        firstButton.config(text="Restart")
        secondButton.config(text="Restart")
    elif answer == "Conduct the survey":
        label.config(text="You ask every single person in the town the set of questions from memory."
                          "\nHowever, since you have nothing to write the answers on, it is completely"
                          "\nuseless since you forget everything answered."
                          "\nYou find your way back home, fruitless."
                          "\nGAME OVER.")
        firstButton.config(text="Restart")
        secondButton.config(text="Restart")
    elif answer == "Grab a log! (failure rate = 65%)":
        label.config(text="You manage to actually grab onto the log."
                          "\nUnfortunately, even though you appallingly ignored the high failure rate "
                          "\ntwice in a row, the log dislodges itself from the river bed and starts"
                          "\nfloating down the stream with you still on it. It goes all the way until"
                          "\nthe ocean.")
        firstButton.config(text="Continue.")
        secondButton.config(text="Continue.")
    elif answer == "Continue.":
        label.config(text="Once you finally arrive at the Sea of Scatterplot Points, still hanging on"
                          "\nfor dear life on the log, the current drags you far, far away."
                          "\nEventually you arrive at some mysterious, uncharted island."
                          "\nThe first thing you see is some weird old man on the shore."
                          "\nWhat do you do?")
        firstButton.config(text="Be friendly")
        secondButton.config(text="Be aggressive")
    elif answer == "Be friendly":
        label.config(text="You say, \"Hello, sir! I need some help, and you seem like a nice guy. "
                          "\nWhat's going on here?\""
                          "\nThe man doesn't seem to understand your words, but he realizes that"
                          "\nyou are indeed someone special (you aren't really)"
                          "\nSlowly, other people start coming out from the shadows to see what is happening"
                          "\nWhat do you do?")
        firstButton.config(text="Still be friendly")
        secondButton.config(text="Be aggressive")
    elif answer == "Be aggressive":
        label.config(text="You start cussing out the man, and being general belligerent."
                          "\nSuddenly, swaths and swarms of people emerge from the shadows."
                          "\nThey take you by force and tie a long rope around your arms."
                          "\nThey drag you over a pit, which seems to be full of the rare"
                          "\nbut insanely deadly boxplot variety of pythons")
        firstButton.config(text="Continue...")
        secondButton.config(text="Continue...")
    elif answer == "Continue...":
        label.config(text="Soon after you accept your demise, you hear the distinct whizzing of a"
                          "\nresidual plot fly by and cut you from the rope before they push you in."
                          "\nHowever, you are unlucky and end up falling in and dying anyway.")
        firstButton.config(text="Restart")
        secondButton.config(text="Restart")
    elif answer == "Still be friendly":
        label.config(text="The man approaches you and says in some weird tongue that sounds kind"
                          "\nof like Greek mixed in with numbers. You're not sure what he means."
                          "\nHe takes hold of your arm and takes you further into the island to"
                          "\nwhat looks like a long-lost ancient civilization"
                          "\nYou suddenly remember reading about this place during your childhood"
                          "\n\"The Ancient Civilization of Bargraphia\"")
        firstButton.config(text="Continue..")
        secondButton.config(text="Continue..")
    elif answer == "Continue..":
        label.config(text="You try talking to the man again, and he suddenly starts speaking"
                          "\nnormal English. The ancient Bargraphian tongue was just for show, apparently"
                          "\nHe tells you that his civilization has been at war with the disgusting"
                          "\nScatterplotonians for several hundred years, and you need to help them"
                          "\nWhat do you do?")
        firstButton.config(text="Help out")
        secondButton.config(text="Politely decline and ask how to get home")
    elif answer == "Politely decline and ask how to get home":
        label.config(text="The man is appalled and tells you that you are now a Bargraphian."
                          "\nThere is no going back, and he is ashamed that you would shun"
                          "\ntheir honor. He forces you to a squadron of nooby Bargraphians"
                          "\nDays later, when the day of battle comes, you are lead to a"
                          "\nplane, in which you are killed."
                          "\nGAME OVER.")
        firstButton.config(text="Restart")
        secondButton.config(text="Restart")
    elif answer == "Help out":
        label.config(text="You decide to help out, because you're in it for the money."
                          "\nThe man, whose name he has revealed to you is Alkimachos, says that"
                          "\nyou must assassinate the emperor of Scatterplotonia in order to"
                          "\nput an end to the madness. Naturally, you arm yourself to the"
                          "\nteeth. Neat enough, the swords are shaped like bar graphs."
                          "\nWhat do you do?")
        firstButton.config(text="Go infiltrate before the battle begins")
        secondButton.config(text="Wait for battle, then rush the emperor")
    elif answer == "Go infiltrate before the battle begins":
        label.config(text="You decide to crouch behind a wall in the leader's castle in the kitchen,"
                          "\nhidden in the shadows. You have a random sample of n=20 poisons to "
                          "\nkill the leader with."
                          "\nYou find his study, and slip some poison into his foodsnacks"
                          "\nWhile rummaging around, you find some files with slope lines"
                          "\nof the economy, complete with linear regression."
                          "\nYou also find plans of wanted to conquer and pillage Bargraphia")
        firstButton.config(text="Continue.......")
        secondButton.config(text="Continue.......")
    elif answer == "Continue.......":
        label.config(text="After doing your espionage and assassination mission, you manage"
                          "\nto escape quickly and silently, back to Alkimachos."
                          "\nAfter a few hours, you hear that the great emperor of the"
                          "\nScatterplotonian empire is no more. You are triumphant."
                          "\nHaving done the job, the Bargraphians give you lavish, rare"
                          "\ngifts and send you back home. You live the rest of your days"
                          "\nrich and carefree."
                          "\nGAME OVER.")
        firstButton.config(text="Restart")
        secondButton.config(text="Restart")
    elif answer == "Wait for battle, then rush the emperor":
        label.config(text="You await battle for several days."
                          "\nThe day finally comes, and you see the emperor in the distance."
                          "\nHowever, the odds are not in your favor (your null hypothesis is"
                          "\nrejected) and you get stabbed through the heart and die.")
        firstButton.config(text="Restart")
        secondButton.config(text="Restart")
    elif answer == "Attempt to read the thing yourself":
        label.config(text="You are a peasant. You cannot read."
                          "\nThat is why you failed the AP Stats exam."
                          "\nWhat do you do?")
        firstButton.config(text="Make something up")
        secondButton.config(text="Admit you can't read")
    elif answer == "Make something up":
        label.config(text="You tell the king that some mountain that you RANDOMLY SELECTED"
                          "\nFROM THE POPULATION OF ALL MOUNTAINS IN THIS AREA has the treasure."
                          "\n(i.e. you just pointed to some mountain in the distance)"
                          "\nHe tells you to go the mountain (with a guard) to retrieve it, so you do that."
                          "\nYou, of course, find nothing.")
        firstButton.config(text="Continue")
        secondButton.config(text="Continue")
    elif answer == "Continue":
        label.config(text="The guard who came with you tells you, \"I hope you know what lying"
                          "\nis a treasonous offense, and we're going to have to send you back"
                          "\nto the king to be executed.\""
                          "\nThe thought of death terrifies you."
                          "\nWhat do you do?")
        firstButton.config(text="Run away")
        secondButton.config(text="Concede and go back")
    elif answer == "Run away":
        label.config(text="You estimate with a normal distribution that you have a mean of 3 minutes"
                          "\nhead start to get a way with a 20 second standard deviation. You know that"
                          "\neach kingdom in your land is equipped with highly skilled Scatterplotonians"
                          "\nwho serve as an army of mercenaries."
                          "\nWhat do you do?")
        firstButton.config(text="Hide in the nearby Bargraphian ruins")
        secondButton.config(text="Try to outrun the Scatterplotonians")
    elif answer == "Try to outrun the Scatterplotonians":
        label.config(text="The Scatterplotonians are able to easily catch up with you, since you are"
                          "\nvery out of shape. They rip you apart and eat you alive."
                          "\nGAME OVER.")
        firstButton.config(text="Restart")
        secondButton.config(text="Restart")
    elif answer == "Hide in the nearby Bargraphian ruins":
        label.config(text="While hiding behind a statue of a nice approximately normal distribution"
                          "\ngraph, you notice carvings of the holy Old Axis all over the ruins."
                          "\nYou find this enticing to learn about, so you enter deeper into to"
                          "\nthe place since you managed to evade the Scatterplotonians"
                          "\nSeeing the beautiful architecture, you spot what looks like a fork"
                          "\nbetween a tomb and a treasure room")
        firstButton.config(text="Investigate the tomb")
        secondButton.config(text="Pilfer the treasure room")
    elif answer == "Investigate the tomb":
        label.config(text="You enter the tomb, and find some ancient tombs regarding the holy"
                          "\nsubjects of bar graphs, axes, and the even older Box-and-Whisker"
                          "\ncivilization."
                          "\nYou manage to leave the ruins safely with your nice tomes and"
                          "\ntons of valuable new knowledge."
                          "\nGAME OVER.")
        firstButton.config(text="Restart")
        secondButton.config(text="Restart")
    elif answer == "Pilfer the treasure room":
        label.config(text="You enter the treasure room full of ancient gold artifacts, most"
                          "\nof which are related to bar graph paraphernalia. You stuff them"
                          "\ninto your your special inventory."
                          "\nHowever, you stupidly knock over a torch by accident, and"
                          "\nyou set the whole ruins ablaze. You manage to barely escape"
                          "\nwith your life, though you end up with half as much gold as you had."
                          "\nGAME OVER.")
        firstButton.config(text="Restart")
        secondButton.config(text="Restart")
    elif answer == "Admit you can't read" or answer == "Find someone who can read it":
        label.config(text="The king says, \"You are an idiot. Please go find someone who can decipher"
                          "\nthis technobabble before I regress your lines!\"")
        firstButton.config(text="Look around")
        secondButton.config(text="Leave the king")
    elif answer == "Look around":
        label.config(text="You look around, and all of a sudden, some guy who has obviously eaten"
                          "\nway too many piecharts comes along and mugs you for all your money"
                          "\nand kills you."
                          "\nGAME OVER.")
        firstButton.config(text="Restart")
        secondButton.config(text="Restart")
    elif answer == "Leave the king":
        label.config(text="You return home, with your biggest excitement in life being having"
                          "\ncrossed a bridge."
                          "\nGAME OVER.")
        firstButton.config(text="Restart")
        secondButton.config(text="Restart")
    elif answer == "Concede and go back":
        label.config(text="You go back with the guard, handcuffed, and get beheaded with a guillotine"
                          "\nwith a blade that looks like a bell-shaped curve."
                          "\nGAME OVER.")
        firstButton.config(text="Restart")
        secondButton.config(text="Restart")
    else:
        close_window()

def close_window():
    root.destroy()

answer = 0

color = "#%06x" % random.randint(0x707070, 0xFFFFFF)
root = tk.Tk()
root.title("Stats project")
root.geometry("800x550")

#smallerFontSize = font.Font(size=10)
#mainFontSize = font.Font(size=40)
instructions = tk.Label(root,
                        text="Instructions: This is an interactive story that involves meaningful choices. Pick a choice. Some are good, some are bad.",
                        font="default 10",
                        bg=color)

credits = tk.Label(root,
                   text="Coded by Arman Tarkhanian, story written by Cristian Franco",
                   font="default 10",
                   bg=color)

randomizeColorButton = tk.Button(root,
                                 text="Randomize color",
                                 command=randomizeColor,
                                 font="default 10").pack()

label = tk.Label(root,
                 text="Hello, welcome to our project!",
                 bg=color,
                 font="default 40")

firstButton = tk.Button(root, text="I'm ready!")
def firstButtonAction():
    answer = firstButton.cget('text')
    flowchart(answer)
firstButton.config(command = firstButtonAction)
firstButton.pack(side="bottom", fill='both')

secondButton = tk.Button(root, text="NaN")
def secondButtonAction():
    answer = secondButton.cget('text')
    flowchart(answer)
secondButton.config(command = secondButtonAction)

buttonQuit = tk.Button(root,
                   text="Quit",
                   command = close_window,
                   font="default 10").pack()

photo = tk.PhotoImage(file="image1.gif")
photoLabel = tk.Label(root,
                   image=photo)
def randomizePicture():
    photo = tk.PhotoImage(file= "image" + str(random.randint(1,10)) + ".gif")
    photoLabel.config(image=photo)
    photoLabel.image = photo
photoLabel.pack()

credits.pack()
instructions.pack()

label.pack(side="bottom")
root.configure(bg=color)
center(root)
# def playMusic():
#     song = pyglet.media.load('OS RuneScape Theme Song.wav')
#     song.play()
#     pyglet.app.run()

root.mainloop()

# global player_thread
# player_thread = Thread(target=playMusic())
# player_thread.start()