# Generated by Django 3.1.5 on 2021-02-26 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0022_auto_20210226_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_master',
            name='id_proof',
        ),
    ]
