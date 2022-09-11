# Generated by Django 3.2.15 on 2022-09-10 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=300)),
                ('author_name', models.CharField(max_length=150)),
                ('publishedon', models.DateField(auto_now_add=True)),
                ('isbn', models.CharField(max_length=13)),
                ('pages', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Books',
                'ordering': ['-publishedon'],
            },
        ),
    ]