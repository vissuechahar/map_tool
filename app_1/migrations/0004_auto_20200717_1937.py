# Generated by Django 3.0.8 on 2020-07-17 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0003_auto_20200717_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interface',
            name='createdon',
            field=models.DateTimeField(),
        ),
    ]