# Generated by Django 3.2.9 on 2021-11-22 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20211111_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=64, verbose_name='Имя')),
                ('phone_number', models.CharField(max_length=12, verbose_name='Номер телефона')),
                ('email', models.CharField(max_length=128, verbose_name='Электронная почта')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('date', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
    ]