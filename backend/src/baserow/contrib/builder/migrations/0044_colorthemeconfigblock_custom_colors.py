# Generated by Django 5.0.9 on 2025-01-02 10:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("builder", "0043_buttonthemeconfigblock_button_font_weight_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="colorthemeconfigblock",
            name="custom_colors",
            field=models.JSONField(db_default=[], default=list),
        ),
    ]
