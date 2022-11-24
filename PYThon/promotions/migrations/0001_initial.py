# Generated by Django 3.1.7 on 2021-04-26 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='promotions',
            fields=[
                ('ma_chuong_trinh', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('ten_chuong_trinh', models.CharField(default='', max_length=150)),
                ('noi_dung', models.TextField(default='')),
                ('phantram_giam', models.IntegerField(default=1)),
                ('ngay_bat_dau', models.DateField()),
                ('thoi_gian_ket_thuc', models.DateField()),
                ('ma_loai_san_pham', models.ForeignKey(db_column='loai_san_pham', on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
            options={
                'db_table': 'chuong_trinh_khuyen_mai',
            },
        ),
    ]
