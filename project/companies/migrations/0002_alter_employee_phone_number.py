# Generated by Django 4.0 on 2022-07-27 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.IntegerField(blank=True, max_length=255),
        ),
    ]
