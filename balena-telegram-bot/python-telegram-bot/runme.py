from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler, CallbackQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent, ReplyKeyboardMarkup, KeyboardButton
from token_var import token_updater
import logging

# TODO
# Todo now on Trello

# Var declaration
updater = Updater(token=token_updater, use_context=True)
dispatcher = updater.dispatcher

tableflip = "(╯°□°）╯︵ ┻━┻"

github_link = "https://github.com/miiiiiYT/telegram-bot-balena"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)




# Functions
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hallo, ich bin ein Roboter, bitte rede mit mir, und schreibe mir /help!")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def spam(update, context):
    i = 0
    while i < 10:
        i = i + 1
        f = "spam " + str(i)
        context.bot.send_message(chat_id=update.effective_chat.id, text=f)

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="TestBot von \x40miiiiiYT\n\nDieser Bot kann:\n\n - /start - Um den Chat zu starten.\n - /help - Zeigt diese Nachricht an.\n - /spam - Schickt dir 10 Nachrichten hintereinander.\n - /mychatid - Gibt dir deine Chat-ID zurück. In privaten Chats das gleiche wie die User-ID.\n - /try - Probiere manche Commands aus!\n - /myuserid - Gibt dir deine User-ID zurück. In privaten Chat das gleiche wie die Chat-ID.\n - /credit - Zeigt dir, wer dir den Bot gebracht hat!\n - Du kannst auch irgendeine Nachricht schreiben(solange es kein /command ist), und der Bot wiederholt sie.\n\nViel Freude!")

def getChatId(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Deine Chat-ID ist:\n" + str(update.effective_chat.id))

def command(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Dieser Command macht nichts!\n" + tableflip)

def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Deine Nachricht in Caps: ' + str(query.upper()),
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)

def caps(update, context):
        try:
            text_caps = ' '.join(context.args).upper()
            context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)
        except BaseException as e:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Du musst Argumente angeben! Error: {0}".format(e))
        except:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, aber etwas ist schiefgelaufen.")

def try_command(update, context):
    keyboard = [[KeyboardButton(text="/spam"),
                KeyboardButton(text="/help"),
                KeyboardButton(text="/mychatid"),
                KeyboardButton(text="/credit")]]

    reply_keyboard = ReplyKeyboardMarkup(keyboard, rezise_keyboard=True, one_time_keyboard=True)
    update.message.reply_text('Diese Commands kannst du ausprobieren:\n\n1. /spam\n2. /help\n3. /mychatid\n4. /credit', reply_markup=reply_keyboard)

def getUserID(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Deine User-ID ist:\n" + str(update.effective_user.id))

def credit(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="\U0001F1E9\U0001F1EA\n\nDieser Bot wurde entwickelt von:\n\n\x40miiiiiYT\nMoinMeister\nLennart\n\nGithub:\n" + github_link + "\n\n\U0001F1EC\U0001F1E7\n\nThis bot was developed by:\n\n\x40miiiiiYT\nMoinMeister\nLennart\n\nGithub:\n" + github_link)

# Handler declaration
start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
spam_handler = CommandHandler('spam', spam)
help_handler = CommandHandler('help', help)
chatId_handler = CommandHandler('mychatid', getChatId)
command_shrug_handler = CommandHandler('command', command)
inline_caps_handler = InlineQueryHandler(inline_caps)
caps_handler = CommandHandler('caps', caps)
try_handler = CommandHandler('try', try_command)
userId_handler = CommandHandler('myuserid', getUserID)
credit_handler = CommandHandler('credit', credit)

# Add Handlers to Updater.dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(spam_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(chatId_handler)
dispatcher.add_handler(command_shrug_handler)
dispatcher.add_handler(inline_caps_handler)
dispatcher.add_handler(caps_handler)
dispatcher.add_handler(try_handler)
dispatcher.add_handler(userId_handler)
dispatcher.add_handler(credit_handler)

# Start Bot
updater.start_polling()