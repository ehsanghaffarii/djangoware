# Generated by Django 2.1.2 on 2018-10-18 20:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sitewide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('unique_id', models.TextField()),
            ],
            options={
                'verbose_name': 'Sitewide',
                'permissions': (('admin_sitewide', 'access to the admin menu'), ('staff_sitewide', 'access to limited admin menu')),
            },
        ),
    ]