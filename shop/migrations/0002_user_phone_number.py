# Generated by Django 3.2.9 on 2021-11-06 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default=999, max_length=12),
            preserve_default=False,
        ),
    ]