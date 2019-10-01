# Generated by Django 2.1.1 on 2019-09-30 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BafosApp', '0010_historicaltracking_tracking'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaltracking',
            name='name',
            field=models.CharField(default='default_poll', max_length=50, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='mtemplate',
            name='name',
            field=models.CharField(default='default_template', max_length=50, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='tracking',
            name='name',
            field=models.CharField(default='default_poll', max_length=50, verbose_name='Name'),
        ),
    ]
