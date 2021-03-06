# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 19:07
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('start_date', models.DateField(auto_now_add=True, verbose_name='Inicio Membresía')),
                ('paid_amount', models.FloatField(default=100, verbose_name='Monto Pagado')),
            ],
            options={
                'verbose_name': 'Membresía',
                'db_table': 'demo_membership',
                'ordering': ('start_date',),
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
