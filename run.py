import subprocess
import sys
import os
import re

# userage: python run.py 127.0.0.1 8001 customize IP and Port
# run by defalut: python run.py

reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

# installation pcakage
libs = ['PyMySQL', 'Pillow', 'Django']
print(installed_packages)
try:
    for item in libs:
        if item not in installed_packages:
            try:
                os.system("pip install " + item)
                print(item + ' installation success')
            except:
                print(item + ' Package installation fail')
    print('Package has been installed')
except:
    print("Failed SomeHow")
print('now run server cmd')

try:
    os.system('python manage.py migrate')
except:
    print('migrate failed')
try:
    os.system("python manage.py createsuperuser --username=admin --email=admin@example.com --traceback")
except:
    print('createsuperuser failed')
if len(sys.argv)>1 :
    if len(sys.argv) >2:
        pattern = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
        if re.match(pattern, sys.argv[1]) is not None and int(sys.argv[2])<=65545 and int(sys.argv[2])>0:
            os.system('python manage.py runserver ' + sys.argv[1] + ':' + sys.argv[2])
        else:
            print('args input error')
    else:
        os.system('python manage.py runserver ' + sys.argv[1] + ':8000')
else:
    print('run defalut')
    try:
        os.system('python manage.py runserver 127.0.0.1:8000')
    except:
        print('run defalut failed')