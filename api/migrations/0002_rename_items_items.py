from django.db import migrations

class Migration(migrations.Migration):
    
    dependencies= [
        ('item', '0001_initial'),
    ]
    
    operations = [
        migrations.RenameModel(
            old_name = 'Items',
            new_name = 'Item',
        ),
    ]