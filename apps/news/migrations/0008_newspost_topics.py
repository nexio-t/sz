# Generated by Django 3.2.7 on 2021-09-03 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0003_auto_20210903_1445'),
        ('news', '0007_auto_20210902_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspost',
            name='topics',
            field=models.ManyToManyField(to='taxonomy.Topic'),
        ),
    ]
