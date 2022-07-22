# Generated by Django 4.0.6 on 2022-07-22 11:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('alias', models.CharField(max_length=20, unique=True)),
                ('pw', models.BinaryField(max_length=60)),
                ('salt', models.BinaryField(max_length=29)),
                ('email', models.CharField(max_length=50)),
                ('active', models.IntegerField(default=1)),
                ('save_img', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
