# Generated by Django 4.1.1 on 2023-04-12 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fashionmartApp", "0002_rename_pic4_buyer_pic_alter_buyer_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="buyer",
            name="addressline3",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
