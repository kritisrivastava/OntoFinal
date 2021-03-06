# Generated by Django 2.0.12 on 2020-04-09 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ontointerface', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInputFormModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(max_length=500)),
                ('inquirer', models.CharField(choices=[('Admin', 'ADMIN'), ('JUNIOR NURSE', 'JUNIOR NURSE'), ('Surgeon', 'SURGEON')], default='ADMIN', max_length=100)),
                ('data_requested', models.CharField(choices=[('Neuraldata', 'NEURODATA'), ('Pediatricdata', 'PEDIATRIC DATA'), ('Gynaecdata', 'Gynac Data')], default='Neuraldata', max_length=100)),
            ],
        ),
    ]
