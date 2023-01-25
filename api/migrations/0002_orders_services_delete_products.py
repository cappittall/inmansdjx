# Generated by Django 4.1 on 2022-11-17 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('key', models.CharField(max_length=50)),
                ('action', models.CharField(max_length=50)),
                ('service', models.IntegerField()),
                ('link', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('runs', models.CharField(blank=True, max_length=200)),
                ('interval', models.CharField(blank=True, max_length=200)),
                ('comments', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('service', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('type', models.CharField(default='Default', max_length=200)),
                ('category', models.CharField(blank=True, max_length=200)),
                ('rate', models.FloatField()),
                ('min', models.IntegerField(default=1)),
                ('max', models.IntegerField(default=99999)),
                ('dripfeed', models.BooleanField(default=False)),
                ('refill', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Servisler',
            },
        ),
        
    ]