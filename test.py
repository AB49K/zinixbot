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
HOST = sys.argv[2]  # host server
PORT = 6667
NICK = sys.argv[3]
IDENT = sys.argv[3]
REALNAME = sys.argv[3]
OWNER = 'zinn'  # the person who owns this
CHANNELINIT = '#linuxmasterrace'
readbuffer = ''
rekt = ['Rekt', 'Really Rekt', 'Tyrannosaurus Rekt', 'Cash4Rekt.com', 'Grapes of Rekt', 'Ship Rekt', 'Rekt markes the spot', 'Caught rekt handed', 'The Rekt Side Story', 'Singin\' In The Rekt', 'Painting The Roses Rekt', 'Rekt Van Winkle', 'Parks and Rekt', 'Lord of the Rekts: The Reking of the King', 'Star Trekt', 'The Rekt Prince of Bel-Air', 'A Game of Rekt', 'Rektflix', 'Rekt it like it\'s hot', 'RektBox 360', 'The Rekt-men', 'School Of Rekt', 'I am Fire, I am Rekt', 'Rekt and Roll', 'Professor Rekt', 'Catcher in the Rekt', 'Rekt-22', 'Harry Potter: The Half-Rekt Prince', 'Great Rektspectations', 'Paper Scissors Rekt', 'RektCraft', 'Grand Rekt Auto V', 'Call of Rekt: Modern Reking 2', 'Legend Of Zelda: Ocarina of Rekt', 'Rekt It Ralph', 'Left 4 Rekt', 'Pokemon: Fire Rekt',
        'The Shawshank Rektemption', 'The Rektfather', 'The Rekt Knight', 'Fiddler on the Rekt', 'The Rekt Files', 'The Good, the Bad, and The Rekt', 'Forrekt Gump', 'The Silence of the Rekts', 'The Green Rekt', 'Gladirekt', 'Spirekted Away', 'Terminator 2: Rektment Day', 'The Rekt Knight Rises', 'The Rekt King', 'REKT-E', 'Citizen Rekt', 'Requiem for a Rekt', 'REKT TO REKT ass to ass', 'Star Wars: Episode VI - Return of the Rekt', 'Braverekt', 'Batrekt Begins', '2001: A Rekt Odyssey', 'The Wolf of Rekt Street', 'Rekt\'s Labyrinth', '12 Years a Rekt', 'Gravirekt', 'Finding Rekt', 'The Arekters', 'There Will Be Rekt', 'Christopher Rektellston', 'Hachi: A Rekt Tale', 'The Rekt Ultimatum', 'Shrekt', 'Rektal Exam', 'Rektium for a Dream', 'The Hunt for Rekt October', 'Oedipus rekt']
#msgpart = ''

shaggy = ['imma rape you make you  gay lol', 'imma rape you make you gay lol', 'you can go to bed now on your own or smell this rag....', 'SusWombat: is never right', 'why am i still typing', 'was a shock to see bare ass lol', 'its like NO, i\'m LAZY LAZY LA-ZY', 'ShaggyTwoDope thinks based on some questions Winter_Fox asks... hes making a bomb or something', 'they already proved they dont mind white stuff covering their face', 'what\'d i tell you about playing cops and robbers without protection', 'sounds like AWindowsKrill jammed his penis in the door again', 'my butthole was bleeding and everything', 'its not like i said, "i like raping turtles and killing hobos"', 'i always tell her the gun wasnt real', 'bios says.. idc bitch anime is on', 'girl is that ass gpl\'d, cause you gotta share that source', 'there is an orgy inside me at all times', '#anarchy', 'some people say hookers with no teeth are terrible but thats a matter of opinion', 'Show me on the hard drive where he touched you', 'wait til they see my dict', 'most of my scars are mental ones', 'freak anal midgets?', 'don\'t worry we all go through a gay phase', 'PureTryOut hates this guy', 'slow or fast, things worth doing are things worth doing, unless its for the dutch.', '(seen enough naked dudes, so nothing shocked me)', 'the dude was eating his own shit', 'if a girl aint down to play some mario, eat some snacks |  aint down with shaggy', 'they use linux just to use wine', 'i never EVER want to smell garlic or put my fist in a cow again unless its for fun', 'Brig once killed a homeless man using the broken part of a spoon he stole from a fast food place.', 'like some random hot girl is gonna get a arch linux turses joke lol', 'its only wrong if she wakes up...', 'ever wonder if the percent of flammable goats is higher than linux users', 'i wonder, how hard would you need to rub two people together to get fire', 'no is just japanese for harder', 'send me an email, shaggy@horsefucker.org', 'best time i had was with a old dude, he was just great lol', 'i return', 'i return <ShaggyTwoDope> so wet :-(', 'i have no filter lol', 'be like "here is your 10 inch item you ordered" printed on the package', 'Chewbacca Gets Sucked Off By Two Female Storm ...', 'every joke is better with a little girl lol', 'you think i have to like you, and you like me?', 'they put cold things in my butt, butt, butt', 'TeenageThowawayV2: good thing my dungeon has no windows', 'TeenageThrowAwayV2: good thing my dungeon has no windows <ShaggyTwoDope> now walk this way..', 'put the lotion on', 'call me a fuckwas', 'i\'d kill a hooker with a wet tire for some crackers...', 'i went full force on her little body', 'no penis for me. no sir...', 'its other peoples porn i dig', 'gotta say, not the first time seeing inside of another mans ass... thanks internet', 'ive had more sex with mentally unstable girls than most people will']

s = socket.socket()
s.connect((HOST, PORT))
s.send('NICK ' + NICK + '\n')
s.send('USER ' + IDENT + ' ' + HOST + ' bla :' + REALNAME + '\n')


def distro(msg):
    distrourl = "http://distrowatch.com/"
# if no arguments, gives random distro
    if msg == "":
        site = urllib2.urlopen(distrourl + "random.php")  # uses random.php to give random distro
        distro = site.readlines()[1][24:-9]  # gets distro name from title
        url = site.geturl()  # gets url from the distro page
        return distro + ' - ' + url  # returns distroname and url
    else:
        # only uses first argument ie damn returns Damn Small
        a = msg[:15]
        site = urllib2.urlopen(distrourl + "table.php?distribution=%s" %
                               a)  # uses table.php to be directed to a distro page
        distro = site.readlines()[1][24:-9]  # gets distro from title
        url = site.geturl()  # gets url from the page
        if distro != "":  # if distro name is empty returns not found
            return distro + ' - ' + url
        else:
            return "Did not find distro named %s." % a

def stackoverflow(msg):
    found = False
    message = ""
    sourl = "http://stackoverflow.com/"
    if msg == "":
        return "Please give a query"
    else:
        a = msg[:15]
        site = (sourl + "search?q=" + a)
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = urllib2.Request(site,headers=hdr)
        page = urllib2.urlopen(req)
        soq = page.readlines()
        for line in soq:
            if "Q:" in line:
                message += line.rstrip('\n')
                break
        for line in soq:
            if found:
              message += re.sub('<.*>', '', line).rstrip('\n')
              break
            if "excerpt" in line:
                found = True 
        return message.rstrip('\n')


def parsemsg(msg):
    try:
        global rswitch
        complete = msg[1:].split(':', 1)  # Parse the message into useful data
        info = complete[0].split(' ')
        msgpart = complete[1]
        sender = info[0].split('!')
        print complete[1]

        # if msgpart[0] == ' ':
        #print("not today")
        if re.search('.*(which|what) (distro|distribution).*(should|best| use).*', re.sub('[\[\]\'?,]', '', msgpart.lower())) and re.search('^((?!worst| ?!not).)*$', re.sub('[\[\]\'?,]', '', msgpart.lower())):
            s.send("privmsg " +
                   info[2] + " :ARCHARCHARCHARCH AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARCH" + '\n')
        if msgpart[0] == '.':  # Treat all messages starting with '`' as command
            cmd = msgpart[1:].split(' ')
            if cmd[0] == 'test':
                s.send("privmsg " + info[2] + " :hello world!" + '\n')
            if cmd[0] == 'highfive':
                try:
                    s.send("privmsg " + info[2] + " :ACTION highfives " +
                           str(re.sub('[\[\]\',]', '', str(cmd[1:]))) + '\n')
                except IndexError:
                    s.send("privmsg " + info[2] + " :ACTION highfives " + str(sender[0]) + '\n')
            if cmd[0] == 'spock':
                s.send("privmsg " + info[2] + " :Live long and prosper!" + '\n')
            if cmd[0] == 'hisname':
                s.send(
                    "privmsg " + info[2] + " :JOOOOOOOOOOOHHHHHHHHHHHHN CEEEEEEEEEEEENNNNNNNNNNAAAAAAAAAAAAA" + '\n')
            if cmd[0] == 'distro':

                if len(cmd) == 1:
                    s.send("privmsg #linuxmasterrace :" + distro("") + '\n')
                else:
                    s.send("privmsg #linuxmasterrace :" + distro(cmd[1]) + '\n')
            if cmd[0] == 'so':
                if len(cmd) == 1:
                    s.send("privmsg " + info[2] + " :" + stackoverflow("") + '\n')
                else:
                    s.send("privmsg " + info[2] + " :" + stackoverflow(cmd[1]) + '\n')
            if cmd[0] == 'peasantry':
                s.send("privmsg #linuxmasterrace :bite my shiny gnu ass!" + '\n')
            if cmd[0] == 'linus':
                s.send("privmsg #linuxmasterrace :Hello everybody out there using minix. I'm doing a (free) operating system (just a hobby, won't be big and professional like gnu) for 386(486) AT clones. This has been brewing since april, and is starting to get ready. I'd like any feedback on things people like/dislike in minix, as my OS resembles it somewhat (same physical layout of the file-system (due to practical reasons) among other things). I've currently ported bash(1.08) and gcc(1.40), and things seem to work. This implies that I'll get something practical within a few months, and I'd like to know what features most people would want. Any suggestions are welcome, but I won't promise I'll implement them :-)" + '\n')
            if cmd[0] == 'dank':
                s.send("privmsg #linuxmasterrace :Smoke weed everyday" + '\n')
            if cmd[0] == 'dankmeme':
                s.send("privmsg " + info[2] + " :http://i.imgur.com/2VKq6AC.jpg" + '\n')

            if cmd[0] == 'interject':
                s.send("privmsg " + info[2] + " :I'd just like to interject for a moment. What you’re referring to as Linux, is in fact, GNU/Linux, or as I’ve recently taken to calling it, GNU plus Linux. Linux is not an operating system unto itself, but rather another free component of a fully functioning GNU system made useful by the GNU corelibs, shell utilities and vital system components comprising a full OS as defined by POSIX." + '\n')
            if cmd[0] == 'rekt':
                random.seed()
                s.send("privmsg " + info[2] + " :" + rekt[random.randrange(74)] + '\n')
            if cmd[0] == 'shaggy':
                random.seed()
                s.send("privmsg " + info[2] + " :" + "<ShaggyTwoDope> " + shaggy[random.randrange(56)] + '\n')
            if cmd[0] == 'shrug':
                s.send("privmsg " + info[2] + " :¯\_(ツ)_/¯" + '\n')
            if cmd[0] == 'rolecall':
                s.send("privmsg " + info[2] + " :Install Gentoo!" + '\n')
            if cmd[0] == 'aids':
                s.send("privmsg " + info[2] +
                       " :Windows command prompt is in any way functional" + '\n')
            if cmd[0] == 'dankswag':
                s.send("privmsg " + info[2] +
                       " :420 yolo #swag smoke weed erry dayyyy, ayy lmao" + '\n')
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
                s.send("privmsg " + info[2] + " " + "(" + sender[0] + ") " + str(thetheroll) + '\n')
            if cmd[0] == 'rswitch':
                if cmd[1] == 'off':
                    rswitch = False
                    s.send("privmsg " + info[2] + " 4 zibot rolling disabled:(" + '\n')
                elif cmd[1] == 'on':
                    rswitch = True
                    s.send("privmsg " + info[2] + " 3 zibot rolling enabled:D" + '\n')
                else:
                    s.send("privmsg " + info[2] + " invalid option" + '\n')
            if cmd[0] == 'doritotini':
                s.send("privmsg " + info[2] + " http://i.imgur.com/yXfaopc.jpg" + '\n')

    except IndexError:
        return 0
    # if "\xe3" in msgpart:
        # time.sleep(1)
        #s.send("privmsg " + info[2] +" :.bang" + '\n')


while 1:
    line = s.recv(500)  # recieve server messages #server message is output
    line = line.rstrip()  # remove trailing 'rn'
    line = line.split('\n')
    for item in line:
        if item.find('Welcome') != -1:  # welcome message
            print('you can do it')
            s.send('privmsg ' + 'NickServ' + ' :IDENTIFY ' + sys.argv[1] + '\r\n')
            s.send('JOIN ' + CHANNELINIT + '\n')  # joins channel
            #s.send('USER '+ ""  +' '+HOST+' bla :'+REALNAME+'\n')
            s.send('NICK ' + "" + '\n')
            s.send('JOIN #lmrdungeonworld'+'\n')
            s.send('JOIN #ayyylmao'+'\n')
            s.send('JOIN #secretlinuxchannel'+'\n')
            s.send('NICK '+ sys.argv[4] +'\n')

        if item.find('PRIVMSG') != -1:  # calls a parsing function
            parsemsg(item)
            time.sleep(1)

        if (item.find("PING") != -1):  # if server pings then pong
            item = item.rstrip()  # remove trailing 'rn'
            item = item.split()
            s.send('PONG ' + item[1] + '\n')
