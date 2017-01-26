from colorama import Fore
import random
import sys
import re

Teams = ['Arsenal', 'Chelsea', 'Everton', 'Liverpool', 'Mancity','Man Utd','Tottenham','PSG','Inter Milan','Juventuse','Napoli','AS ROMA','AT M','Sevilla','Dortmoont']

Teams_size = len(Teams)


if __name__=='__main__':
    print (Fore.RED+'\n<<<Teams>>>')
    print Teams
    print (Fore.RESET)
    while True:
        name = raw_input(Fore.BLUE+'# %s Name: ')
        print (Fore.RESET)
        if name == 'exit':
            sys.exit()
        
        elif re.match('rm.*',name):
            args = name.split()[1]
            print args
            Teams.remove(args)
            Teams_size = Teams_size-1
            print (Fore.RED+'\n<<<Teams>>>')
            print Teams
            print (Fore.RESET)

        else:
            tm = Teams[random.randrange(0,Teams_size)]
            print (Fore.GREEN+'RESULT: %s - %s\n' % (name,tm))
            print (Fore.RESET)
            
            Teams.remove(tm)
            Teams_size = Teams_size-1
            print (Fore.RED+'\n<<<Teams>>>')
            print Teams
            print (Fore.RESET)

            
