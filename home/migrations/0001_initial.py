# Generated by Django 3.2.4 on 2021-06-28 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TotalEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.TextField(blank=True, null=True)),
                ('loc_name', models.TextField(blank=True, null=True)),
                ('day1sd', models.IntegerField(blank=True, db_column='Day1SD', null=True)),
                ('day01fir', models.IntegerField(blank=True, db_column='Day01FIR', null=True)),
                ('day02sd', models.IntegerField(blank=True, db_column='Day02SD', null=True)),
                ('day02fir', models.IntegerField(blank=True, db_column='Day02FIR', null=True)),
                ('day03sd', models.IntegerField(blank=True, db_column='Day03SD', null=True)),
                ('day03fir', models.IntegerField(blank=True, db_column='Day03FIR', null=True)),
                ('day04sd', models.IntegerField(blank=True, db_column='Day04SD', null=True)),
                ('day04fir', models.IntegerField(blank=True, db_column='Day04FIR', null=True)),
                ('other_entry', models.IntegerField(blank=True, db_column='Other_entry', null=True)),
            ],
            options={
                'db_table': 'Total_Entry',
                'managed': False,
            },
        ),
    ]