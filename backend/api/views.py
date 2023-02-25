from django.forms.models import model_to_dict
from products.models import Product

from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer
# Create your views here.

@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by('?').first()
    data = {}
    if instance:
        # data = model_to_dict(instance)
        data = ProductSerializer(instance).data
    return Response(data)
