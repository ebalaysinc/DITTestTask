from django.urls import path
from .modules import auth, titles, chapters, workers

urlpatterns = [
    path('auth/', auth.api_auth),

    path('getAllTitles/', titles.api_get_all_titles),
    path('getTitle/', titles.api_get_title),
    path('title/createTitle/', titles.api_create_title),
    path('title/deleteTitle/', titles.api_delete_title),
    path('title/editTitle/', titles.api_edit_title),

    path('getAllChapters/', chapters.api_get_all_chapters),
    path('getChapter/', chapters.api_get_chapter),
    path('chapter/createChapter/', chapters.api_create_chapter),
    path('chapter/editChapter/', chapters.api_edit_chapter),
    path('chapter/deleteChapter/', chapters.api_delete_chapter),

    path('getAllWorkers/', workers.api_get_all_workers),
    path('worker/createWorker/', workers.api_create_worker),
    path('worker/editWorker/', workers.api_edit_worker),
    path('worker/deleteWorker/', workers.api_delete_worker)
]