from django.db import migrations, models

class Migration(migrations.Migration):
    
    initial = True
    
    dependencies= [
        
    ]
    
    operations = [
        migrations.CreateModel(
            name = 'Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize= False, verbose_name = 'ID' )),
                ('name', models.CharField(blank= True, max_length=255, null = True)),
                ('category', models.CharField(blank= True, max_length=255, null = True)),
                ('subcategory', models.CharField(blank = True, max_length= 255, null = True)),
                ('amount', models.IntegerField()),
                ('price', models.FloatField()),
                ('date_created', models.DateTimeField(auto_now_add= True)),
                ('date_modified', models.DateTimeField(auto_now = True)),
                
                    
            ],
        ),
    ]
    