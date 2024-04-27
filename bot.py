from telegram import *
from telegram.ext import *
from DataBase import *
from uuid import uuid4
from functions import *
from create_database import *

Updater = Updater("YOUR-Token_bot")
dis = Updater.dispatcher


def start(update, callback: CallbackContext):
    Chat_type = update.message.chat.type
    if Chat_type == 'private':
        firstname = update.message.from_user.first_name
        username = update.message.from_user.username
        lastname = update.message.from_user.last_name
        name = firstname + lastname if lastname != None else firstname
        user_id = update.message.from_user.id
        languagecode = update.message.from_user.language_code
        profile = Updater.bot.get_user_profile_photos(user_id)
        image = profile['photos'][0][0]['file_id']

        users(
            name=name,
            image=image,
            username=username,
            user_id=user_id,
            languagecode=languagecode
        )

        update.message.reply_text(("""سلام  {}  عزیز به کاوشگر کاویم خوش امدی.

🔷 کاویم یک موتور جستجو برای حوزه های مالیه، میتونی والت آدرس، هش آدرس و یا نماد یک کوین رو جستجو کنی تا اطلاعاتش رو ببینی.

🔹 برای شروع اینارو امتحان کن:

🔸Coin: 
/p BTC or usd

🔸Wallet adress:
/w 34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo

🔸Transaction hash:
/h f854aebae95150b379cc1187d848d58225f3c4157fe992bcd166f58bd5063449


    اطلاعات بیشتر رو میتونی تو سایت {} ببینی
    
    """).format("<a href='tg://user?id={}'>{}</a>",
                "<a href='https://www.kavim.ir'>{}</a>").format(user_id,
                                                                firstname,
                                                                "کاویم"),
                                  parse_mode=ParseMode.HTML)


def data_gp(update, contaxt: CallbackContext):
    chat_title = update.message.chat.title
    chat_type = update.message.chat.type
    chat_id = update.message.chat_id
    chat_username = update.message.chat.username
    count_chat = Updater.bot.get_chat_members_count(chat_id)

    groups_database(
        name=chat_title,
        count_chat=count_chat,
        chat_type=chat_type,
        numerical_id=chat_id,
        chat_username=chat_username)


def inlinequery(update, context: CallbackContext):
    query = update.inline_query.query
    query = query.strip()
    if query != "" and query != None and query != " ":
        # انگلیسی بودن درخواست
        if query.isascii() == True:
            count_query = len(query)

            if count_query == 34:
                req = wallet_address(query)

                if req == False:
                    results = [InlineQueryResultArticle(id=uuid4(),
                                                        title="{}".format(
                                                            query),
                                                        input_message_content=InputTextMessageContent(
                                                            "Wallet not found"))]
                    update.inline_query.answer(results, cache_time=10)

                else:
                    keyboard = [[InlineKeyboardButton("moro information", url=(
                        "https://kavim.ir/info/{}").format(query))], ]
                    reply_markup = InlineKeyboardMarkup(keyboard)
                    date = tarikh()
                    photo_url = "https://api.qrserver.com/v1/create-qr-code/?data={}&size=500x500&margin=20&format=jpg".format(
                        query)
                    thumb_height = 10
                    thumb_width = 15
                    results = [InlineQueryResultPhoto(id=uuid4(),
                                                      title="{}".format(
                                                          'wallet address'),
                                                      type="photo",
                                                      thumb_url=photo_url,
                                                      thumb_height=thumb_height,
                                                      thumb_width=thumb_width,
                                                      photo_url=photo_url,
                                                      caption="{}".format(
                                                          req) + date,
                                                      parse_mode=ParseMode.HTML,
                                                      reply_markup=reply_markup)]
                    update.inline_query.answer(results)

            elif count_query == 64:
                req = Transaction_hash(query)
                if req == False:
                    results = [InlineQueryResultArticle(id=uuid4(),
                                                        title="{}".format(
                                                            query),
                                                        input_message_content=InputTextMessageContent(
                                                            "Transaction hash was not found"))]
                    update.inline_query.answer(results, cache_time=10)
                else:
                    date = tarikh()
                    keyboard = [[InlineKeyboardButton("moro information",
                                                      url=(
                                                          "https://kavim.ir/info/{}").format(
                                                          query))]]
                    reply_markup = InlineKeyboardMarkup(keyboard)

                    results = [InlineQueryResultArticle(id=uuid4(),
                                                        title="{}".format(
                                                            'Transaction hash'),
                                                        input_message_content=InputTextMessageContent(
                                                            req + date,
                                                            parse_mode=ParseMode.HTML),
                                                        reply_markup=reply_markup)]
                    update.inline_query.answer(results)

            else:
                keyboard = [
                    [InlineKeyboardButton("Refresh", callback_data=f"{query}")],
                    [InlineKeyboardButton("more information", url=(
                        "https://kavim.ir/info/{}").format(query))],
                ]
                reply_markup = InlineKeyboardMarkup(keyboard)
                req = CoinPrice(query)

                if req == False:
                    results = [InlineQueryResultArticle(id=uuid4(),
                                                        title="{}".format(
                                                            query),
                                                        input_message_content=InputTextMessageContent(
                                                            "Coin not found"))]
                    update.inline_query.answer(results, cache_time=10)
                else:
                    date = tarikh()
                    thumb_url = "https://kavim.ir/{}".format(req[1])
                    thumb_height = 10
                    thumb_width = 15
                    results = [InlineQueryResultArticle(id=uuid4(),
                                                        title="{}".format(
                                                            query),
                                                        thumb_url=thumb_url,
                                                        thumb_height=thumb_height,
                                                        thumb_width=thumb_width,
                                                        input_message_content=InputTextMessageContent(
                                                            req[0] + date,
                                                            parse_mode=ParseMode.HTML),
                                                        reply_markup=reply_markup)]
                    update.inline_query.answer(results, cache_time=10)
        # اگر درخواست فارسی بود
        else:
            results = [InlineQueryResultArticle(id=uuid4(), title="{}".format(
                'Language Error'),
                                                input_message_content=InputTextMessageContent(
                                                    Language_Error(query)))]
            update.inline_query.answer(results)


def edite_price(update, context: CallbackContext):
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("Refresh", callback_data=f'{query.data}')],
        [InlineKeyboardButton(
            "more information",
            url=("https://kavim.ir/info/{}").format(query.data))],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    req = CoinPrice(query.data)
    date = tarikh()
    edited_text = req[0] + date
    query.edit_message_text(text=f"{edited_text}", parse_mode=ParseMode.HTML,
                            reply_markup=reply_markup)


def Coin_Command(update, context: CallbackContext):
    text = update.message.text
    query = (text[3:])
    query = query.strip()
    print(query)
    if query != "" and query != None and query != " ":
        if query.isascii() == True:
            coinprice = CoinPrice(query)
            try:
                keyboard = [
                    [InlineKeyboardButton("Refresh", callback_data=f"{query}")],
                    [InlineKeyboardButton("more information", url=(
                        "https://kavim.ir/info/{}").format(query))],
                ]
                reply_markup = InlineKeyboardMarkup(keyboard)
                update.message.reply_text(
                    text=("{}{}").format(coinprice[0], tarikh()),
                    parse_mode=ParseMode.HTML, reply_markup=reply_markup)
            except:
                update.message.reply_text("Coin was not found")
        else:
            update.message.reply_text(
                "لطفا درخواست خود را به زبان انگلیسی وارد کنید.")


def wallet_Command(update, context: CallbackContext):
    chat_id = update.message.chat.id
    text = update.message.text
    message_id = update.message.message_id
    query = (text[3:])
    wallet = wallet_address(query)
    keyboard = [[InlineKeyboardButton("moro information",
                                      url=("https://kavim.ir/info/{}").format(
                                          query))], ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if wallet == False:
        update.message.reply_text("Wallet address was not found")
    else:
        photo = "https://api.qrserver.com/v1/create-qr-code/?data={}&size=500x500&margin=20&format=jpg".format(
            query)
        Updater.bot.send_photo(chat_id, photo, wallet + tarikh(),
                               parse_mode=ParseMode.HTML,
                               reply_to_message_id=message_id,
                               reply_markup=reply_markup)


def hash_Command(update, context: CallbackContext):
    text = update.message.text
    query = (text[3:])
    hash = Transaction_hash(query.strip())
    if hash == False:
        update.message.reply_text("Transaction hash was not found")
    else:
        keyboard = [[InlineKeyboardButton("moro information", url=(
            "https://kavim.ir/info/{}").format(query))], ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(text=("{}{}").format(hash, tarikh()),
                                  parse_mode=ParseMode.HTML,
                                  reply_markup=reply_markup)


def creat_database(update, context: CallbackContext):
    user_id = update.message.from_user.id
    if user_id == 297214696:
        start_database()
        print("database created.")


print('bot statrted')
dis.add_handler(CallbackQueryHandler(edite_price))
dis.add_handler(CommandHandler("creat_database", creat_database))
dis.add_handler(MessageHandler(Filters.chat_type.groups, data_gp), group=2)
dis.add_handler(CommandHandler("start", start))
dis.add_handler(CommandHandler("p", Coin_Command))
dis.add_handler(CommandHandler("h", hash_Command))
dis.add_handler(CommandHandler("w", wallet_Command))
dis.add_handler(InlineQueryHandler(inlinequery))
Updater.start_polling()
Updater.idle()
