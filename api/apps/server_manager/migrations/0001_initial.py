# Generated by Django 3.0.8 on 2020-07-11 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificated at')),
                ('server_ip', models.GenericIPAddressField()),
                ('server_name', models.CharField(default='k6z4EUEz', max_length=16)),
                ('is_connected', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('WR', 'WORKING'), ('PS', 'PAUSED'), ('ST', 'STOPPED')], default='ST', max_length=2)),
            ],
            options={
                'verbose_name': 'Servers',
                'verbose_name_plural': 'Servers',
                'db_table': 'server',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='ServerConnection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssh_username', models.CharField(max_length=64)),
                ('ssh_password', models.CharField(max_length=256)),
                ('server', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='server_manager.Server')),
            ],
            options={
                'verbose_name': 'Server connections',
                'verbose_name_plural': 'Server connections',
                'db_table': 'server_connection',
            },
        ),
    ]
