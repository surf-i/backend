# Generated by Django 4.0.4 on 2022-04-28 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0008_alter_datoscategoria_id_alter_datoscategoria_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='autor',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='website',
            name='fecha',
            field=models.DateField(null=True),
        ),
    ]
