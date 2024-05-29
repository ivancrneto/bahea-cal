from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['POST'])
def cors_test(request):
    return JsonResponse({'status':'OK'}, status=status.HTTP_200_OK)