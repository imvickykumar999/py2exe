import os, shutil

# os.system('pip install pyinstaller')
os.system('pyinstaller --onefile hello.py')

shutil.move('dist/hello.exe', 'hello.exe')
shutil.rmtree('build')
shutil.rmtree('dist')
shutil.rmtree('__pycache__')

if os.path.exists("hello.spec"):
  os.remove("hello.spec")
