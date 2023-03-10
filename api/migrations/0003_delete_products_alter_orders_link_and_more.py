# Generated by Django 4.1 on 2022-11-17 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_orders_services_delete_products'),
    ]

    operations = [

        migrations.AlterField(
            model_name='orders',
            name='link',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='orders',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orders',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.services', verbose_name='service'),
        ),
    ]
