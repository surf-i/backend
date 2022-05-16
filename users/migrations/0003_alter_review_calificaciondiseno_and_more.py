# Generated by Django 4.0.3 on 2022-05-16 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_review_calificacionusabilidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='calificacionDiseno',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='calificacionUsabilidad',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='gradoVeracidad',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=5),
        ),
    ]
