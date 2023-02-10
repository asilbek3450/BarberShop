# Generated by Django 4.1.6 on 2023-02-09 20:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
                ('phone_number', models.CharField(default=None, max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '998 [XX] [XXX XX XX]'. Up to 12 digits allowed.", regex='^998[0-9]{9}$')])),
                ('email', models.EmailField(blank=True, default=None, max_length=100, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
