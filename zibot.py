# coding: utf-8
import sys
import socket
import string
import os
import time
import re
import random
import urllib2

global rswitch
rswitch = True
i = 0
HOST='' #host server
PORT=6667
NICK=''
IDENT=''
REALNAME=''
OWNER='' #the person who owns this
CHANNELINIT=''
readbuffer=''
rekt = ['Rekt', 'Really Rekt', 'Tyrannosaurus Rekt', 'Cash4Rekt.com', 'Grapes of Rekt', 'Ship Rekt', 'Rekt markes the spot', 'Caught rekt handed', 'The Rekt Side Story', 'Singin\' In The Rekt', 'Painting The Roses Rekt', 'Rekt Van Winkle', 'Parks and Rekt', 'Lord of the Rekts: The Reking of the King', 'Star Trekt', 'The Rekt Prince of Bel-Air', 'A Game of Rekt', 'Rektflix', 'Rekt it like it\'s hot', 'RektBox 360', 'The Rekt-men', 'School Of Rekt', 'I am Fire, I am Rekt', 'Rekt and Roll', 'Professor Rekt', 'Catcher in the Rekt', 'Rekt-22', 'Harry Potter: The Half-Rekt Prince', 'Great Rektspectations', 'Paper Scissors Rekt', 'RektCraft', 'Grand Rekt Auto V', 'Call of Rekt: Modern Reking 2', 'Legend Of Zelda: Ocarina of Rekt', 'Rekt It Ralph', 'Left 4 Rekt', 'Pokemon: Fire Rekt', 'The Shawshank Rektemption', 'The Rektfather', 'The Rekt Knight', 'Fiddler on the Rekt', 'The Rekt Files', 'The Good, the Bad, and The Rekt', 'Forrekt Gump', 'The Silence of the Rekts', 'The Green Rekt', 'Gladirekt', 'Spirekted Away', 'Terminator 2: Rektment Day', 'The Rekt Knight Rises', 'The Rekt King', 'REKT-E', 'Citizen Rekt', 'Requiem for a Rekt', 'REKT TO REKT ass to ass', 'Star Wars: Episode VI - Return of the Rekt', 'Braverekt', 'Batrekt Begins', '2001: A Rekt Odyssey', 'The Wolf of Rekt Street', 'Rekt\'s Labyrinth', '12 Years a Rekt', 'Gravirekt', 'Finding Rekt', 'The Arekters', 'There Will Be Rekt', 'Christopher Rektellston', 'Hachi: A Rekt Tale', 'The Rekt Ultimatum', 'Shrekt', 'Rektal Exam', 'Rektium for a Dream', 'The Hunt for Rekt October', 'Oedipus rekt']
#msgpart = ''


s=socket.socket()
s.connect((HOST, PORT))
s.send('NICK '+NICK+'\n')
s.send('USER '+IDENT+' '+HOST+' bla :'+REALNAME+'\n')


def distro(msg):
    distrourl = "http://distrowatch.com/"
# if no arguments, gives random distro
    if msg == "":
        site = urllib2.urlopen(distrourl + "random.php") #uses random.php to give random distro
        distro = site.readlines()[1][24:-9] #gets distro name from title
        url = site.geturl() #gets url from the distro page
        return distro+ ' - '+url #returns distroname and url
    else:
    #only uses first argument ie damn returns Damn Small
        a = msg[:15]
        site = urllib2.urlopen(distrourl + "table.php?distribution=%s" %a) #uses table.php to be directed to a distro page
        distro = site.readlines()[1][24:-9] #gets distro from title
        url = site.geturl() #gets url from the page
        if distro !="": #if distro name is empty returns not found
            return distro+' - '+url
        else:
            return "Did not find distro named %s." %a

def parsemsg(msg):
    try:
        global rswitch
        complete=msg[1:].split(':',1) #Parse the message into useful data 
        info=complete[0].split(' ') 
        msgpart=complete[1] 
        sender=info[0].split('!') 
        print complete[1]

        #if msgpart[0] == ' ':
            #print("not today")
        if re.search('.*(which|what) (distro|distribution).*(should|best| use).*', re.sub('[\[\]\'?,]', '', msgpart.lower())) and re.search('^((?!worst).)*$', re.sub('[\[\]\'?,]', '', msgpart.lower())):
            s.send("privmsg " + info[2] +" :ARCHARCHARCHARCH AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARCH"+'\n')
        if msgpart[0]=='.': #Treat all messages starting with '`' as command 
            cmd=msgpart[1:].split(' ') 
            if cmd[0]=='test': 
                s.send("privmsg " + info[2] +" :hello world!"+'\n')
            if cmd[0]=='highfive':
                try:
                    s.send("privmsg " + info[2] +" :ACTION highfives " + str(re.sub('[\[\]\',]', '', str(cmd[1:]))) + '\n')
                except IndexError:
		    s.send("privmsg " + info[2] +" :ACTION highfives " + str(sender[0]) + '\n')
            if cmd[0] == 'spock':
                s.send("privmsg " + info[2] +" :Live long and prosper!"+ '\n')
	    if cmd[0] == 'hisname':
	        s.send("privmsg " + info[2] + " :JOOOOOOOOOOOHHHHHHHHHHHHN CEEEEEEEEEEEENNNNNNNNNNAAAAAAAAAAAAA" + '\n')
	    if cmd[0]=='distro':
            
                if len(cmd) == 1:
                    s.send ("privmsg #linuxmasterrace :" + distro( "" ) + '\n')
                else:
                    s.send ("privmsg #linuxmasterrace :" + distro( cmd[1] ) + '\n')
            if cmd[0]=='peasantry':
                s.send("privmsg #linuxmasterrace :bite my shiny gnu ass!"+'\n')
            if cmd[0] == 'linus':
                s.send("privmsg #linuxmasterrace :Hello everybody out there using minix. I'm doing a (free) operating system (just a hobby, won't be big and professional like gnu) for 386(486) AT clones. This has been brewing since april, and is starting to get ready. I'd like any feedback on things people like/dislike in minix, as my OS resembles it somewhat (same physical layout of the file-system (due to practical reasons) among other things). I've currently ported bash(1.08) and gcc(1.40), and things seem to work. This implies that I'll get something practical within a few months, and I'd like to know what features most people would want. Any suggestions are welcome, but I won't promise I'll implement them :-)" + '\n')
            if cmd[0] == 'dank':
                s.send("privmsg #linuxmasterrace :Smoke weed everyday" + '\n')
            if cmd[0] == 'dankmeme':
	        s.send("privmsg " + info[2] + " :http://i.imgur.com/2VKq6AC.jpg" + '\n')
       	   
	    if cmd[0] == 'interject':
                s.send("privmsg " + info[2] +" :I'd just like to interject for a moment. What you’re referring to as Linux, is in fact, GNU/Linux, or as I’ve recently taken to calling it, GNU plus Linux. Linux is not an operating system unto itself, but rather another free component of a fully functioning GNU system made useful by the GNU corelibs, shell utilities and vital system components comprising a full OS as defined by POSIX." + '\n')
            if cmd[0] == 'rekt':
                random.seed()
                s.send("privmsg " + info[2] +" :" + rekt[random.randrange(74)] + '\n')
            if cmd[0] == 'shrug':
                s.send("privmsg " + info[2] +" :¯\_(ツ)_/¯" + '\n')
            if cmd[0] == 'rolecall':
                s.send("privmsg " + info[2] +" :Install Gentoo!" + '\n')
            if cmd[0] == 'aids':
                s.send("privmsg " + info[2] +" :Windows command prompt is in any way functional" + '\n')
            if cmd[0] == 'dankswag':
                s.send("privmsg " + info[2] +" :420 yolo #swag smoke weed erry dayyyy, ayy lmao" + '\n')
                s.send("privmsg " + info[2] + " :BLAME THE FRENCH" + '\n')
            if cmd[0] == 'zroll' and rswitch == True:
                roll = ['']
                roll = cmd[1].split('d')
                i = 0
                total = 0
                rolls = ['0']
                thetheroll = ''
                theroll = 0
                try:
                    while i < int(roll[0]):
                        theroll = random.randrange(1, int(roll[1]))
                        total += theroll
                        rolls.append(theroll)
                        thetheroll = str(total) + ' ' + str(rolls[1:])
                        i += 1 
                except:
                    theroll = random.randrange(1, int(roll[1]))
                    total += theroll
                    rolls.append(theroll)
                    thetheroll = str(total) + ' ' + str(rolls[1:])
                s.send("privmsg " + info[2] +" " + "(" + sender[0] +") " + str(thetheroll) + '\n')
            if cmd[0] == 'rswitch':
                if cmd[1] == 'off':
                    rswitch = False
                    s.send("privmsg " + info[2] +" 4 zibot rolling disabled:(" + '\n')
                elif cmd[1] == 'on':
                    rswitch = True
                    s.send("privmsg " + info[2] +" 3 zibot rolling enabled:D" + '\n')
                else:
                    s.send("privmsg " + info[2] +" invalid option" + '\n')
            if cmd[0] == 'doritotini':
                s.send("privmsg " + info[2] +" http://i.imgur.com/yXfaopc.jpg" + '\n')
    except IndexError:
        return 0
    #if "\xe3" in msgpart:
        #time.sleep(1)
        #s.send("privmsg " + info[2] +" :.bang" + '\n')


while 1:
    line=s.recv(500) #recieve server messages #server message is output
    line=line.rstrip() #remove trailing 'rn'
    line=line.split('\n')
    for item in line:
        if item.find('Welcome')!=-1: #welcome message
            print ('you can do it')
            s.send('privmsg ' + 'NickServ' + ' :IDENTIFY password' + '\r\n')
            s.send('JOIN '+CHANNELINIT+'\n') #joins channel
            #s.send('USER '+ ""  +' '+HOST+' bla :'+REALNAME+'\n')
            s.send('NICK '+ "" +'\n')
        if item.find('PRIVMSG')!=-1: #calls a parsing function
            parsemsg(item)
            time.sleep(1)
 
        if (item.find("PING") != -1 ): #if server pings then pong
            item=item.rstrip() #remove trailing 'rn'
            item=item.split()
            s.send('PONG ' + item[1] + '\n')
        
         
    

