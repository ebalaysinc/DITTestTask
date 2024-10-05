### Модель Title
Содержит в себе следующие данные:
- name: Имя тайтла (TextField)
- link: Ссылка на обсуждение тайтла, например, на MangaLib (TextField)

### Модель Chapter
Содержит в себе следующие данные:
- Модель Title, к которому прикреплена глава (one-to-many)
- name: Имя главы (TextField)
- status: Глава в работе или завершена (BooleanField)
- original: Ссылка на оригинал/анлейт (TextField)

### Модель Worker
Содержит в себе следующие данные:
- Модель Chapter, к которому прикреплён работник (one-to-many)
- nickname: Ник работника (TextField)
- contact: Контакт для связи (TextField)
- occupation: Должность работника (TextField)