# Generated by Django 2.2.13 on 2020-06-29 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0020_auto_20200626_0612'),
    ]

    operations = [
        migrations.AddField(
            model_name='gatepass',
            name='p_contact',
            field=models.CharField(default='9999999999', max_length=9999999999),
        ),
        migrations.AddField(
            model_name='gatepass',
            name='room',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
