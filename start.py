import sys
import random
import string
import datetime
import logging
import subprocess
import json
import time
import requests
import urllib.request
import ssl

# Fixed Scraping: SSL: CERTIFICATE_VERIFY_FAILED error
ssl._create_default_https_context = ssl._create_unverified_context

HELP = """OPTIONS:
    --cute                          (default) sends cute/caring/lovie-dovie messages (okie ❤️🥰😘)
    --mean                          sends moodie messages that tend to pick up fights (k.)
    --hungry                        sends food related messages (Kk 😋🤤🍕🍩)
    --random                        sends messages like a bipolar (k. ❤️🥰😘) 
    -f (frequent)                   sends him message more frequently
    -r (reply)                      adds auto-reply feature, else ghost him without the tag """

subreddit_list = ["BetterEveryLoop", "AnimalsBeingJerks", "meme"]

#todo: https://www.twilio.com/blog/2016/09/how-to-receive-and-respond-to-a-text-message-with-python-flask-and-twilio.html

def printInfo(mood, settings, appleID):
    print("Starting AI girlfriend chatbot...")
    if 'r' in settings:
        print("Sending messages to " + appleID + " in " + mood[2:] + " mood with auto-reply feature. ")
    else: 
        print("Sending messages to " + appleID + " in " + mood[2:] + " mood. ")

#credit: https://github.com/noahbroyles/iMessageFUN
def runAppleScript(applescript):
    arguments = [item for x in [("-e", l.strip()) for l in applescript.split('\n') if l.strip() != ''] for item in x]
    proc = subprocess.Popen(["osascript"] + arguments, stdout=subprocess.PIPE)
    proc.stdout.flush()

def sendMessage(message, appleID):
    script = '''
    on run
        tell application "Messages"
            set iMessageService to 1st service whose service type = iMessage
            set boyfriend to buddy "''' + appleID + '''" of iMessageService
            send "''' + message + '''" to boyfriend
        end tell
    end run'''
    runAppleScript(script)
    logging.info("Sent" + message + " at " + str(datetime.datetime.now()))

def getMeme(subreddit):
    response = requests.get("https://meme-api.herokuapp.com/gimme/" + subreddit)
    url = json.loads(response.text)["url"]
    # apple script cannot send image file: urllib.request.urlretrieve(url, "meme.jpg")
    return url

def getMessage(path, category):
    with open('messages/' + path, 'r') as file:
        data = json.load(file)
    x = random.randint(0, len(data[category]) - 1)
    return data[category][x]

def generateMessage(mood, appleID):
    if "mean" in mood:
        sendMessage(message, appleID)
    elif "hungry" in mood:
        sendMessage(message, appleID)
    elif "random" in mood:
        sendMessage(message, appleID)
    else:
        x = random.randint(0, 11)
        if x%11 == 0: 
            message = getMessage("cute.json", "greetings")
            sendMessage(message, appleID)
        else:
            i = random.randint(0, len(subreddit_list) - 1)
            meme = getMeme(subreddit_list[i])
            sendMessage(meme, appleID)

if __name__ == "__main__":

    args = sys.argv
    if len(args) < 2:
        print("\n" + HELP + "\n")
    
    try:
        mood = [arg for arg in args if arg.startswith("--")][0]
    except IndexError:
        mood = '--cute'
    
    try:
        settings = [arg for arg in args if arg.startswith("-") and not arg.startswith("--")][0]
    except IndexError:
        settings = ''    

    appleID = args[-1]
    for x in appleID:
        if x not in string.digits and '@' not in appleID:
            sys.exit("ERROR: Invalid AppleID or Phone number: {}".format(appleID))

    printInfo(mood, settings, appleID)
    logging.basicConfig(filename="message.log", level=logging.INFO)
    logging.info("Sending message to " + appleID + " with " + mood + " " + settings)
    
    while True:
        try:
            generateMessage(mood, appleID)
            if 'f' in settings:
                time.sleep(5)
            else:
                time.sleep(10) 
        except KeyboardInterrupt:
            print("RAP got interrupted")
            break
        except Exception as e:
            print(e)
            logging.ERROR(e)
            break
    








