# Generated by Django 3.1.7 on 2021-03-16 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0002_service_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('status', models.BooleanField()),
                ('types', models.CharField(max_length=1)),
                ('idservice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contain', to='Services.services')),
            ],
        ),
        migrations.DeleteModel(
            name='Service_detail',
        ),
    ]
