# Generated by Django 4.1.6 on 2023-02-16 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.CharField(max_length=240)),
                ('año', models.CharField(max_length=240)),
                ('inicio', models.DateField()),
                ('fin', models.DateField()),
            ],
        ),
    ]
