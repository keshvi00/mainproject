# Generated by Django 5.0.3 on 2024-03-07 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('entryApp', '0002_customuser2_delete_customuserr'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomUser2',
            new_name='CustomUserr',
        ),
    ]
