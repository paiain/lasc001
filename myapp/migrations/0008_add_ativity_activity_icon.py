# Generated by Django 4.0.6 on 2022-09-13 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_add_data_all_add_id_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_ativity',
            name='activity_icon',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
