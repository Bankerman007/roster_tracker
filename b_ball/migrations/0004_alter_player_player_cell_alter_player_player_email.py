# Generated by Django 4.0 on 2022-01-02 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b_ball', '0003_alter_player_player_cell_alter_player_player_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='player_cell',
            field=models.CharField(default=123, max_length=30),
        ),
        migrations.AlterField(
            model_name='player',
            name='player_email',
            field=models.CharField(default=123, max_length=30),
        ),
    ]
