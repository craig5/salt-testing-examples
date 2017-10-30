default: help

SALT_GPG_KEY_URL = https://repo.saltstack.com/apt/ubuntu/16.04/amd64/latest/SALTSTACK-GPG-KEY.pub
SALT_XENIAL = deb http://repo.saltstack.com/apt/ubuntu/16.04/amd64/latest xenial main
SALTSTACK_APT_FILE = /etc/apt/sources.list.d/saltstack.list
#
VENV_DIR = venv
TESTS_DIR = tests
BIN_DIR = $(VENV_DIR)/bin
PIP_CMD = $(BIN_DIR)/pip
PYTHON_CMD = $(BIN_DIR)/python
FLAKE8_CMD = $(BIN_DIR)/flake8
NOSE_CMD = $(BIN_DIR)/nosetests
NOSE_ARGS = --nocapture --nologcapture --verbose

_add_key:
	wget --quiet -O - $(SALT_GPG_KEY_URL) | sudo apt-key add -

install: _add_key
	echo "$(SALT_XENIAL)" | sudo tee -a $(SALTSTACK_APT_FILE)
	sudo apt-get update
	sudo apt-get install --assume-yes python-virtualenv python-dev
	sudo sudo apt-get --assume-yes install salt-master salt-minion
	echo "master: localhost" | sudo tee -a /etc/salt/minion.d/master.conf
	sudo service salt-minion restart
	@echo "Install salt..."

dev:
	virtualenv $(VENV_DIR)
	$(PIP_CMD) install -r requirements.txt
	$(PIP_CMD) install -r tests/requirements.txt
	$(PIP_CMD) install -r dev_requirements.txt

test:
	$(FLAKE8_CMD) salt-files
	$(FLAKE8_CMD) tests
	$(NOSE_CMD) $(NOSE_ARGS) $(TESTS_DIR)

clean:
	@echo "Nothing to do, yet..."

help:
	@echo "Choose from the following:"
	@echo "	install		Install salt"
	@echo "	clean		Delete temp files"
	@echo "	help		This message"
