# Create your views here.
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes

@api_view(['GET'])
def hola-mundo(request):
    template = '<h1>Hola Mundo Inove, esto es Django APIs!</h1>' 
    return HttpResponse(template)

@api_view(['GET', 'POST'])
@permission_classes([]) # Eliminamos la necesidad de autenticar al usuario.
def return_request_data(request):
    template = f'<h1>{request.GET.get("mi_parametro")}</h1>'
    print(template)
    return HttpResponse(template)