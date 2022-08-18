# Generated by Django 4.0.4 on 2022-07-31 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='stadiums',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('tier', models.CharField(max_length=10)),
                ('seats', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]