# Generated by Django 4.0 on 2022-07-27 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_alter_employee_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.IntegerField(blank=True),
        ),
    ]
