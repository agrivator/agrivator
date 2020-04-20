# Generated by Django 3.0.4 on 2020-04-20 06:42

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('phone_one', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(code='invalid_mobile', message='Please Enter 10/11 digit mobile number or landline as 0<std code><phone number>', regex='^((\\+91|91|0)[\\- ]{0,1})?[456789]\\d{9}$')])),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_type', models.CharField(choices=[('Farmer', 'Farmer'), ('Shop', 'Shop'), ('Customer', 'Customer')], max_length=50)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_address', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='FarmerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farm_address', models.TextField(max_length=500)),
                ('farm_phone', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(code='invalid_mobile', message='Please Enter 10/11 digit mobile number or landline as 0<std code><phone number>', regex='^((\\+91|91|0)[\\- ]{0,1})?[456789]\\d{9}$')])),
            ],
        ),
        migrations.CreateModel(
            name='ShopProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=255)),
                ('shop_address', models.TextField(max_length=500)),
                ('shop_phone', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(code='invalid_mobile', message='Please Enter 10/11 digit mobile number or landline as 0<std code><phone number>', regex='^((\\+91|91|0)[\\- ]{0,1})?[456789]\\d{9}$')])),
                ('shop_owner_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cost', models.FloatField()),
                ('quantity', models.FloatField()),
                ('organic', models.BooleanField()),
                ('farmer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
