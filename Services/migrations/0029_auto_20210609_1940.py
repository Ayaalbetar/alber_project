# Generated by Django 3.1.7 on 2021-06-09 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0028_auto_20210609_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertising',
            name='photo',
            field=models.ImageField(null=True, upload_to=' photos/%Y/%m/%d/ '),
        ),
    ]
