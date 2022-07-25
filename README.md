# MINIMUM PACKAGE DEMO
## Introduction
This repo is a template of a minimum python package builder as a quick starter.

## Installation
1. Download the package from [here](https://github.com/keemsunguk/min_package/blob/master/dist/min_package-1.0-py3-none-any.whl)
2. install in your working environment .
```buildoutcfg
pip install min_package-1.0-py3-none-any.whl
```
Alternatively, you can use it from the codebase.
```buildoutcfg
git clone https://github.com/keemsunguk/min_package.git
cd min_package
python3 -m venv mp_env
source mp_env/bin/activate
pip install -r requirements.txt
```
## SDLC
### Clean 
Known issues: snake_name naming style, type-check for Pandas object
```buildoutcfg
pylint <project root>/minpkg/
```

### UnitTest
Run unit test at the project root level
```buildoutcfg
python -m unittest discover
```

To use it from Jupyter without installing the package, install the kernel.
You will need to have ipykernel installed and have access to a working fwds_env.
```buildoutcfg
python -m ipykernel install --user --name mp_env --display-name mp_env
```
### Building a wheel file
To build your own distribution file, run the following command at the project root.
```buildoutcfg
python3 setup.py sdist bdist_wheel
```
### Building a requirements.txt
After install all desired and necessary packages, run the following command.
```buildoutcfg
pip freeze > requirements.txt
```

## VERSION HISTORY
### 1.0
Minimum files for packaging


