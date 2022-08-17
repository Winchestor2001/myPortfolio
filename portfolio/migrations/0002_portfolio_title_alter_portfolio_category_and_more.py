# Generated by Django 4.1 on 2022-08-05 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='category',
            field=models.CharField(choices=[('Web Site', 'Web'), ('Telegram Bot', 'TgBot'), ('Other', 'Other')], max_length=100),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='category_2',
            field=models.CharField(choices=[('Web', 'Web'), ('TgBot', 'TgBot'), ('Other', 'Other')], max_length=100, null=True),
        ),
    ]
