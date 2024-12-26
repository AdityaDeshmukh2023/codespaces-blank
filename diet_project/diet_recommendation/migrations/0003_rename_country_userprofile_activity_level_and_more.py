# Generated by Django 5.1.4 on 2024-12-26 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("diet_recommendation", "0002_remove_userprofile_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="userprofile",
            old_name="country",
            new_name="Activity_level",
        ),
        migrations.RenameField(
            model_name="userprofile",
            old_name="language",
            new_name="Target_timeline",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="state",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="veg_or_nonveg",
        ),
    ]
