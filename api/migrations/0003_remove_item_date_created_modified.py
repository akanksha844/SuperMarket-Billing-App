from django.db import migrations

class Migration(migrations.Migration):
    
    dependencies= [
        ('item', '0002_rename_items_item'),
    ]
    
    operations = [
        migrations.RemoveField(
            model_name = 'item',
            name = 'date_created',
        ),
        migrations.RemoveField(
            model_name = 'item',
            name = 'date_modified',
        ),
    ]
    