# Generated by Django 2.2.3 on 2019-07-23 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slot',
            options={'ordering': ['pk']},
        ),
        migrations.AddField(
            model_name='customer',
            name='eta',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]