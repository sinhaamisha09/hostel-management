# Generated by Django 2.2.11 on 2020-06-21 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='date_time',
        ),
        migrations.RemoveField(
            model_name='register',
            name='hostel',
        ),
        migrations.AddField(
            model_name='register',
            name='address',
            field=models.CharField(max_length=3000, null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='course',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='date_in',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='enrollment_no',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='register',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=None, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='hostel_name',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='p_contact',
            field=models.CharField(max_length=9999999999, null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='room_no',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='s_contact',
            field=models.CharField(max_length=9999999999, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='student_email',
            field=models.EmailField(default='pk@pk.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='register',
            name='student_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='student_password',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
