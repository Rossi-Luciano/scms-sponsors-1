# Generated by Django 3.2.12 on 2022-07-06 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtaildocs', '0012_uploadeddocument'),
    ]

    operations = [
        migrations.CreateModel(
            name='SponsorNamesStandardizedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last update date')),
                ('is_valid', models.BooleanField(blank=True, default=False, null=True, verbose_name='É valido?')),
                ('line_count', models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantidade de linhas')),
                ('attachment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document')),
                ('creator', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='sponsornamesstandardizedfile_creator', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sponsornamesstandardizedfile_last_mod_user', to=settings.AUTH_USER_MODEL, verbose_name='Updater')),
            ],
            options={
                'verbose_name_plural': 'Sponsor Name Standardized Upload',
            },
        ),
        migrations.CreateModel(
            name='SponsorNamesStandardized',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last update date')),
                ('sponsor_id', models.IntegerField(null=True, verbose_name='ID')),
                ('sponsor_name_std', models.CharField(blank=True, max_length=255, null=True, verbose_name='Standard Name')),
                ('sponsor_acron_std', models.CharField(blank=True, max_length=255, null=True, verbose_name='Standard Acronym')),
                ('creator', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='sponsornamesstandardized_creator', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sponsornamesstandardized_last_mod_user', to=settings.AUTH_USER_MODEL, verbose_name='Updater')),
            ],
            options={
                'verbose_name_plural': 'Sponsor Name Standardized',
            },
        ),
    ]