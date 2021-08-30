# iMessage Chatbot

*AI Girlfriend in iMessage*  

Dating is hard and time consuming. Communication is essential to having a happy, healthy relationship. This chatbot is here to help you solve the problem.
<br>
## Design:
*A clear and professional communication with client is the key to a successful product.* 

<img width="1101" alt="Screen Shot 2021-08-29 at 5 10 28 PM" src="https://user-images.githubusercontent.com/20052048/131270077-db75877c-f8d6-4937-b950-30093c149ca0.png">


## Setup:
Install the requirements for the project by running the following command in your terminal:
```
pip install -r requirements.txt
```

## Run the script:
Default: 
```
python start.py [apple ID or phone number]
```
Tags: 
<pre>
    --cute                          (default) sends cute/caring/lovie-dovie messages (okie ❤️🥰😘) 
    --mean                          sends moodie messages that tend to pick up fights (k.)
    --hungry                        sends food related messages (Kk 😋🤤🍕🍩)
    --random                        sends messages like a bipolar (k. ❤️🥰😘)
    -f (frequent)                   sends him message more frequently
    -r (reply)                      adds auto-reply feature, else ghost him without the tag 
</pre>
For example: if you want to send a lot of mean messages to your bf with auto-reply feature:
```
python start.py -rf --mean [apple ID or phone number]
```


## TODO Checklist:
- [X] logging
- [X] have this algorithm running somewhere 24/7 - local so far
- [ ] f tag: -f <int minutes> user can set how frequently they want to send messages
- [ ] auto-reply: NLP. reply based on user behavior (prev conversation)
- [ ] fetch new memes from internet
- [ ] send messages to multiple boyfriends because I can
