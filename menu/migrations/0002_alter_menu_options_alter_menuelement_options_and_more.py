# Generated by Django 4.2.14 on 2024-07-24 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': 'меню', 'verbose_name_plural': 'меню'},
        ),
        migrations.AlterModelOptions(
            name='menuelement',
            options={'verbose_name': 'элемент меню', 'verbose_name_plural': 'элементы меню'},
        ),
        migrations.AddField(
            model_name='menu',
            name='main_menu_element',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='menu', to='menu.menuelement', verbose_name='основной элемент меню'),
        ),
        migrations.AlterField(
            model_name='menuelement',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='menu.menuelement', verbose_name='родитель'),
        ),
    ]
