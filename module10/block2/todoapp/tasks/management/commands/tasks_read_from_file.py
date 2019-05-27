# coding: utf-8
from django.core.management import BaseCommand
from datetime import datetime
from tasks.models import TodoItem

class Command(BaseCommand):
    help = u"Read tasks from file (one line = one task)and save them to db"

    def add_arguments(self, parser):
        parser.add_argument('--file', dest='input_file', type=str)

    def handle(self, *args, **options):
        with open(options['input_file'], "r", encoding='utf-8') as fp:
            for line in fp:
                t = TodoItem(description=line)
                t.save()
            