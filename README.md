# python-package-example

An example method to package a python desktop app on windows

Packaging Python desktop applications in Windows can be painful. There are tools that can ease the pain but from my experience they each have tradeoffs. Here is an example method to package a desktop application using the embedded python distribution and no third-party tools.

The embeddable version of Python is stripped down and isolated from the system registry. Checkout the python docs: [3.8. Embedded Distribution](https://docs.python.org/3/using/windows.html#embedded-distribution), andownload it [here](https://www.python.org/downloads/windows/).

---

## Install Pip

I wanted to use pip to ease the installation and maintenance of packages. Unfortunately embedded python does not come with pip support. We can install pip we just need to do a little work:

1. Extract ```python36.zip``` to a folder titled ```python36```.

2. Modify the ```python36._pth``` file which overrides sys.path meaning that the registry and enviroment variables will be ignored. You can read more .pth files in the Python Docs at [3.5. Finding modules](https://docs.python.org/3.6/using/windows.html#finding-modules). Edit your ```python36._pth``` to look like:

    ```python
    lib/site-packages
    python36
    .
    import site
    ```
3. Install pip with [get-pip.py](https://github.com/pypa/get-pip) which you can download from from [here](https://bootstrap.pypa.io/). Ensure you are in the correct folder when you run this command, or use the absolute path to the Python executable:

    ```Batchfile
    C:\Users\tarre\code\python-package-example\python-3.6.4-embed-win32\python.exe get-pip.py
    ```

Now we can use pip as normal. Be sure to call it from the embedded executable. For example:

```Batchfile
C:\Users\tarre\code\python-package-example\python-3.6.4-embed-win32\python.exe -m pip install <packagename>
```

---

## Install Your Packages

Now install the demo PyQt package. I am using absolute paths just to be explicit.

```Batchfile
C:\Users\tarre\code\python-package-example\python-3.6.4-embed-win32\python.exe -m pip install C:\Users\tarre\code\python-package-example\demo_app
```

---

## Launchers

Launching your app.

### Command Line

We can simply call it from the command line:

```Batchfile
C:\Users\tarre\code\python-package-example\python-3.6.4-embed-win32\python.exe -m pip demo_app
```

Of course your average user would not want to do this.

### Batch File

We can create a batch file.



### Shortcut


###







[Using CPython’s Embeddable Zip File](https://blogs.msdn.microsoft.com/pythonengineering/2016/04/26/cpython-embeddable-zip-file/)