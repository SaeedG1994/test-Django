# Generated by Django 4.0.5 on 2022-07-10 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dev_projects', '0010_alter_review_owner'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='review',
            name='owner',
        ),
    ]