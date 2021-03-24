# Generated by Django 3.1.7 on 2021-03-23 19:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pokemons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_pokemon', to='jwt_auth.user'),
            preserve_default=False,
        ),
    ]
