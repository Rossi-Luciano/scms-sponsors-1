# Generated by Django 3.2.12 on 2022-07-06 23:27

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
            name='IdentifiedSponsorsFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last update date')),
                ('is_valid', models.BooleanField(blank=True, default=False, null=True, verbose_name='É valido?')),
                ('line_count', models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantidade de linhas')),
                ('attachment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document')),
                ('creator', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='identifiedsponsorsfile_creator', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='identifiedsponsorsfile_last_mod_user', to=settings.AUTH_USER_MODEL, verbose_name='Updater')),
            ],
            options={
                'verbose_name_plural': 'Identified Sponsors Upload',
            },
        ),
        migrations.CreateModel(
            name='IdentifiedSponsors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last update date')),
                ('sponsor_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Sponsor Name')),
                ('std_id_jac', models.IntegerField(blank=True, null=True, verbose_name='ID (Jaccard)')),
                ('score_jac', models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True, verbose_name='Score (Jaccard)')),
                ('std_id_sem', models.IntegerField(blank=True, null=True, verbose_name='ID (Semantic)')),
                ('score_sem', models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True, verbose_name='Score (Semantic)')),
                ('creator', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='identifiedsponsors_creator', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='identifiedsponsors_last_mod_user', to=settings.AUTH_USER_MODEL, verbose_name='Updater')),
            ],
            options={
                'verbose_name_plural': 'Identified Sponsors',
            },
        ),
    ]