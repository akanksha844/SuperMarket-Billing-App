from import_export import resources

from .models import Item


class ItemResource(resources.ModelResource):
    class Meta:
        model = Item