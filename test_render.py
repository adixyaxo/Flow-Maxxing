import os
from jinja2 import Environment, FileSystemLoader

class Dummy(dict):
    def __getattr__(self, name):
        return Dummy()
    def __getitem__(self, name):
        return Dummy()

env = Environment(loader=FileSystemLoader('templates'))
context = {
    'active_page': 'dashboard',
    'user': {'first_name': 'A', 'last_name': 'B', 'email': 'a@b.com', 'preferences': [1,1,1]},
    'date_joined': '2023-01-01',
    'note': {'tags': ['tag1'], 'title': 't', 'date_created': '2023', 'content': 'c'},
    'notes': [],
    'tasks': [],
    'code': '404',
    'title': 'Error',
    'message': 'msg',
}

for root, dirs, files in os.walk('templates'):
    for f in files:
        if f.endswith('.html'):
            path = os.path.relpath(os.path.join(root, f), 'templates')
            try:
                env.get_template(path).render(**context)
                print(f"OK: {path}")
            except Exception as e:
                print(f"Error in {path}: {type(e).__name__} - {e}")
