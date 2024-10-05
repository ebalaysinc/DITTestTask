from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.authtoken.models import Token
from ..models import Title, Chapter


"""
Функция для создания главы тайтла
"""
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def api_create_chapter(request):

    # Проверяем наличие необходимых параметров и является ли id числом
    if all(data in request.data for data in ('id', 'name', 'status', 'original')) and str(request.data['id']).isnumeric():

        # Проверяем, не существует ли объекта с этим ID
        if not Title.objects.filter(id=int(request.data['id'])).exists():
            # Если не существует - дропаем ошибку
            return Response({'status': False, 'error': 'TitleNotExistError'}, status=HTTP_400_BAD_REQUEST)

        title = Title.objects.get(id = int(request.data['id']))
        chapter = title.chapter_set.create(name = request.data['name'],
                                 status = False if request.data['status'] == '0' else True,
                                 original = request.data['original'])
        
        return Response({'status': True,
                         'chapter': {'id': chapter.id, 'name': chapter.name, 'status': chapter.status, 'original': chapter.original}})

    else:
        # Иначе - дропаем 400 с ошибкой
        return Response({'status': False, 'error': 'NoDataProvidedError'}, status=HTTP_400_BAD_REQUEST)


"""
Функция для получения всех глав тайтла
"""
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def api_get_all_chapters(request):

    # Проверяем наличие необходимых параметров и является ли id числом
    if all(data in request.data for data in ('id',)) and str(request.data['id']).isnumeric():

        # Проверяем, не существует ли объекта с этим ID
        if not Title.objects.filter(id=int(request.data['id'])).exists():
            # Если не существует - дропаем ошибку
            return Response({'status': False, 'error': 'TitleNotExistError'}, status=HTTP_400_BAD_REQUEST)

        title = Title.objects.get(id = int(request.data['id']))

        return Response({'status': True,
                         'chapters': [{'id': chapter.id, 'name': chapter.name, 'status': chapter.status, 'original': chapter.original} for chapter in title.chapter_set.all()]})

    else:
        # Иначе - дропаем 400 с ошибкой
        return Response({'status': False, 'error': 'NoDataProvidedError'}, status=HTTP_400_BAD_REQUEST)


"""
Функция для получения одной главы
"""
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def api_get_chapter(request):

    # Проверяем наличие необходимых параметров и является ли id числом
    if all(data in request.data for data in ('id',)) and str(request.data['id']).isnumeric():

        # Проверяем, не существует ли объекта с этим ID
        if not Chapter.objects.filter(id=int(request.data['id'])).exists():
            # Если не существует - дропаем ошибку
            return Response({'status': False, 'error': 'ChapterNotExistError'}, status=HTTP_400_BAD_REQUEST)

        chapter = Chapter.objects.get(id = int(request.data['id']))

        return Response({'status': True,
                         'chapter': {'id': chapter.id, 'name': chapter.name, 'status': chapter.status, 'original': chapter.original}})

    else:
        # Иначе - дропаем 400 с ошибкой
        return Response({'status': False, 'error': 'NoDataProvidedError'}, status=HTTP_400_BAD_REQUEST)


"""
Функция для изменения главы тайтла
"""
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def api_edit_chapter(request):

    # Проверяем наличие необходимых параметров и является ли id числом
    if all(data in request.data for data in ('id',)) and str(request.data['id']).isnumeric():

        # Проверяем, не существует ли объекта с этим ID
        if not Chapter.objects.filter(id=int(request.data['id'])).exists():
            # Если не существует - дропаем ошибку
            return Response({'status': False, 'error': 'ChapterNotExistError'}, status=HTTP_400_BAD_REQUEST)

        chapter = Chapter.objects.get(id = int(request.data['id']))

        # Проверяем наличие параметров для изменения
        if 'name' in request.data: chapter.name = request.data['name']
        if 'status' in request.data: chapter.status = False if request.data['status'] == '0' else True
        if 'original' in request.data: chapter.original = request.data['original']
        
        chapter.save()

        return Response({'status': True,
                         'chapter': {'id': chapter.id, 'name': chapter.name, 'status': chapter.status, 'original': chapter.original}})

    else:
        # Иначе - дропаем 400 с ошибкой
        return Response({'status': False, 'error': 'NoDataProvidedError'}, status=HTTP_400_BAD_REQUEST)


"""
Функция для удаления главы тайтла
"""
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def api_delete_chapter(request):

    # Проверяем наличие необходимых параметров и является ли id числом
    if all(data in request.data for data in ('id',)) and str(request.data['id']).isnumeric():

        # Проверяем, не существует ли объекта с этим ID
        if not Chapter.objects.filter(id=int(request.data['id'])).exists():
            # Если не существует - дропаем ошибку
            return Response({'status': False, 'error': 'ChapterNotExistError'}, status=HTTP_400_BAD_REQUEST)

        Chapter.objects.filter(id=int(request.data['id'])).delete()
        return Response({'status': True})

    else:
        # Иначе - дропаем 400 с ошибкой
        return Response({'status': False, 'error': 'NoDataProvidedError'}, status=HTTP_400_BAD_REQUEST)