# Generated by Django 5.0.2 on 2024-03-17 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_post_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='poster',
            field=models.ImageField(default='/images/blog-pic.avif', upload_to='images/'),
        ),
    ]
