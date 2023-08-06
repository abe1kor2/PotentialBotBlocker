import instabot
import time,random

def pick_random(start, end):
    tar = random.randint(2,15)
    i = 1
    rand = 0
    while i<=tar:
        rand = random.randint(start,end)
        i+=1
    return rand




def count_down(timer):
    while timer:
        mins, secs = divmod(timer, 60)
        timeformat = 'Sleeping CountDown => {:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        timer -= 1
    print('\n\n')


bot=instabot.Bot(base_path='logs')
#add your username an dpassword here
username=""
password=""
bot.login(username=username,password=password)

user_id=bot.get_user_id_from_username(username)
followers=(bot.get_user_followers(user_id))
fh = open('Potential Bots.txt', 'w')

for follower in followers:
    
    user_info=bot.get_user_info(follower)
    name=user_info.get('username')
    potential_bot_followers=(user_info["follower_count"])
    # set a minimum followers number here add your desire number
    limit=10
    if int(potential_bot_followers)<limit:
        print("\n user ", name, " has less then ", limit ," followers")

        fh.write("\n user has now been blocked %s" % name)
        print("\n BLOCKED")
        bot.api.block(follower)
        count_down((pick_random(5,10)))
        
    else:
        print("\n[++] greater than ", limit ," followers")
        time.sleep(0.5)

fh.close()