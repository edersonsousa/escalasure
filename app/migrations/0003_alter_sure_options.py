# Generated by Django 3.2.16 on 2022-12-04 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_sure_pub_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sure',
            options={'get_latest_by': ['-priority', 'order_date']},
        ),
    ]