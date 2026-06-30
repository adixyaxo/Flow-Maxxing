import os
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))
for root, dirs, files in os.walk('templates'):
    for f in files:
        if f.endswith('.html'):
            try:
                env.get_template(os.path.relpath(os.path.join(root, f), 'templates'))
            except Exception as e:
                print(f"Error in {f}: {e}")
