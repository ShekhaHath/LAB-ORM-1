# Generated by Django 5.0.2 on 2024-03-17 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_post_delete_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]