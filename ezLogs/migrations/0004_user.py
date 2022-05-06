# Generated by Django 3.2.3 on 2022-03-07 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ezLogs", "0003_alter_logdetail_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("username", models.CharField(max_length=200, unique=True)),
                ("pswd_hash", models.CharField(max_length=500, unique=True)),
                ("emailid", models.EmailField(max_length=200, unique=True)),
                ("verified", models.BooleanField(default=False)),
            ],
        ),
    ]
