# Generated by Django 5.0.2 on 2024-02-16 07:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("review", "0003_comment_updated_at_alter_post_created_at_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="created",
            new_name="created_at",
        ),
    ]