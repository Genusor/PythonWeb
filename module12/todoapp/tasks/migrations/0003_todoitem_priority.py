# Generated by Django 2.1.5 on 2019-07-08 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_todoitem_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='priority',
            field=models.IntegerField(choices=[(1, 'Высокий приоритет'), (2, 'Средний приоритет'), (3, 'Низкий приоритет')], default=2, verbose_name='Приоритет'),
        ),
    ]
