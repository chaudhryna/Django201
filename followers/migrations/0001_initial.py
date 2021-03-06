# Generated by Django 4.0 on 2021-12-12 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed_by', to='auth.user')),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='auth.user')),
            ],
            options={
                'unique_together': {('followed_by', 'following')},
            },
        ),
    ]
