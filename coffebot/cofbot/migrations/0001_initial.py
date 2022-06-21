# Generated by Django 4.0.1 on 2022-05-18 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barista',
            fields=[
                ('ID_barista', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('Full_name', models.CharField(max_length=200)),
                ('Birthday', models.DateField()),
                ('Phone_number', models.PositiveBigIntegerField()),
                ('Addres', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Buying',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_check', models.PositiveIntegerField()),
                ('Cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_ingred', models.PositiveIntegerField()),
                ('Name', models.CharField(max_length=200)),
                ('Count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Price', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_id', models.PositiveIntegerField(unique=True)),
                ('name', models.CharField(max_length=200)),
                ('code', models.PositiveIntegerField(unique=True)),
                ('admin', models.BooleanField(default=False)),
                ('score', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Count_ingred', models.IntegerField()),
                ('ID_ingred', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cofbot.ingredients')),
                ('ID_product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cofbot.product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Count', models.PositiveIntegerField()),
                ('ID_check', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cofbot.buying')),
                ('ID_product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cofbot.product')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cofbot.profile')),
            ],
        ),
        migrations.AddField(
            model_name='buying',
            name='Customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cofbot.profile'),
        ),
        migrations.AddField(
            model_name='buying',
            name='ID_barista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cofbot.barista'),
        ),
    ]