# Generated by Django 3.1.1 on 2020-09-28 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0003_auto_20200928_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='size',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
