import telebot

Token="6418845587:AAEIflv6abFe7OdPCiv0OO49PXj6Pb8hy0Q"

bot=telebot.TeleBot(Token)

@bot.message_handler(['start'])
def start(message):
    bot.reply_to(message,"Welcome to the Fruitful Ventures 😀.")
    
@bot.message_handler(['hi'])
def hi(message):
    bot.reply_to(message,"Hi 👋👋")
    
@bot.message_handler(['howareyou','howareyou?'])
def howareyou(message):
    bot.reply_to(message,"I am good!")
    
@bot.message_handler(['goodmorning','GoodMorning'])
def goodmorning(message):
    bot.reply_to(message," GoodMorning 😀.")

@bot.message_handler(['Goodafternoon','goodafternoon'])
def goodafternoon(message):
    bot.reply_to(message," Good afternoon 😀.")    

@bot.message_handler(['Goodevening','goodevening'])
def goodevening(message):
    bot.reply_to(message," Good evening 😀.")  
      
@bot.message_handler(['Good night','goodnight'])
def goodafternoon(message):
    bot.reply_to(message," Good night 😴.")  
      
@bot.message_handler(['Bye ',"bye"])
def bye(message):
    bot.reply_to(message,"Bye 👋👋")

@bot.message_handler(['whatisyourname'])
def whatisyourname(message):
    bot.reply_to(message,"My Name is Berry Bot")
    


@bot.message_handler(['list'])
def list(message):
    bot.reply_to(message,"apple=20$,     Banana=21$,    Mango=45$,    Kiwi=43$,        Orange=27$,     Pineapple=32$")    
    
@bot.message_handler(['help'])
def help(message):
    bot.reply_to(message,'''
    "If you have any problem please! contact our developer.At the same time Search /Contact")    
    Commands to use the bot:         
    Type:- /start :-to talk the bot             
    Type:-/help:-if you needed help than type it.
    Type:-/list:- It can give the list of the Fruits.
    Type:-/Contact:-It can give the  information for contact the Developer.
    Type:-/Order:-Use the command to order your list.
    Type:-/whatisthepriceofapple:-You can ask the price of any item.            
    Type:-/whocreatethisbot:-You can ask the creator name of the bot.
    Type:-/givememyorderlist:-You can ask the list of your order.Than it can give the list
    Type:-/hi:-It can used to say hi to the bot.    
    Type:-/howareyou  or /howareyou? :- It can used to ask the bot.
    Type:-/whatisyourname:-You can ask the Name of the bot.
    Type:- /goodmorning    or    /GoodMorning
    Type:- /Goodafternoon  or  /goodafternoon
    Type:- /Goodevening    or    /goodevening
    Type:- /Good night      or      /goodnight
    Type:- /Bye            or      /bye
                 ''')
                 
                 
@bot.message_handler(['whocreatethisbot'])
def whocreatethisbot(message):
    bot.reply_to(message,"This bot created by Mohan")   

@bot.message_handler(["Contact"])
def Contact(message):
    bot.reply_to(message,"Please contact on Instagram-->https://instagram.com/code_with_mohan?igshid=MzMyNGUyNmU2YQ==")
    
@bot.message_handler(["Order"])
def  Order(message):
    bot.reply_to(message,"if you want to order than Search  /apple, /banana, /mango, /kiwi, /orange, /pineapple")    

@bot.message_handler(['apple'])
def apple(message):
    # bot.reply_to(message, "Howmany kg's do you need?")
    bot.reply_to(message,"Okay Your order has been placed successfully")

@bot.message_handler(['banana'])
def banana(message):
    # bot.reply_to(message, "Howmany kg's do you need?")
    bot.reply_to(message,"Okay Your order has been placed successfully")
    
@bot.message_handler(['mango'])
def mango(message):
    # bot.reply_to(message, "Howmany kg's do you need?")
    bot.reply_to(message,"Okay Your order has been placed successfully")
    
@bot.message_handler(['kiwi'])
def kiwi(message):
    # bot.reply_to(message, "Howmany kg's do you need?")
    bot.reply_to(message,"Okay Your order has been placed successfully")

@bot.message_handler(['orange'])
def orange(message):
    # bot.reply_to(message, "Howmany kg's do you need?")
    bot.reply_to(message,"Okay Your order has been placed successfully")

@bot.message_handler(['pineapple'])
def pineapple(message):
    # bot.reply_to(message, "Howmany kg's do you need?")
    bot.reply_to(message,"Okay Your order has been placed successfully")

@bot.message_handler(['givememyorderlist'])
def givememyorderlist(message):
     bot.reply_to(message,'''
                  
                  Okay sure,  
                  apple, 
                  banana, 
                  mango, 
                  kiwi, 
                  orange, 
                  pineapple.    
                  ''' )
    
@bot.message_handler(['whatisthepriceofapple'])
def whatisthepriceofapple(message):
    bot.reply_to(message,"The apple price is 20$")



bot.polling()