# Generated by Django 4.0.3 on 2022-04-22 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='disenoPromedio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AddField(
            model_name='website',
            name='usabilidadPromedio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AddField(
            model_name='reviewmetadata',
            name='numReviewsOptionalParams',
            field=models.IntegerField(null=False, default=0),
        ),
        migrations.AddField(
            model_name='reviewmetadata',
            name='sumaDiseno',
            field=models.IntegerField(null=False, default=0),
        ),
        migrations.AddField(
            model_name='reviewmetadata',
            name='sumaUsabilidad',
            field=models.IntegerField(null=False, default=0),
        ),
    ]
