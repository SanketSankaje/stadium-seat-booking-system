# Generated by Django 3.1.3 on 2020-12-05 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
