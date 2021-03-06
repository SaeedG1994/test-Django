# Generated by Django 4.0.5 on 2022-07-01 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dev_users', '0003_profile_location_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد '),
        ),
        migrations.AlterField(
            model_name='skill',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات '),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='نام '),
        ),
        migrations.AlterField(
            model_name='skill',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dev_users.profile', verbose_name='یوز مربوط '),
        ),
    ]
