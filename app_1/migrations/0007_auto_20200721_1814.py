# Generated by Django 3.0.7 on 2020-07-21 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0006_auto_20200721_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interface',
            name='updatedon',
            field=models.DateField(blank=True, null=True),
        ),
    ]
