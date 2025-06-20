# Generated by Django 5.1.6 on 2025-06-16 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название меню')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название пункта')),
                ('url', models.CharField(blank=True, max_length=255, null=True, verbose_name='Явный URL')),
                ('named_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='Именованный URL')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='menu_app.menu', verbose_name='Меню')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='menu_app.menuitem', verbose_name='Родительский пункт')),
            ],
            options={
                'verbose_name': 'Пункт меню',
                'verbose_name_plural': 'Пункты меню',
            },
        ),
    ]
