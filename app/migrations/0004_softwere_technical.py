# Generated by Django 3.1.14 on 2021-12-08 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_education_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Softwere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Softwere')),
                ('level', models.CharField(max_length=100, verbose_name='Level')),
                ('percentage', models.IntegerField(verbose_name='Percentage')),
            ],
        ),
        migrations.CreateModel(
            name='Technical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Softwere')),
                ('level', models.CharField(max_length=100, verbose_name='Level')),
                ('percentage', models.IntegerField(verbose_name='Percentage')),
            ],
        ),
    ]
