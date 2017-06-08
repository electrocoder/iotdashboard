# remove_migrations.py
"""
Run this file from a Django =1.7 project root. 
Removes all migration files from all apps in a project.
"""
from unipath import Path

this_file = Path(__file__).absolute()
current_dir = this_file.parent
dir_list = current_dir.listdir()

for paths in dir_list:
    migration_folder = paths.child('migrations')
    if migration_folder.exists():
        list_files = migration_folder.listdir()
        for files in list_files:
            split = files.components()
            try:
                if split[-1] != Path('__init__.py'):
                    files.remove()
            except:
                pass

for paths in dir_list:
    migration_folder = paths.child('__pycache__')
    if migration_folder.exists():
        list_files = migration_folder.listdir()
        for files in list_files:
            split = files.components()
            try:
                if split[-1] != Path('__init__.py'):
                    files.remove()
            except:
                pass
