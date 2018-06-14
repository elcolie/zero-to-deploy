# Generated by Django 2.0.6 on 2018-06-13 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('menu_type', models.CharField(choices=[('Food', 'food'), ('Drink', 'drink')], default='Food', max_length=15)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('take_home', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]