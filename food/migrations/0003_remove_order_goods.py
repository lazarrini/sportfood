# Generated by Django 4.2.5 on 2023-09-06 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_alter_goodinorder_good_alter_goodinorder_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='goods',
        ),
    ]
