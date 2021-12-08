# Generated by Django 3.1.14 on 2021-12-07 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title')),
                ('subtitle', models.CharField(blank=True, max_length=100, null=True, verbose_name='Subtitle')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('job', models.TextField(verbose_name='Job')),
                ('introduction', models.TextField(verbose_name='Introduction')),
                ('github', models.CharField(blank=True, max_length=100, null=True, verbose_name='github')),
                ('twitter', models.CharField(blank=True, max_length=100, null=True, verbose_name='twitter')),
                ('linkedin', models.CharField(blank=True, max_length=100, null=True, verbose_name='linkedin')),
                ('facebook', models.CharField(blank=True, max_length=100, null=True, verbose_name='facebook')),
                ('instagram', models.CharField(blank=True, max_length=100, null=True, verbose_name='instagram')),
                ('topimage', models.ImageField(upload_to='images', verbose_name='TopImages')),
                ('subimage', models.ImageField(upload_to='images', verbose_name='SubImages')),
            ],
        ),
    ]