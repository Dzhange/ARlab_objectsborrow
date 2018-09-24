# Generated by Django 2.0.7 on 2018-09-23 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0013_auto_20180922_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='spec',
            field=models.CharField(choices=[('SC', 'Boot C in 302'), ('SA', 'Boot A in 302'), ('FR', '301'), ('SB', 'Boot B in 302'), ('ST', 'All Boots(ABCD) in 302'), ('SD', 'Boot D in 302')], max_length=2),
        ),
        migrations.AlterField(
            model_name='stuff',
            name='spec',
            field=models.CharField(choices=[('DT', 'Ddesktop'), ('PT', 'Printer'), ('MC', 'iMac'), ('EP', 'EarPhone'), ('SP', 'Speaker')], max_length=20),
        ),
        migrations.AlterField(
            model_name='stuff',
            name='status',
            field=models.CharField(choices=[('PF', 'Perfect'), ('TB', 'Toltally Broken'), ('SB', 'Slightly Broken')], max_length=2),
        ),
    ]
