# Generated by Django 4.1.6 on 2024-03-04 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_admin_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='Employee_ID',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='admin',
            name='End_Date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
