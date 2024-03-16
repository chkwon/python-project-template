# python-project-template

## Installation
From the root directory of this repo:
```
pip install .
```
which will install a package named `mypypackage` to your Python package directory.

The dependency information with other package information is located in `pyproject.toml`


## Example 
To test if `mypypackage` is installed correctly, run the following code *outside* this repo:
```
import mypypackage
xyplot(0, 1, 10)
```

## Unit Test

```
cd tests
pytest
```