# Generated by Django 4.0.1 on 2022-04-07 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0009_alter_t_list_t_amt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=110)),
                ('message', models.TextField()),
            ],
        ),
    ]
