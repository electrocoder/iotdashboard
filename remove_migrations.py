"""
Iotdashboard project
Django 3.1
Python 3.8

Author: Sahin MERSIN

Demo: http://iotdashboard.pythonanywhere.com
Source: https://github.com/electrocoder/iotdashboard

https://iothook.com/
http://mesebilisim.com

The MIT License (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
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
