# Generated by Django 4.0.6 on 2022-09-09 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_delete_addactivity'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_ativity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=10)),
                ('activity_Date', models.CharField(max_length=50)),
                ('activity_data', models.CharField(max_length=255)),
            ],
        ),
    ]