# Generated by Django 4.0.5 on 2022-07-10 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dev_users', '0004_profile_username_alter_skill_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='نام کاربری '),
        ),
    ]
