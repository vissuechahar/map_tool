# Generated by Django 3.0.7 on 2020-07-28 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0011_interfacedetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='interfacedetail',
            name='interface',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_1.Interface'),
        ),
    ]
