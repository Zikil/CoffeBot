# Generated by Django 4.0.1 on 2022-05-20 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cofbot', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buying',
            old_name='ID_barista',
            new_name='Barista',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='ID_check',
            new_name='Buying',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='ID_product',
            new_name='Product',
        ),
        migrations.RemoveField(
            model_name='buying',
            name='ID_check',
        ),
        migrations.AddField(
            model_name='buying',
            name='Check',
            field=models.IntegerField(auto_created=True, default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='Count',
            field=models.PositiveIntegerField(default=1),
        ),
    ]