# Generated by Django 4.2.3 on 2023-07-12 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_auction_id_alter_bid_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='auctions/images'),
        ),
    ]
