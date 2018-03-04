#!C:\Users\tarre\code\python-package-example\python-3.6.4-embed-win32\pythonw.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'demo-app==0.1','gui_scripts','demo_app'
__requires__ = 'demo-app==0.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('demo-app==0.1', 'gui_scripts', 'demo_app')()
    )
