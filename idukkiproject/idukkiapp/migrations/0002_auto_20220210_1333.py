# Generated by Django 3.2.12 on 2022-02-10 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idukkiapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='how_many',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='leaving',
            field=models.DateTimeField(),
        ),
    ]
