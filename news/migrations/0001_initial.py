# Generated by Django 4.1.3 on 2024-01-16 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breaking_news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Breaking_news',
            },
        ),
    ]
