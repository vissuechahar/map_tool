# Generated by Django 3.0.8 on 2020-07-17 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InterfaceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interface', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=50)),
                ('publisherschema', models.CharField(choices=[('TS', 'Trade Stone'), ('O', 'Others')], max_length=4)),
                ('subscriber', models.CharField(max_length=50)),
                ('subscriberschema', models.CharField(choices=[('RMS', 'RMS'), ('DMS', 'DMS')], max_length=4)),
                ('updatedon', models.DateField(auto_now_add=True)),
                ('createdon', models.DateTimeField(auto_now_add=True)),
                ('approveon', models.DateField(auto_now=True, null=True)),
                ('assignon', models.DateField(auto_now=True)),
                ('approveby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='approveby', to=settings.AUTH_USER_MODEL)),
                ('assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assign_to', to=settings.AUTH_USER_MODEL)),
                ('createdby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('interface_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.InterfaceType')),
                ('updatedby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updateby', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
