# Generated by Django 3.2.8 on 2021-10-31 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_pontoturistico_enderecos'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='pontosturisticos'),
        ),
    ]
