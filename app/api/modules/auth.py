from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

"""
Функция авторизации
"""
@authentication_classes((BasicAuthentication, TokenAuthentication))
@api_view(['POST'])
@permission_classes((AllowAny,))
def api_auth(request):
    # Проверяем, есть ли в запросе логин и пароль
    if all(cred in request.data for cred in ('username', 'password')):
        user = authenticate(username=request.data['username'], password=request.data['password'])

        # Проверяем, успешна ли авторизация
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'status': True, 'token': token.key})

        # Иначе, дропаем ответ с 400
        else:
            return Response({'status': False, 'error': 'BadCredentialsError'}, status=HTTP_400_BAD_REQUEST)
    
    # Если нет, то дропаем ответ и ошибку 400
    else:
        return Response({'status': False, 'error': 'CredentialsMissedError'}, status=HTTP_400_BAD_REQUEST)