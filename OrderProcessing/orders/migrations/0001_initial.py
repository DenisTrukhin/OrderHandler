# Generated by Django 2.2.3 on 2019-07-14 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=512, verbose_name='Description')),
                ('price', models.IntegerField(db_index=True, verbose_name='Price')),
            ],
        ),
    ]