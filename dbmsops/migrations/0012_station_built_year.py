# Generated by Django 4.1.3 on 2022-11-24 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbmsops', '0011_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='built_year',
            field=models.IntegerField(default=2022),
        ),
    ]