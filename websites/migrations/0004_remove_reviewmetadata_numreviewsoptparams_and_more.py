# Generated by Django 4.0.3 on 2022-04-22 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0003_remove_website_calificaciondisenopromedio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='tipo',
            field=models.CharField(choices=[('NO CALIFICADO', 'No calificado'), ('SOCIAL', 'Social'), ('ENTRETENIMIENTO', 'Entretenimiento'), ('NOTICIAS', 'Noticias'), ('ACADEMICO', 'Academico'), ('OPINION', 'Opinion'), ('COMERCIO', 'Comercio'), ('TECNOLOGIA', 'Tecnologia'), ('PRODUCTIVIDAD', 'Productividad'), ('TURISMO', 'Turismo'), ('INVESTIGACION', 'Investigacion'), ('PERIODISMO', 'Periodismo'), ('TEST', 'Test')], default='NO CALIFICADO', max_length=50, primary_key=True, serialize=False),
        ),
    ]
