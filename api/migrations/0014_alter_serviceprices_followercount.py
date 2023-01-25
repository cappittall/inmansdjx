# Generated by Django 4.1.5 on 2023-01-16 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_serviceprices_followercount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceprices',
            name='followerCount',
            field=models.CharField(choices=[('0-100', '0-100'), ('100-500', '100-500'), ('500-1000', '500-1000'), ('1000-3000', '1000-3000'), ('3000-5000', '3000-5000'), ('5000- ??', '5000- ??')], default='0-100', max_length=10),
        ),
    ]
