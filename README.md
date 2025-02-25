# spotifyCLI <img src="./images/spotifyLogo.png" alt="Logo" width="30" />
A simple command line interface to interact with spotify directly from the terminal

### Quick Setup
Create a directory and cd into it
```bash
$ mkdir spotifyCLI
$ cd spotifyCLI
```
Create a python virtual environment
```bash
$ python3 -m nenv {name} # I just call it 'spotifyCLI'
```
Activate the `venv`
```bash
$ . {name}/bin/activate # e.g. $ . spotifyCLI/bin/activate
```
OR
```bash
$ source {name}/bin/activate # e.g. $ source spotifyCLI/bin/activate
```
We create this virtual environment so that any packages installed are local to your directory and do not interfere with system-wide
packages.
### Package Requirement
This CLI tool uses Python's `click` package, but isn't requited to be installed separately.<br>
The setup.py file installs the package when forming symlink in later step.<br>
Run the following command in the current directory.
```bash
$ pip install --editable .
```
#### What's the purpose of doing it this way?
`setup.py` is a script used by Python's package manager (pip or setuptools) to let python know that your project script can be
installed as a package.<br>
Then when we run `pip install` with the `--editable` flag, it looks for that setup file and installs the script as a global package
which can then be run like any other command (`mkdir` or `numpy`). The `--editable` flag creates a symbolic link to your system's
global path so that any changes to the CLI script doesn't need to be copied to a new file, rather its just a pointer to the changed
file. This allows changes to the script to take effect immediately.

### Final Touches
Once everything is setup we can just deactivate our virtual environment by running:
```bash
$ deactivate
```

