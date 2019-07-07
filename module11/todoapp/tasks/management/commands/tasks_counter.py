# coding: utf-8
from django.core.management import BaseCommand
from tasks.models import TodoItem
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = u"считает количество задач на каждого пользователя и выводит топ-25 пользователей в базе с числом их тасок: выполненных и невыполненных."

    def handle(self, *args, **options):
        #1
        mas={}
        mas_uncomp={}
        count1=0
        for u in User.objects.all():
            count3=0
            count2=0
            for t in u.tasks.all():
                if t.is_completed:
                    count1+=1
                else:
                    count2+=1
                    mas_uncomp[u]=count2
                count3+=1
            mas[u]=count3
        print(count1)
        
        #2 
        list_d = list(mas.items())
        list_d.sort(key=lambda i: i[1])
        print(list_d[-5])

        #3
        count4=0
        for s in mas_uncomp.items():
            if s[1]< 20:
                count4+=1
        print(count4)
        #4
        list_d = list(mas_uncomp.items())
        list_d.sort(key=lambda i: i[1])
        print(list_d[-2])