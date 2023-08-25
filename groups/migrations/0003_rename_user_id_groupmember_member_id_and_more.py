# Generated by Django 4.2.2 on 2023-08-22 23:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("groups", "0002_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="groupmember",
            old_name="user_id",
            new_name="member_id",
        ),
        migrations.AddField(
            model_name="groupmember",
            name="admin",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="group",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="group",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
