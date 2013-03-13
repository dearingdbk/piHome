install:
        #sudo apt-get update
        #sudo apt-get update --assume-yes
        #sudo apt-get upgrade --assume-yes
        sudo apt-get install python-setuptools --assume-yes
        wget http://www.antlr3.org/download/Python/antlr_python_runtime-3.1.3.tar.gz
        tar xzf antlr_python_runtime-3.1.3.tar.gz
        cd antlr_python_runtime-3.1.3/
        sudo python setup.py install
        wget http://sourceforge.net/projects/pyfuzzy/files/pyfuzzy/pyfuzzy-0.1.0/pyfuzzy-0.1.0.tar.gz
        tar xzf pyfuzzy-0.1.0.tar.gz
        cd pyfuzzy-0.1.0.tar.gz
        sudo python setup.py install
