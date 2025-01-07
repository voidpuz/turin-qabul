# Generated by Django 5.1.4 on 2025-01-07 20:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admission', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('canceled', 'Canceled')], default='pending', max_length=32, verbose_name='Status')),
                ('paid_at', models.DateTimeField(blank=True, null=True, verbose_name='Paid at')),
                ('canceled_at', models.DateTimeField(blank=True, null=True, verbose_name='Canceled at')),
                ('payment_type', models.CharField(choices=[('CLICK', 'CLICK'), ('PAYME', 'PAYME')], verbose_name='Payment Type')),
                ('commission', models.PositiveSmallIntegerField(db_default=0, default=0, verbose_name='Commission Percent')),
                ('fiscal_check_url', models.URLField(blank=True, null=True, verbose_name='Fiscal check url')),
                ('extra', models.JSONField(blank=True, null=True, verbose_name='Extra')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions', to='admission.admission')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
                'db_table': 'Transaction',
            },
        ),
    ]