from requests_html import HTMLSession
import json

username = input()
session = HTMLSession()

source = {'https://github.com/': 'Page not found · GitHub',
          'https://career.habr.com/': 'Хабр Карьера - ошибка 404',
          'https://pikabu.ru/@': '404. Страница не найдена',
          'https://reddit.com/user/': 'Reddit - Dive into anything',
          'https://instagram.com/': 'Страница не найдена • Instagram'
          }
sites = []
for key, value in source.items():
    url = key + username
    response = session.get(url)
    if response.status_code < 400:
        title = response.html.find('title', first=True) 
        t = title.text
        if t != value:
            sites.append(url)

d = dict()
d[username] = d.get(username, []) + sites
with open ('parse.json', 'a') as file:
        json.dump(d, file, indent=1)
