# Generated by Django 4.2.5 on 2023-10-26 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_first_app', '0002_alter_easylevel_submission_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='easylevel',
            name='level_params_digits',
            field=models.CharField(default='easy-1-1', max_length=50),
        ),
        migrations.AddField(
            model_name='hardlevel',
            name='level_params_digits',
            field=models.CharField(default='easy-1-1', max_length=50),
        ),
        migrations.AddField(
            model_name='mediumlevel',
            name='level_params_digits',
            field=models.CharField(default='easy-1-1', max_length=50),
        ),
    ]