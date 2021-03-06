# Generated by Django 4.0.5 on 2022-07-05 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tallapp', '0002_vouchertype_contra_ledger_payment_ledger_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='vouchertype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tallapp.vouchertype'),
        ),
        migrations.AddField(
            model_name='contra',
            name='vouchertype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tallapp.vouchertype'),
        ),
        migrations.AddField(
            model_name='payment',
            name='vouchertype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tallapp.vouchertype'),
        ),
        migrations.AddField(
            model_name='receipt',
            name='vouchertype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tallapp.vouchertype'),
        ),
        migrations.CreateModel(
            name='sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('amount', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tallapp.particulars')),
                ('date', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tallapp.account')),
                ('vouchertype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tallapp.vouchertype')),
            ],
        ),
        migrations.CreateModel(
            name='journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('amount', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tallapp.particulars')),
                ('date', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tallapp.account')),
                ('vouchertype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tallapp.vouchertype')),
            ],
        ),
    ]
