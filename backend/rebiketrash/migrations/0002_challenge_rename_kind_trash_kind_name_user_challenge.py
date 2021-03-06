# Generated by Django 4.0.6 on 2022-07-22 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rebikeuser', '0001_initial'),
        ('rebiketrash', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='challenge',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'challenge',
            },
        ),
        migrations.RenameField(
            model_name='trash_kind',
            old_name='kind',
            new_name='name',
        ),
        migrations.CreateModel(
            name='user_challenge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('challenge_number', models.ForeignKey(db_column='challenge_number', on_delete=django.db.models.deletion.CASCADE, to='rebiketrash.challenge')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='rebikeuser.user')),
            ],
            options={
                'db_table': 'user_challenge',
            },
        ),
    ]
