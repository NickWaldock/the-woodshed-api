# Generated by Django 3.2.19 on 2023-05-24 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../woodshed_media/profile-default_iqrrx0.png', upload_to='images/'),
        ),
    ]