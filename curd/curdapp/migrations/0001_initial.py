# Generated by Django 3.1.1 on 2020-09-30 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usn', models.IntegerField()),
                ('Name', models.CharField(max_length=50)),
                ('marks', models.IntegerField()),
                ('cgpa', models.IntegerField()),
            ],
        ),
    ]
