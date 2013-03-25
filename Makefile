WANTLR = http://www.antlr3.org/download/Python/
ANTLR = antlr_python_runtime-3.1.3
WFUZZY = http://sourceforge.net/projects/pyfuzzy/files/pyfuzzy/
FUZZY = pyfuzzy-0.1.0
install:
        sudo apt-get update
        sudo apt-get update --assume-yes
        sudo apt-get upgrade --assume-yes
        sudo apt-get install python-setuptools --assume-yes
        sudo apt-get install git --assume-yes
        wget $(WANTLR)$(ANTLR).tar.gz
        tar xzf $(ANTLR).tar.gz
        cd ./$(ANTLR)/ ; sudo python setup.py install
        wget $(WFUZZY)$(FUZZY)/$(FUZZY).tar.gz
        tar xzf $(FUZZY).tar.gz
        cd ./$(FUZZY)/ ; sudo python setup.py install
        sudo easy_install pyFuzzy
        sudo apt-get install sqlite3
        sudo easy_install web.py
        sudo rm -R $(ANTLR)*
        sudo rm -R $(FUZZY)*
        sqlite3 todo.db < backend/schema.sql
# Need to move our files into appropriate directory #
# code.py model.py templates/index.html templates/base.html #
# to directory that easy install created /usr/local/lib/python2.7/dist-packages/web.py-0.37-py2.7.egg/web/ #
