# Generated by Django 2.2 on 2019-06-09 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_merge_20190609_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]