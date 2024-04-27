import requests
from re import *
import datetime


def tarikh():
    now = datetime.datetime.today()
    mm = str(now.month)
    dd = str(now.day)
    yyyy = str(now.year)
    hour = str(now.hour)
    mi = str(now.minute)
    ss = str(now.second)
    tarikh = (
        '\n\n🗓 Date:  {} / {} / {}   {}:{}:{}'.format(
            "<code>" + yyyy + "</code>",
            "<code>" + mm + "</code>", "<code>" + dd + "</code>",
            "<code>" + hour + "</code>",
            "<code>" + mi + "</code>", "<code>" + ss + "</code>")
    )
    return tarikh


def CoinPrice(query):
    headers = {'User-agent': 'Kavim API'}
    req = requests.get(
        "https://kavim.ir/api/internalUsage757575/{}".format(query),
        headers=headers)
    b = req.json()
    print("req in coin price")

    try:
        if b['success'] == False:
            return False
        else:
            if b['type'] == "crypto":
                # در اعداد بزرگ تر از یک تابع رند استفاده شده است
                if float(b['USD']['lastPrice']) > float(1):
                    image = b["image"]
                    result = (
                        "♦️ Symbol: {}\n\n💰 Last Price: {}\n{}\n\n🔺 High Price: {}\n🔻 Low Price: {}"
                        .format("<code>" + b['symbol'] + "</code>",
                                "<code>" + f"${round(float(b['USD']['lastPrice']), 2):,}" + "</code>",
                                "<code>" + f"{round(float(b['IRT']['lastPrice'])):,}" + " تومان" + "</code>",
                                "<code>" + f"${round(float(b['USD']['highPrice']), 2):,}" + "</code>",
                                "<code>" + f"${round(float(b['USD']['lowPrice']), 2):,}" + "</code>"))
                    return result, image
                    # رند نکردن اعداد زیر 1 به دلیل 0 شدن
                elif float(b['USD']['lastPrice']) <= float(1):
                    image = b["image"]
                    result = (
                        "♦️ Symbol: {}\n\n💰 Last Price: {}\n{}\n\n🔺 High Price: {}\n🔻 Low Price: {}"
                        .format("<code>" + b['symbol'] + "</code>",
                                "<code>" + "$" + b['USD'][
                                    'lastPrice'] + "</code>",
                                "<code>" + f"{round(float(b['IRT']['lastPrice']), 2):,}" + " تومان" + "</code>",
                                "<code>" + "$" + b['USD'][
                                    'highPrice'] + "</code>",
                                "<code>" + "$" + b['USD'][
                                    'lowPrice'] + "</code>"))
                    return result, image

            elif b['type'] == "money":
                image = "images/kavim-logo.png"
                result = (
                    "♦️ Symbol: {}\n\n💰 Last Price: {}\n\n📈 Change Value: {} ({})\n\n🔺 HighPrice: {}\n🔻 Low Price: {}\n\n🧮 Last price update: {}"
                    .format("<code>" + b['symbol'] + "</code>",
                            "<code>" + f"{b['lastPrice']:,}" + "</code>",
                            "<code>" + f"{b['change_value']:,}" + "</code>",
                            "<code>" + f"{b['change_percent']}" + "%" + "</code>",
                            "<code>" + f"{b['highPrice']:,}" + "</code>",
                            "<code>" + f"{b['lowPrice']:,}" + "</code>",
                            "<code>" + b['time'] + "</code>"))
                return result, image
    except:
        result = ("{} Was not found".format(query))
        return result


def wallet_address(query):
    try:
        headers = {'User-agent': 'Kavim API'}
        req = requests.get(
            "https://kavim.ir/api/internalUsage757575/{}".format(query),
            headers=headers)
        b = req.json()
        if b['success'] == False:
            return False
        else:
            result = (
                "♦️ Coin: {}\n\n📍 Address: {}\n\n📥️ Total Received: {}\n\n📤 Total Sent: {}\n\n⚖️ Final Balance: {}"
                .format("<code>" + b['coin'] + "</code>",
                        "<code>" + query + "</code>",
                        "<code>" + str(b['total_received']) + "</code>",
                        "<code>" + str(b["total_sent"]) + "</code>",
                        "<code>" + str(b['final_balance']) + "</code>"))
            return result
    except:
        result = ("Wallet address was not found")
        return result


def Transaction_hash(query):
    try:
        headers = {'User-agent': 'Kavim API'}
        req = requests.get(
            "https://kavim.ir/api/internalUsage757575/{}".format(query),
            headers=headers)
        b = req.json()
        date = findall(r"(^.*)T", str(b['confirmed']))[0]
        time = findall(r"T(.*)Z", str(b['confirmed']))[0]
        result = ("📌 Hash: {}\n\n❗️ Total: {}\n\n✅ Confirmed: {}   {}".format(
            "<code>" + str(b['hash']) + "</code>",
            "<code>" + str(b['total']) + "</code>",
            "<code>" + str(date) + "</code>", "<code>" + str(time) + "</code>"))
        return result
    except:
        return False


# ارور زبان
def Language_Error(query):
    c = ("لطفا درخواست خود را به زبان انگلیسی وارد کنید")
    return c
