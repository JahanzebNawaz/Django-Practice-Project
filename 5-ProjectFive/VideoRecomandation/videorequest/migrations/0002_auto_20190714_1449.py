# Generated by Django 2.2.3 on 2019-07-14 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videorequest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='videotitle',
            field=models.CharField(max_length=50),
        ),
    ]
