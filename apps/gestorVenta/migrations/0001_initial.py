# Generated by Django 4.0 on 2022-07-21 05:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestorZapatilla', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sale', models.DateField()),
                ('price_sale', models.FloatField(validators=[django.core.validators.MinValueValidator(50.0), django.core.validators.MaxValueValidator(500.0)])),
                ('type_pay', models.CharField(choices=[('F', 'Físico'), ('I', 'IziPay'), ('Y', 'Yape')], max_length=1)),
                ('gain', models.FloatField(default=0.0)),
                ('amount_shoes', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(50)])),
                ('entire_price', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(50.0)])),
                ('concrete_zapatilla', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestorZapatilla.detalle_zapatilla')),
            ],
        ),
    ]