# Generated by Django 3.1.7 on 2021-07-03 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0029_auto_20210609_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AlterField(
            model_name='advertising',
            name='photo',
            field=models.ImageField(null=True, upload_to='photo/%Y/%m/%d/'),
        ),
    ]