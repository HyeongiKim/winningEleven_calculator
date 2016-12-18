#!/usr/bin/env python2

# Written by Kim Hyeongi
# 2016.12.17.
from colorama import Fore
import time
import sys
import re

Scores = []

def Cal_score(mem1,mem2,score1,score2):
    for member in Scores:
        if member[0] == mem1:
            if score1>score2:
                member[1]+=1
            elif score1==score2:
                member[2]+=1
            else:
                member[3]+=1
            member[4] += (score1-score2)
    for member in Scores:
        if member[0] == mem2:
            if score1>score2:
                member[3]+=1
            elif score1==score2:
                member[2]+=1
            else:
                member[1]+=1
            member[4] += (score2-score1)
    return 0

def Print_score():
    print (Fore.GREEN+'\n####SCORE BOARD####\n')
    print '-'*19
    print '%5s | %2s %2s %2s %2s'%('Name','W','D','L','S')
    print '-'*19
    for member in Scores:
        print '%5s | %2d %2d %2d %2d'% (member[0],member[1],member[2],member[3],member[4])
    print (Fore.RESET)
    return 0

if __name__=='__main__':
    print (Fore.GREEN+'\nBooting calculator...\n')
    print (Fore.RESET)
    time.sleep(1)
    
    print (Fore.RED+'Put (name and selected team) member\n')
    for i in range(4):
        name = raw_input('# %s Name: \n' % (i+1))
        Scores.append([name,0,0,0,0])

    print (Fore.RESET)
    Print_score()

    while True:
        command = raw_input('# ')
        if re.match('add.*',command):
            args = command.split()[1:]
            Cal_score(args[0],args[1],int(args[2]),int(args[3]))
        elif command=='print':
            Print_score()

        elif command=='exit':
            sys.exit()

