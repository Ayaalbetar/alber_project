# Generated by Django 3.1.7 on 2021-06-05 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0026_auto_20210605_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='amount_money',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]