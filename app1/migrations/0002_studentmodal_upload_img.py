# Generated by Django 3.0.8 on 2021-01-10 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodal',
            name='upload_img',
            field=models.ImageField(default=None, upload_to='student/'),
        ),
    ]