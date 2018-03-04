# python-package-example

An example method to package a python desktop app on windows
 
Packaging Python desktop applications in Windows can be painful. 

---

## Third Party Tools

There are number of third party tools which can make this task relatively easy. If you can get by using one of these, go for it. Unfortunately, each of these tools usually need a little help to make them work.

### [PyInstaller](http://www.pyinstaller.org/)

Probably the easiest to use. For the most part you can simply call ```pyinstaller myapp``` and it will work. I was happy with this method untill recently the .exe files produced by it started getting quarantined by Crowd Strike on my users computers. Since disabling Crowd Strike is not an option I had to look for other methods.

### [CXFreeze](https://anthony-tuininga.github.io/cx_Freeze/)

This requires a little extra work. I had trouble getting file assocations to work properly. Though, to be fair I only spent a few hours trying to debug it.

### [PyInsist](https://pynsist.readthedocs.io/en/latest/)

This tool is differenet from PyInstaller and CXFreeze in that it produces an installer with NSIS. 

### [py2exe](http://www.py2exe.org/)

### [Briefcase](https://pybee.org/project/projects/tools/briefcase/)

---

## Embedded Python

The embeddable version of Python is stripped down and isolated from the system registry. Checkout the python docs: [3.8. Embedded Distribution](https://docs.python.org/3/using/windows.html#embedded-distribution), andownload it [here](https://www.python.org/downloads/windows/).

___

## Installing Pip In Embedded Python

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
___

## Installing Packages in Embedded Python

Once pip is installed we can use pip as normal. Just be careful to call it from the embedded executable. It is probably safest to use its absolute path. For example:

```Batchfile
C:\Users\tarre\code\python-package-example\python-3.6.4-embed-win32\python.exe -m pip install <packagename>
```

I have provided two barebones demo apps in this distro to demonstrate console and GUI apps, they are very creatively titled demo_console, and demo_pyqt. Note that the demo apps utilizes entry_points which you can read about [here](http://setuptools.readthedocs.io/en/latest/pkg_resources.html?#entry-points), [here](https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and-scripts/), and [here](https://amir.rachum.com/blog/2017/07/28/python-entry-points/).

```Batchfile
C:\Users\tarre\code\python-package-example\python-3.6.4-embed-win32\python.exe -m pip install C:\Users\tarre\code\python-package-example\demo_pyqt

C:\Users\tarre\code\python-package-example\python-3.6.4-embed-win32\python.exe -m pip install C:\Users\tarre\code\python-package-example\demo_console
```

___

## Launchers

 The [Python docs](https://docs.python.org/3/using/windows.html#python-application) alluded to two different methods to launch python applications but they do not provide any examples.

## Batch File

We can create a batch file to call the app.

## Shortcuts

We can create windows shortcut.

## Specialized Executable

I think this is the most interesting method. We can write a bit of C/C++ to create a custom executable that simply calls Py_Main and passes a few arguments.

The benefits of this include:

* Custom Icon, and application metadata
* Easy file assocations
* Processes are unique and do not display as Python


[Using CPython’s Embeddable Zip File](https://blogs.msdn.microsoft.com/pythonengineering/2016/04/26/cpython-embeddable-zip-file/)

[custom-python-launcher](https://github.com/cprogrammer1994/custom-python-launcher)


[Distribute a Windows Python app with Inno Setup](http://www.entropyreduction.al/python/distutils/2017/09/21/bundle-python-app-w-inno-setup.html)