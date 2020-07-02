# Generated by Django 3.0.4 on 2020-06-26 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BennaFood', '0006_auto_20200626_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentaire',
            name='recette',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentaires', to='BennaFood.Recette'),
        ),
        migrations.AlterField(
            model_name='recette',
            name='categorie',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='categorie', to='BennaFood.Categorie'),
        ),
    ]
