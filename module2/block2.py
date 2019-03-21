import time
import os
def second(sec):
    if sec > 4 and sec!=1:
        return " секунд "
    elif sec == 1:
        return " секунду "
    else:
        return " секунды "

email = input("Введите e-mail ")
i = 0
restart = False
while email.find("@") == -1:
    if restart:
        email = input("Снова введите e-mail ")
        restart = False
        i = -1
    else:  
        print("неправильный email. Попробуйте еще раз")
        email = input("Введите e-mail ")
    i = i + 1
    if i==2:
        j = 5
        while j != 0:
            print("Превышено допустимое количество ошибок, подождите " + str(j) + second(j) +"и попробуйте снова")
            time.sleep(1)
            j = j - 1
            #os.system('cls')
            restart = True