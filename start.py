import sys
import random
import string
import datetime
import logging
import subprocess

HELP = """OPTIONS:
    --cute                          (default) sends cute/caring/lovie-dovie messages (okie ❤️🥰😘)
    --mean                          sends moodie messages that tend to pick up fights (k.)
    --hungry                        sends food related messages (Kk 😋🤤🍕🍩)
    --random                        sends messages like a bipolar (k. ❤️🥰😘) 
    -f (frequent)                   sends him message more frequently
    -r (reply)                      adds auto-reply feature, else ghost him without the tag """


#todo: -f <int> user can set how frequently they want to send messages

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
            set leyla to buddy "''' + appleID + '''" of iMessageService
            send "''' + message + '''" to leyla
        end tell
    end run'''
    runAppleScript(script)
    logging.info("Sent" + message + " at " + str(datetime.datetime.now()))




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
    
    sendMessage("hiii", appleID)









