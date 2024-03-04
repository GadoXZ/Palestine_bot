from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler,MessageHandler,filters, ContextTypes 
#to do list : 1-menu to select time period 2-menu to select characters,events and myrters 3-linking the choices to text containing info
Token: Final ='6487838705:AAGd-ANCIoXl1y5Rl8Wf9iMAjhxVNB1T_U8'
BOT_USERNAME:Final='@Gado0001bot'

#commands
async def start_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Welcome to palestine History bot you can learn the truth regarding palestine during different time periods')
async def help_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('this bot is made to give you info about palestine history to use it choose an info type highlighted bu" "')    


# text responses 
def handle_response(text:str) -> str :
    print(f'What would you like to learn about?\n')
    print(f'1."important events"\n2."characters"\n3."martyrs"')
    if 'important events' in text :  
        result = Time_period (text)
        return result
    if 'characters' in text:
        result = Time_period(text)
        return result 
    if 'martyrs'in text:
        result = Time_period(text)
        return result
    return "please choose an info type form the highlighted ones"
    
def Time_period(infotype:str):
    print (f'select the time period\n1."2002-2016"\n"2.2016-2024"')
    period = update.message.text
    if period == '2002-2016':
        if infotype == 'important events':
            return 'important events' #insert real info here after finishing the code
        elif infotype == 'characters':
            return 'characters'       #insert real info here after finishing the code
        elif infotype == ' martyrs':
            return 'martyrs'          #insert real info here after finishing the code
    elif period == '2016-2024':
        if infotype == 'important events':
            return 'important events'
        elif infotype == 'characters':
            return 'characters'
        elif infotype == ' martyrs':
            return 'martyrs'
if __name__=='__telegram__':
    app=Application.builder().token(Token).build()
    
    #adding the commands created above
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    
    #adding the responses created above in the app
    app.add_handler(MessageHandler(filters.TEXT,handle_response))
    
    #new message check
    app.run_polling(poll_interval=5)
            