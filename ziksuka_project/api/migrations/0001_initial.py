# Generated by Django 3.1.4 on 2021-02-03 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(default='alan', max_length=100)),
                ('title', models.CharField(default='title', max_length=100)),
                ('content', models.CharField(default='content', max_length=1000)),
            ],
        ),
    ]