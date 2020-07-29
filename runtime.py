from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler, CallbackQueryHandler, BasePersistence, PicklePersistence, DictPersistence
from telegram import InlineQueryResultArticle, InputTextMessageContent, ReplyKeyboardMarkup, KeyboardButton
from telegram.error import BadRequest
from token_var import token_updater
from uuid import uuid4
import hashlib
import logging


# Var declaration
persistence = PicklePersistence(filename="persistence_file")

updater = Updater(token=token_updater, use_context=True, persistence=persistence)
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
    context.bot.send_message(chat_id=update.effective_chat.id, text="TestBot von \x40miiiiiYT\n\nDieser Bot kann:\n\n - /start - Um den Chat zu starten.\n - /help - Zeigt diese Nachricht an.\n - /spam - Schickt dir 10 Nachrichten hintereinander.\n - /mychatid - Gibt dir deine Chat-ID zurück. In privaten Chats das gleiche wie die User-ID.\n - /try - Probiere manche Commands aus!\n - /myuserid - Gibt dir deine User-ID zurück. In privaten Chat das gleiche wie die Chat-ID.\n - /credit - Zeigt dir, wer dir den Bot gebracht hat!\n - /hash <Text> - Konvertiert den gegebenen Text mithilfe des SHA256 Algorhythmusses in einen Hash.\n - /put <Wert> - Speichert einen Wert in der Datenbank.\n - /get <UUID> - Ruft einen Wert von der Datenbank ab.\n - /uuidlist - Listet alle UUIDs in der Datenbank auf.\n - /remove <UUID> - Löscht einen Wert aus der Datenbank.\n - Du kannst auch irgendeine Nachricht schreiben(solange es kein /command ist), und der Bot wiederholt sie.\n\nViel Freude!")

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
                KeyboardButton(text="/credit"),
                KeyboardButton(text="/myuserid"),
                KeyboardButton(text="/hash"),
                KeyboardButton(text="/put"),
                KeyboardButton(text="/get"),
                KeyboardButton(text="/uuidlist"),
                KeyboardButton(text="/remove")]]

    reply_keyboard = ReplyKeyboardMarkup(keyboard, rezise_keyboard=True)
    update.message.reply_text('Diese Commands kannst du ausprobieren:\n\n1. /spam\n2. /help\n3. /mychatid\n4. /credit\n5. /myuserid\n6. /hash\n7. /put\n8. /get\n9. /uuidlist\n10. /remove', reply_markup=reply_keyboard)

def getUserID(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Deine User-ID ist:\n" + str(update.effective_user.id))

def credit(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="\U0001F1E9\U0001F1EA\n\nDieser Bot wurde entwickelt von:\n\n\x40miiiiiYT\nMoinMeister\nLennart\n\nGithub:\n" + github_link + "\n\n\U0001F1EC\U0001F1E7\n\nThis bot was developed by:\n\n\x40miiiiiYT\nMoinMeister\nLennart\n\nGithub:\n" + github_link)

def hash(update, context):
    sha = hashlib.sha256()
    try:
        sha.update(str(context.args[0]).encode())
        context.bot.send_message(chat_id=update.effective_chat.id, text="Erfolg! Der Hash von {0} lautet:".format(context.args[0]))
        context.bot.send_message(chat_id=update.effective_chat.id, text=str(sha.hexdigest()))

    except IndexError:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Bitte benutze `/hash <Text>`", parse_mode="Markdown")

def put(update, context):
    key = str(uuid4())
    try:
        value = context.args[0]
    except IndexError:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Bitte benutze `/put <Wert>`", parse_mode="Markdown")

    context.user_data[key] = value

    update.message.reply_markdown("**" + value + "**" + " wurde mit der UUID `{0}` in der Datenbank gespeichert.".format(key))

def get(update, context):
    
    
    try:
        key = context.args[0]
        value = context.user_data[key]
        update.message.reply_markdown("Erfolg! Der Wert von `{0}` lautet:".format(key))
        update.message.reply_text(value)

    except KeyError:
        update.message.reply_text('Wert nicht gefunden.')

    except IndexError:
        update.message.reply_markdown("Bitte benutze `/get <UUID>`")

def uuidlist(update, context):
    try:
        update.message.reply_markdown(list(context.user_data.keys()))
    except BadRequest:
        update.message.reply_text("Du hast noch nichts in der Datenbank gespeichert!")

def remove(update, context):
    try:
        value = context.user_data[context.args[0]]
        key = context.args[0]
        del context.user_data[context.args[0]]
        update.message.reply_markdown("Wert \'{0}\' mit UUID `{1}` wurde gelöscht.".format(value, key))
    except IndexError:
        update.message.reply_markdown("Bitte benutze `/remove <UUID>`!")
    except KeyError:
        update.message.reply_markdown("UUID {0} nicht gefunden.".format(context.args[0]))

def clear(update, context):
        context.user_data.clear()
        update.message.reply_text("Datenbank geleert.")
    
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
hash_handler = CommandHandler('hash', hash)
put_handler = CommandHandler('put', put)
get_handler = CommandHandler('get', get)
uuidlist_handler = CommandHandler('uuidlist', uuidlist)
remove_handler = CommandHandler('remove', remove)
clear_handler = CommandHandler('clear', clear)

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
dispatcher.add_handler(hash_handler)
dispatcher.add_handler(put_handler)
dispatcher.add_handler(get_handler)
dispatcher.add_handler(uuidlist_handler)
dispatcher.add_handler(remove_handler)
dispatcher.add_handler(clear_handler)

# Start Bot
updater.start_polling()
print('Running...')