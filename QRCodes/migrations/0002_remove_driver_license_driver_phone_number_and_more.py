# Generated by Django 5.1.1 on 2024-09-30 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QRCodes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='license',
        ),
        migrations.AddField(
            model_name='driver',
            name='phone_number',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
