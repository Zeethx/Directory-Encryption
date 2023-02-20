import subprocess

# define the required packages to install
required_packages = ["pycryptodome", "pyYAML"]

# install each package using pip
for package in required_packages:
    subprocess.check_call(["pip", "install", package])
