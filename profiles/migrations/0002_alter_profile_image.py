# Generated by Django 3.2.19 on 2023-05-24 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='https://res.cloudinary.com/dnqpruigq/image/upload/v1684932323/woodshed_media/profile-default_iqrrx0.png', upload_to='images/'),
        ),
    ]
