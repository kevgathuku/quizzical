# Generated by Django 2.2.1 on 2019-06-02 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0003_auto_20190602_1333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
    ]
