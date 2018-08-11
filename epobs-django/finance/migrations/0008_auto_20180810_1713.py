# Generated by Django 2.0.7 on 2018-08-11 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0007_auto_20180809_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensetransaction',
            name='date_approved',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expensetransaction',
            name='date_issued',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expensetransaction',
            name='date_paid',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expensetransaction',
            name='discount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expensetransaction',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='finance.EmployeeAccount'),
        ),
        migrations.AlterField(
            model_name='expensetransaction',
            name='quantity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expensetransaction',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='finance.SupplierAccount'),
        ),
        migrations.AlterField(
            model_name='expensetransaction',
            name='unit_cost',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='revenuetransaction',
            name='date_issued',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='revenuetransaction',
            name='date_paid',
            field=models.DateField(blank=True, null=True),
        ),
    ]
