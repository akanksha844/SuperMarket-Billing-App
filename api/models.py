from django.db import models

class Item(models.Model):
    
    category = models.CharField(max_length = 255, blank =True, null = True)
    subcategory = models.CharField(max_length = 255, blank= True, null = True)
    name= models.CharField(max_length = 255, blank= True, null = True)
    amount = models.PositiveIntegerField()
    price = models.FloatField()
    
    
    def  __str__(self) -> str:
        return self.name