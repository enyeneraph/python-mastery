
# Understanding Module Imports and File Imports

In the course of my Python journey, I have consistently encountered ImportError and FileNotFoundError issues. The former occurs more frequently than the latter. This mini article revisits the fundamentals and provides a guide on handling imports effectively to reduce these errors.

## What is a Module?
A module is a Python file that can contain variables, functions, and classes. 
Despite its name, a module is not a collection of files in a folder but a single file. The term "module" might seem to imply multiple entities, but it actually refers to the various elements defined within a single python file.

Example:

```python
Copy code
# mymodule.py
def greet(name):
    return f"Hello, {name}!"
```

## Understanding the Import System

Typically, after writing a script containing some functions, you'll need to import these functions into another script. The common syntax is:

```python
Copy code
from mymodule import greet
```

This is where issues may or may not arise. You might see all your files and their directories, but Python has a specific mechanism for handling imports.

The sys.path list defines the paths Python searches for the module you want to import. The first argument in sys.path is the parent directory of your entry point, i.e., the file you passed to the Python interpreter.

If your module is within the same directory as your running file, easypeasy. However, things get tricky when the module is outside that directory.

## How to Import Modules not contained in the same directory as your input script
1. The solutions that involve modifying sys.path (`sys.path.append` and `sys.path.insert`) Personally, I don't think these are the best. But sometimes you just need a quick fix.
2. Using the __init__.py (This is a bit of an issue(doesn't work), cos' python no longer needs __init__.py to turn a folder to a package. Every folder is a package.)

To be continued
Resource: https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html

#Todo
1. difference between nameespace package and ...
2. Solution to import issues
3. Deeper dive to how python handles import in large prrojects e.g currentt project