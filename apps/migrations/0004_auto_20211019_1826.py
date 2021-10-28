# Generated by Django 3.2.7 on 2021-10-19 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_alter_contact_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='category',
            field=models.CharField(choices=[('food', 'food'), ('clothes', 'clothes'), ('shoes', 'shoes')], default='selcect a category', max_length=40),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(max_length=11),
        ),
    ]
