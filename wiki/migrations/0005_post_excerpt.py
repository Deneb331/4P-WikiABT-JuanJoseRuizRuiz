# Generated by Django 3.2.18 on 2023-03-29 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0004_auto_20230322_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='excerpt',
            field=models.CharField(default='This is a default excerpt', max_length=300),
        ),
    ]
