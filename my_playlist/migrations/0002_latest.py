# Generated by Django 3.0.4 on 2020-03-22 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_playlist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Latest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
