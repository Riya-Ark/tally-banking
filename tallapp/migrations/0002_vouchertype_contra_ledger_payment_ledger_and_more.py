# Generated by Django 4.0.5 on 2022-07-05 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tallapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vouchertype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vouchertype', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='contra',
            name='ledger',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tallapp.ledger'),
        ),
        migrations.AddField(
            model_name='payment',
            name='ledger',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tallapp.ledger'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tallapp.ledger'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='amount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tallapp.particulars'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='date',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tallapp.account'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='ledger',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tallapp.ledger'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='transactiontype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tallapp.transactiontype'),
        ),
        migrations.AlterField(
            model_name='contra',
            name='amount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tallapp.particulars'),
        ),
        migrations.AlterField(
            model_name='contra',
            name='date',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tallapp.account'),
        ),
        migrations.AlterField(
            model_name='ledger',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tallapp.groups'),
        ),
        migrations.AlterField(
            model_name='particulars',
            name='particualrs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tallapp.ledger'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tallapp.particulars'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tallapp.account'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='amount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tallapp.particulars'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='date',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tallapp.account'),
        ),
    ]
