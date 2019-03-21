from datetime import timedelta, datetime as dt
from db import query_user_last_seen, list_users
import time

def second(sec):
    if sec > 4 and sec!=1:
        word = " секунд "
    elif sec == 1:
        word = " секунду "
    else:
        word = " секунды "
    return str(sec) + word

def check_user_is_active(username):
    last_seen=query_user_last_seen(username)
    if last_seen+timedelta(days=180)>=dt.now():
        return True
    else:
        return False  

def get_email_from_user(attempts=3, sleep_duration=10):
    email = input("Введите e-mail: ")
    i = 1
    while (email.find("@") == -1):
        print("неправильный email. Попробуйте ещё раз")
        i = i + 1
        email = input("Попытка " + str(i) + ". Введите e-mail: ")
        if i % attempts == 0:
            while sleep_duration>0:
                print("Переборщили с попытками. Подождите " + second(sleep_duration))
                time.sleep(1)
                sleep_duration = sleep_duration - 1
    return email  

username = get_email_from_user().split("@")[0].lower()
registered_users = list_users()
user_will_active = (dt.now()+timedelta(days=180)).date()
if username in registered_users[0]:
    if check_user_is_active(username):
        print("Ваш аккаунт подтвержден до " + str(user_will_active))
    else:
        print("Вам надо подтвердить логин")   
else:
    print("Вы с нами совсем недавно! Добро пожаловать")
