# Generated by Django 2.2.12 on 2022-11-13 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('app_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('date_time', models.DateTimeField(null=True)),
                ('status', models.CharField(max_length=10, null=True)),
                ('mode', models.CharField(max_length=10)),
                ('Doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Patient')),
            ],
        ),
    ]