# Generated by Django 4.1.2 on 2022-10-15 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("personalApp", "0002_alter_personal_is_staffed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personal",
            name="is_staffed",
            field=models.BooleanField(default=False),
        ),
    ]
