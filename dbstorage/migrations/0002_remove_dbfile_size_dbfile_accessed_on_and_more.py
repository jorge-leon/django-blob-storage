# Generated by Django 4.2.1 on 2023-05-22 09:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("dbstorage", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="dbfile",
            name="size",
        ),
        migrations.AddField(
            model_name="dbfile",
            name="accessed_on",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="dbfile",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
        ),
    ]
