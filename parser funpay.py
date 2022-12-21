import requests
from bs4 import BeautifulSoup as bs
import time
language = input("введите свой язык/enter your language(only en/ru, только англ/рус): ")
if language == "en":
    URL_TEMPLATE = input("enter the link here: ")
    base = input("which file will be output to(.txt): ")
    it = input("after how many seconds everything will be written out again in .txt: ")


    def parse(url=URL_TEMPLATE):
        global g
        g = int(input("how much to parse the accounts?: "))
        r = requests.get(url)
        soup = bs(r.text, "html.parser")
        accounts_name = soup.find_all("div", class_="tc-desc-text")
        price_account = soup.find_all("div", class_="tc-price")
        print("find accounts:", len(accounts_name), "from them it will be deduced", g)
        with open("baseee.txt", "w", encoding="utf-8") as f:
            for a in range(0, g):
                f.write(accounts_name[a].text)
                f.write(price_account[a + 1].text)
                f.write("\n")
    parse()
    def parse0(url=URL_TEMPLATE):
        global g
        r = requests.get(url)
        soup = bs(r.text, "html.parser")
        accounts_name = soup.find_all("div", class_="tc-desc-text")
        price_account = soup.find_all("div", class_="tc-price")
        print("find accounts:", len(accounts_name), "from them it will be deduced", g)
        with open(base, "w", encoding="utf-8") as f:
            for a in range(0, g):
                f.write(accounts_name[a].text)
                f.write(price_account[a + 1].text)
                f.write("\n")

    while True:
        time.sleep(1)
        parse0()


if language == "ru":
    import requests
    from bs4 import BeautifulSoup as bs
    import time

    URL_TEMPLATE = input("введи ссылку, пример: 'https://funpay.com/!!LOTS!!/x': ")
    base = input(
        "введи имя файла(.txt) в которое будет вписано все что спарсилось иначе программа сама создаст его с именем которое ты ввел: ")
    it = input("число которое ты введешь будет являтся секундами которые повлияют на обновление .txt: ")


    def parse(url=URL_TEMPLATE):
        global g
        g = int(input("сколько аккаунтов ты хочешь спарсить?: "))
        r = requests.get(url)
        soup = bs(r.text, "html.parser")
        accounts_name = soup.find_all("div", class_="tc-desc-text")
        price_account = soup.find_all("div", class_="tc-price")
        print("нашло аккаунтов:", len(accounts_name), "будет выписано только:", g)
        with open("baseee.txt", "w", encoding="utf-8") as f:
            for a in range(0, g):
                f.write(accounts_name[a].text)
                f.write(price_account[a + 1].text)
                f.write("\n")


    parse()


    def parse0(url=URL_TEMPLATE):
        global g
        r = requests.get(url)
        soup = bs(r.text, "html.parser")
        accounts_name = soup.find_all("div", class_="tc-desc-text")
        price_account = soup.find_all("div", class_="tc-price")
        print("нашло аккаунтов:", len(accounts_name), "будет выписано только:", g)
        with open(base, "w", encoding="utf-8") as f:
            for a in range(0, g):
                f.write(accounts_name[a].text)
                f.write(price_account[a + 1].text)
                f.write("\n")


    while True:
        time.sleep(1)
        parse0()

else:
    print("there is no such language")