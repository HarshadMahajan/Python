# Generated by Django 2.2.1 on 2019-06-11 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ICC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=200)),
                ('matches', models.IntegerField()),
                ('matches_won', models.IntegerField()),
                ('net_r_r', models.CharField(max_length=200)),
                ('points', models.IntegerField()),
            ],
            options={
                'db_table': 'ICC',
            },
        ),
    ]
