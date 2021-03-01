import instabot
import time,random

def pick_random(s,e):
    tar = random.randint(2,15)
    i = 1
    rand = 0
    while i<=tar:
        rand = random.randint(s,e)
        i+=1
    return rand




def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = 'Sleeping CountDown => {:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('\n\n')


bot=instabot.Bot(base_path='logs')
#add your username an dpassword here
user=""
passw=""
bot.login(username=user,password=passw)

idd=bot.get_user_id_from_username(user)
fol=(bot.get_user_followers(idd))
fh = open('Potential Bots.txt', 'w')

for i in fol:
    
    inf=bot.get_user_info(i)
    name=inf['username']
    num=(inf["follower_count"])
    # set a minimum followers number here add your desire number
    limit=10
    if int(num)<limit:
        print("\n user ", name, " has less then ", limit ," followers")

        fh.write("\n user has now been blocked %s" % name)
        print("\n BLOCKED")
        bot.api.block(i)
        countdown((pick_random(30,50)))
        
    else:
        print("\n[++] greater than ", limit ," followers")
        time.sleep(0.5)

fh.close()