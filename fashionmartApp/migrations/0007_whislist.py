# Generated by Django 4.1.1 on 2023-04-14 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("fashionmartApp", "0006_alter_buyer_addressline3_delete_wishlist"),
    ]

    operations = [
        migrations.CreateModel(
            name="Whislist",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fashionmartApp.product",
                    ),
                ),
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
