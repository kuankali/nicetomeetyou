# Generated by Django 2.1.2 on 2018-10-06 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NbaNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('context', models.CharField(blank=True, default='', max_length=1000)),
                ('photo', models.URLField(blank=True, default='')),
                ('video', models.URLField(blank=True, default='')),
            ],
        ),
    ]
