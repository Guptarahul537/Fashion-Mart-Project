# Generated by Django 4.1.1 on 2023-04-16 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("fashionmartApp", "0008_rename_whislist_wishlist"),
    ]

    operations = [
        migrations.CreateModel(
            name="Checkout",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("total", models.IntegerField()),
                ("shipping", models.IntegerField()),
                ("final", models.IntegerField()),
                (
                    "rppid",
                    models.CharField(blank=True, default="", max_length=30, null=True),
                ),
                ("date", models.DateField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fashionmartApp.buyer",
                    ),
                ),
            ],
        ),
    ]
