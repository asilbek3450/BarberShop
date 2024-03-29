# Generated by Django 4.1.6 on 2023-02-09 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BarberImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='barbers_images/')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Barber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='barber_image', to='barbers.barberimage')),
                ('shop_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='working_shop', to='shops.shop')),
            ],
        ),
    ]
