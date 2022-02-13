# Generated by Django 3.2.12 on 2022-02-10 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idukkiapp', '0003_auto_20220210_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('locname', models.CharField(max_length=250)),
                ('desc', models.TextField()),
            ],
        ),
    ]
