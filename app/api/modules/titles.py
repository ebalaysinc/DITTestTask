from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.authtoken.models import Token
from ..models import Title


"""
Функция для получения всех тайтлов
"""
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def api_get_all_titles(request):
    return Response({'status': True, 'titles': [{'id': i.id, 'name': i.name, 'link': i.link} for i in Title.objects.all()]})


"""
Функция для получения одного тайтла
"""
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def api_get_title(request):

    # Проверяем наличие необходимых параметров и является ли id числом
    if all(data in request.data for data in ('id',)) and str(request.data['id']).isnumeric():

        # Проверяем, не существует ли объекта с этим ID
        if not Title.objects.filter(id=int(request.data['id'])).exists():
            # Если не существует - дропаем ошибку
            return Response({'status': False, 'error': 'TitleNotExistError'}, status=HTTP_400_BAD_REQUEST)

        title = Title.objects.get(id = int(request.data['id']))

        return Response({'status': True,
                         'title': {'id': title.id, 'name': title.name, 'link': title.link}})

    else:
        # Иначе - дропаем 400 с ошибкой
        return Response({'status': False, 'error': 'NoDataProvidedError'}, status=HTTP_400_BAD_REQUEST)


"""
Функция для удаления тайтла
"""
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def api_delete_title(request):
    # Проверяем наличие необходимых параметров, а также, является ли id числом
    if all(data in request.data for data in ('id',)) and str(request.data['id']).isnumeric():

        # Проверяем наличие объекта с таким id
        if Title.objects.filter(id=int(request.data['id'])).exists():
            # Всё ок - возвращаем status: true
            Title.objects.filter(id=int(request.data['id'])).delete()
            return Response({'status': True})
        
        else: # Иначе - ошибку
            return Response({'status': False, 'error': 'TitleNotExistError'}, status=HTTP_400_BAD_REQUEST)
    
    else:
        # Иначе - дропаем 400 с ошибкой
        return Response({'status': False, 'error': 'NoDataProvidedError'}, status=HTTP_400_BAD_REQUEST)


"""
Функция для создания тайтла
"""
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def api_create_title(request):
    # Проверяем наличие необходимых параметров
    if all(data in request.data for data in ('name', 'link')):
        # Всё ок - возвращаем status: true и id
        created_title = Title.objects.create(name=request.data['name'], link=request.data['link'])
        return Response({'status': True,
                         'title': {'id': created_title.id, 'name': created_title.name, 'link': created_title.link}})
    
    else:
        # Иначе - дропаем 400 с ошибкой
        return Response({'status': False, 'error': 'NoDataProvidedError'}, status=HTTP_400_BAD_REQUEST)


"""
Функция для изменения тайтла
"""
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def api_edit_title(request):
    # Проверяем наличие необходимых параметров
    if all(data in request.data for data in ('id',)) and str(request.data['id']).isnumeric():

        # Проверяем, существует ли объект с таким id
        if not Title.objects.filter(id=int(request.data['id'])).exists():
            # Если нет - возвращаем ошибку
            return Response({'status': False, 'error': 'TitleNotExistError'}, status=HTTP_400_BAD_REQUEST)
        
        title = Title.objects.get(id = int(request.data['id']))

        # Проверяем наличие различных параметров для изменения
        if 'name' in request.data: title.name = request.data['name']
        if 'link' in request.data: title.link = request.data['link']
        
        title.save()

        return Response({'status': True,
                         'title': {'id': title.id, 'name': title.name, 'link': title.link}})
    
    else:
        # Иначе - дропаем 400 с ошибкой
        return Response({'status': False, 'error': 'NoDataProvidedError'}, status=HTTP_400_BAD_REQUEST)