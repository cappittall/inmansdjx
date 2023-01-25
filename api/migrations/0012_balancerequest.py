# Generated by Django 4.1.5 on 2023-01-16 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0011_alter_orders_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.005)),
                ('status', models.BooleanField(default=False, max_length=50)),
                ('time_stampt', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BalanceRequests', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Balance Requests',
                'ordering': ('-id',),
            },
        ),
    ]