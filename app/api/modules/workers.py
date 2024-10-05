from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.authtoken.models import Token
from ..models import Title, Chapter, Worker


"""
Функция для создания работника в главе
"""
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def api_create_worker(request):

    # Проверяем наличие необходимых параметров и является ли id числом
    if all(data in request.data for data in ('id', 'nickname', 'contact', 'occupation')) and str(request.data['id']).isnumeric():

        # Проверяем, не существует ли объекта с этим ID
        if not Chapter.objects.filter(id=int(request.data['id'])).exists():
            # Если не существует - дропаем ошибку
            return Response({'status': False, 'error': 'ChapterNotExistError'}, status=HTTP_400_BAD_REQUEST)

        worker = Chapter.objects.get(id = int(request.data['id']))
        worker = worker.worker_set.create(nickname = request.data['nickname'],
                                 contact = request.data['contact'],
                                 occupation = request.data['occupation'])
        
        return Response({'status': True,
                         'worker': {'id': worker.id, 'nickname': worker.nickname, 'contact': worker.contact, 'occupation': worker.occupation}})

    else:
        # Иначе - дропаем 400 с ошибкой
        return Response({'status': False, 'error': 'NoDataProvidedError'}, status=HTTP_400_BAD_REQUEST)


"""
Функция для получения всех работников в главе
"""
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def api_get_all_workers(request):

    # Проверяем наличие необходимых параметров и является ли id числом
    if all(data in request.data for data in ('id',)) and str(request.data['id']).isnumeric():

        # Проверяем, не существует ли объекта с этим ID
        if not Chapter.objects.filter(id=int(request.data['id'])).exists():
            # Если не существует - дропаем ошибку
            return Response({'status': False, 'error': 'ChapterNotExistError'}, status=HTTP_400_BAD_REQUEST)

        chapter = Chapter.objects.get(id = int(request.data['id']))

        return Response({'status': True,
                         'workers': [{'id': worker.id, 'nickname': worker.nickname, 'contact': worker.contact, 'occupation': worker.occupation} for worker in chapter.worker_set.all()]})

    else:
        # Иначе - дропаем 400 с ошибкой
        return Response({'status': False, 'error': 'NoDataProvidedError'}, status=HTTP_400_BAD_REQUEST)


"""
Функция для изменения работника в главе
"""
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def api_edit_worker(request):

    # Проверяем наличие необходимых параметров и является ли id числом
    if all(data in request.data for data in ('id',)) and str(request.data['id']).isnumeric():

        # Проверяем, не существует ли объекта с этим ID
        if not Worker.objects.filter(id=int(request.data['id'])).exists():
            # Если не существует - дропаем ошибку
            return Response({'status': False, 'error': 'WorkerNotExistError'}, status=HTTP_400_BAD_REQUEST)

        worker = Worker.objects.get(id = int(request.data['id']))

        # Проверяем наличие параметров для изменения
        if 'nickname' in request.data: worker.nickname = request.data['nickname']
        if 'contact' in request.data: worker.contact = request.data['contact']
        if 'occupation' in request.data: worker.occupation = request.data['occupation']
        
        worker.save()

        return Response({'status': True,
                         'worker': {'id': worker.id, 'nickname': worker.nickname, 'contact': worker.contact, 'occupation': worker.occupation}})

    else:
        # Иначе - дропаем 400 с ошибкой
        return Response({'status': False, 'error': 'NoDataProvidedError'}, status=HTTP_400_BAD_REQUEST)


"""
Функция для удаления работника из главы
"""
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def api_delete_worker(request):

    # Проверяем наличие необходимых параметров и является ли id числом
    if all(data in request.data for data in ('id',)) and request.data['id'].isnumeric():

        # Проверяем, не существует ли объекта с этим ID
        if not Worker.objects.filter(id=int(request.data['id'])).exists():
            # Если не существует - дропаем ошибку
            return Response({'status': False, 'error': 'WorkerNotExistError'}, status=HTTP_400_BAD_REQUEST)

        Worker.objects.filter(id=int(request.data['id'])).delete()
        return Response({'status': True})

    else:
        # Иначе - дропаем 400 с ошибкой
        return Response({'status': False, 'error': 'NoDataProvidedError'}, status=HTTP_400_BAD_REQUEST)