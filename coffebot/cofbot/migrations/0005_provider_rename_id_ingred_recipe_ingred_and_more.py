# Generated by Django 4.0.1 on 2022-05-28 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cofbot', '0004_alter_buying_barista_alter_buying_check_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Nomber', models.CharField(max_length=15)),
            ],
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='ID_ingred',
            new_name='Ingred',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='ID_product',
            new_name='Product',
        ),
        migrations.RemoveField(
            model_name='ingredients',
            name='ID_ingred',
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateRequest', models.DateField()),
                ('DateSupply', models.DateField()),
                ('Price', models.PositiveIntegerField()),
                ('Delivered', models.BooleanField()),
                ('Provider', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cofbot.provider')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cost', models.DecimalField(decimal_places=2, max_digits=7)),
                ('Count', models.PositiveIntegerField()),
                ('Ingred', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cofbot.ingredients')),
                ('Supply', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cofbot.supply')),
            ],
        ),
    ]
