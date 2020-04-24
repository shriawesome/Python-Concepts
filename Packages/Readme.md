## Packages

  * Packages are modules that contains other modules.
  * Packages are generally implemented as directories containing a special `__init__.py` file.
  * The `__init__.py` file is executed when the package is imported.
  * Packages can contain sub packages  which themselves are implemented with the `__init__.py` files directories.

  * sys.path :
    * List of directories python checks for modules.
    * It can be used for adding user defined module entries in the path as well, so as to avoid import errors.
    * This can be done simply by ```sys.path.append('not_seached_directory')```

  * `PYTHONPATH` is the Environment variable listing the paths added to the sys.path
  * This can also be used to add the `not_seached_directory` to the sys.path without actually appending it.
  * For linux/Unix :
    * `export PYTHONPATH=not_seached_directory`
  * For Windows :
    * `set PYTHONPATH=not_seached_directory`

  * Process for Creating a Package :
    * |- Path_entry/    (Must be a sys.path)
      * |- my_Package/  (Directory containing your package)
      *   * |- `__init__.py`

  * For demo I've created a Reader Package that reads the bz2 and zip files automatically.
  * [Snapshot](https://github.com/shriawesome/Python-Concepts/blob/master/Packages/imgs/Reader_op1.png)
