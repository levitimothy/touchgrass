# Generated by Django 5.0.2 on 2024-04-12 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touchgrass', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.CharField(default='n/a', max_length=500),
        ),
    ]
