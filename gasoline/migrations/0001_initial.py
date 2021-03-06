# Generated by Django 3.1.2 on 2020-10-30 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('about', models.CharField(blank=True, help_text='Short description of the station', max_length=200, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to=None)),
                ('register', models.CharField(blank=True, help_text='Unique Register given for the Mexican Govenment', max_length=64, null=True, unique=True)),
                ('latitude', models.FloatField(max_length=9)),
                ('longitude', models.FloatField(max_length=9)),
                ('town', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, help_text='Official name of the Mexican state where is located the station', max_length=50, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('status', models.CharField(default='ghost', help_text="Station' status based on their activity. It changes when a user verify the station ", max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gas_type', models.CharField(choices=[('premium', 'premium'), ('regular', 'regular'), ('diesel', 'diesel')], help_text='Type of gasoline between the GAS_CHOICES', max_length=20)),
                ('price', models.FloatField(max_length=5)),
                ('date', models.DateTimeField(auto_now_add=True, help_text='Date Time on wich the prices are registred', verbose_name='created at')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gasoline.station')),
            ],
        ),
    ]
