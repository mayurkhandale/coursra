# Generated by Django 3.0.8 on 2021-01-10 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20210110_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailsModal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('eAdress', models.EmailField(max_length=254, unique=True)),
                ('Subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='studentmodal',
            name='upload_img',
        ),
    ]
