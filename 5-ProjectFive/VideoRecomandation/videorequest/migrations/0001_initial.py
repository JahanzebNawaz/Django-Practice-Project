# Generated by Django 2.2.3 on 2019-07-14 14:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videotitle', models.CharField(max_length=20)),
                ('videodesc', models.TextField()),
                ('data_added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
