# Generated by Django 3.2.7 on 2021-11-05 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='category',
            field=models.CharField(choices=[('clothes', 'clothes'), ('shoes', 'shoes'), ('food', 'food')], default='selcect a category', max_length=40),
        ),
    ]
