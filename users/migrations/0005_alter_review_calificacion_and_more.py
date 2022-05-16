# Generated by Django 4.0.3 on 2022-05-16 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_review_calificacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='calificacion',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='review',
            name='calificacionDiseno',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='calificacionUsabilidad',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='gradoVeracidad',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
    ]