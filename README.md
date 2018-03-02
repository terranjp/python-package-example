# python-package-example
An example method to package a python desktop app on windows


Creating desktop Python applications is painful. There are packages available to ease the pain but from my experience they each have tradeoffs. Here is an example method to package a deskptop application using the embeed python distribution. 

The embeddable version of Python is very stripped down and is relatively isolated. The Python docs describe about it [here](https://docs.python.org/3/using/windows.html#embedded-distribution).

Download the [embeddable zip file](https://www.python.org/downloads/windows/) from python.org and extract it. 

I wanted to use pip to ease the installation of packages. Unfortunately embedded python does not come with pip support. In order to add pip we have to modify the the 







[Using CPython’s Embeddable Zip File](https://blogs.msdn.microsoft.com/pythonengineering/2016/04/26/cpython-embeddable-zip-file/)




