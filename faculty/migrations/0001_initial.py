
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(

            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=50)),
                ('student_email', models.EmailField(max_length=254)),
                ('student_password', models.CharField(max_length=50)),
                ('hostel', models.CharField(max_length=3)),
                ('image', models.ImageField(default='', upload_to='student/images')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
