#!/usr/bin/python
from collections import OrderedDict 
import argparse
import random
import re
import sys


##################################
# This program will play war for 2 - 10 people, based on input from the cmd line
# The default will be that the user gets to (basically, press a key to flip a card)
# If the user passes in an argument for auto = 1 then the computer will play all hands
##################################

##################################
# Functions!
def makedeck():
	deck = []
	suits = ["clubs", "diamonds", "hearts", "spades"]
	cards = ['02','03','04','05','06','07','08','09','10','11','12','13','14']
	for s in suits:
		for c in cards:
			deck.append(str(c) + s)
#	print(deck)
#	print(len(deck))
	return(deck)

def shuffle(mydeck):
	#print("in shuffle func")
	for i in range(0, len(mydeck), 1):
		r = random.randint(0, i)
		mydeck[i], mydeck[r] = mydeck[r], mydeck[i]
	return(mydeck)

def isplayerout(thisplayer):
	print("in is player out for player %s" % thisplayer)
	print(len(globals()['gameplayer%s' % thisplayer]))
	if(len(globals()['gameplayer%s' % thisplayer]) == 0):
		return True
	else:
		return False

def isthereawinner(thisplayer):
	print("in is there a winner")
	if(len(globals()['gameplayer%s' % thisplayer]) == 52):
		print("player %s wins!!" % thisplayer)
		exit(0)

# /Functions
##################################

##################################
# step 0, define argparse, help, and basic setup things
helptext = "This is a program to play the classic card game, \"War\" against the computer players or in an automated fashion where the computer players play without any human player"
parser = argparse.ArgumentParser()
parser.add_argument("--auto", "-a", action='store_true', help="use --auto = 1 if you want the computer to play without human interaction")
parser.add_argument("--players", "-p", help="number of players, between 2 and 10, inclusive")
parser.description = helptext
#parser = argparse.ArgumentParser(description = helptext)
args = parser.parse_args()
#print(args)
#print(args.players)
#print(args.auto)

if args.players:
	numplayers = args.players
	try:
		numplayers = int(args.players)
	except:
		print("you must enter an integer for the number of players")
		exit(1)
		
#	print(numplayers)
	if numplayers < 0 or numplayers > 52:
		print("The number of players must be between 2 and 52")
		exit(1)
		
else:
	print("user wants default of two players")
	numplayers = int(2)
allplayers = []

for i in range(int(numplayers)):
	globals()['gameplayer%s' % i] = []

myvars = OrderedDict(globals())

for allvars in myvars:
	if ("gameplayer") in allvars:
		allplayers.append(allvars)
allplayers.sort() # so that the  players are in order: gameplayer0, gameplayer1, ...

print(len(allplayers))

for x in allplayers:
	print(x)
	
print("done with basic setup")
# end basic setup
##################################



##################################
# First, let's create the array of an unshuffled deck


		
mydeck = makedeck()
mydeck = shuffle(mydeck)
print(mydeck)
print(len(mydeck))


	
if args.auto:
	print("user wants an automated game")


# End creating the classes for the deck and players
##################################

# Create arrays to hold the cards for each player
##################################
initcardcount = 52/numplayers
print("initcardcount is %s " % int(initcardcount))
anyremainder = 52 % numplayers
if(anyremainder != 0):
	print("there are cards remaining")
cards = int(0)

while(cards < (initcardcount -1)):
	for x in range(len(allplayers)):
		print(x)
		globals()['gameplayer%s' % x].append(mydeck[0])
		print(globals()['gameplayer%s' % x])
		mydeck.pop(0)
	cards = cards + 1
	print("cards per person dealt: %s" % cards)
	print("cards left: %s" % len(mydeck))

print("time to start the game")


# End dealing the deck
##################################

##################################
# This will be the main part of the game
# the process will be:
# 1) check if any player is out. If so, drop them
# --- what would be the best process for that? 
# --- --- if player3 drops out, should player4, be renamed to player3 and player5 be renamed to player4?
# --- --- if player3 drops out, should they play a card of value 0 each turn so that player# stays the same and that the person that's out has no chance to somehow win the game?
# --- --- maybe I could use the isplayerout() and simply skip them; who cares if there are players of player0, player1, player4 left?
# 2) for the players that are in the game, get their card[0] 
# 3) we don't care if the card played is a hearts, club, ...  so we'll look at the first two characters of that array entry.
# 4) check if one person has the highest ranking card
# 5) if there is a tie in the highest cards, war!
# 5a) if war, the players that had less than the highest cards are already out
# 5b) warplayersX[] for each player in the war? What is the best way to pull them aside? Maybe have a war() where I can pass in a list of the players in the war? If so, then what about a double war? I'd have to figure out a way to correctly exit a nested war(). hmm
# 6) when you finally get one player with the highest card, add all of the played cards to the winner's hand
# 7) after figuring out who won, goto 1

# i'll be looping waiting for somebody to win, so all this will be in a big loop.

##################################
# check if any player has run out of cards (lost the game)
# if yes, remove them from players[] or maybe leave them in but set their top card to be value 0 so they never win?
while True:
	for x in range(len(allplayers)):
		print(x)
		if(isplayerout(int(x))):
			for y in range(len(allplayers)):
				print(y)
				globals()['gameplayer%s' % x] = globals()['gameplayer%s' % x+1] 
				print(globals()['gameplayer%s' % x])

# End checking for an eliminated players
##################################

##################################
# Fifth, have the remaining players flip over a card (look at card in hand[0] for them)
	print("going to print the top card for each player")
	for x in range(len(allplayers)):
		print("player %s" % x)
		print((globals()['gameplayer%s' % x][0])[0:2])
		

# End having the players flip their top cardcard
##################################

##################################
# sixth, check if one person had the highest ranking card out of all players


# End checking if a player won the hand
##################################

##################################
# If yes, add those cards to their hand


# End adding those played cards to the winner's hand
##################################

##################################
# If the top two or more people tied, WAR!

	###################################
	# If one of those players that tied doesn't have any more cards in their hand, they lose


	# End the losing player from that hand
	##################################


# end war
###################################


###################################
# If one of those players that tied doesn't have four remaining cards for the three down + one up,
# use only cards_remaining - 1

	
	for x in range(len(allplayers)):
		print(x)
		isthereawinner(int(x))
	
	print("going to force an exit")
	exit(0)

# End war
##################################

