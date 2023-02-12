# Generated by Django 4.1.5 on 2023-01-24 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_remove_omega_dbconn_vat_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='omegadbconn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CUSTOM_CODE', models.CharField(max_length=20)),
                ('CUSTOM_NAME', models.CharField(max_length=100)),
                ('VAT_RATE', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.DeleteModel(
            name='omega_dbconn',
        ),
    ]