# Generated by Django 4.1 on 2022-10-14 12:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicePrices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usersToFollow', models.FloatField(default=0.005)),
                ('postLikes', models.FloatField(default=0.005)),
                ('postComments', models.FloatField(default=0.005)),
                ('postSaves', models.FloatField(default=0.005)),
                ('commentLikes', models.FloatField(default=0.005)),
                ('reelsLikes', models.FloatField(default=0.005)),
                ('reelsComments', models.FloatField(default=0.005)),
                ('igTVLikes', models.FloatField(default=0.005)),
                ('igTVComments', models.FloatField(default=0.005)),
                ('liveBroadCastLikes', models.FloatField(default=0.005)),
                ('liveBroadCastComments', models.FloatField(default=0.005)),
                ('liveWatches', models.FloatField(default=0.005)),
                ('postShares', models.FloatField(default=0.005)),
                ('suicideSpams', models.FloatField(default=0.005)),
                ('storyShares', models.FloatField(default=0.005)),
                ('videoShares', models.FloatField(default=0.005)),
                ('singleUserDMs', models.FloatField(default=0.005)),
                ('multiUserDMs', models.FloatField(default=0.005)),
                ('spams', models.FloatField(default=0.005)),
                ('time_stampt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Birim Fiyatlar',
            },
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, default='', max_length=20)),
                ('birth_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('tc', models.CharField(blank=True, default='', max_length=15)),
                ('iban', models.CharField(blank=True, default='TR', max_length=50)),
                ('bank', models.CharField(blank=True, default='Banka', max_length=50)),
                ('coin', models.CharField(blank=True, default='USDT - TRC20 (Tron network) Addresi!', max_length=50)),
                ('coin_adresi', models.CharField(blank=True, default='', max_length=50)),
                ('info', models.JSONField(blank=True, default=dict, null=True)),
                ('place', models.JSONField(blank=True, default=dict, null=True)),
                ('is_online', models.BooleanField(default=False)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='profil_fotoları/%Y/%m/')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Profiller',
            },
        ),
        migrations.CreateModel(
            name='InstagramAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('userName', models.CharField(default='', max_length=250)),
                ('password', models.CharField(default='', max_length=250)),
                ('pwdPassword', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('claim', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('authToken', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('csrftoken', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('rur', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('dsUserID', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('sessionID', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('mid', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('ghost', models.BooleanField(default=False)),
                ('gender', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('country', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('adminArea', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('locality', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('subLocality', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instagram', to='api.profil')),
            ],
            options={
                'verbose_name_plural': 'instagram',
            },
        ),
        migrations.CreateModel(
            name='EarnList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation_id', models.CharField(blank=True, max_length=50, null=True)),
                ('type', models.CharField(blank=True, max_length=50, null=True)),
                ('pdflink', models.CharField(blank=True, max_length=200, null=True)),
                ('amount', models.FloatField(default=0.005)),
                ('ghost', models.BooleanField(default=False)),
                ('operation_data', models.JSONField(default=dict, unique=True)),
                ('time_stampt', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Kazanclar', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Kazanc Tablosu',
                'ordering': ('-id',),
            },
        ),
    ]