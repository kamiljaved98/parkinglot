# Generated by Django 2.2.3 on 2019-07-25 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_auto_20190724_1034'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dailyrecord',
            options={'ordering': ['-date']},
        ),
    ]
