# Generated by Django 3.2.9 on 2021-12-04 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GPSData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('X_Coords', models.DecimalField(decimal_places=6, max_digits=9)),
                ('Y_Coords', models.DecimalField(decimal_places=6, max_digits=9)),
                ('img', models.ImageField(upload_to='DB Pictures')),
            ],
        ),
    ]
