# String Calculator

The following is a TDD Kata- an exercise in coding, refactoring and test-first, that you should apply daily for at least 15 minutes.

Before you start: 

* Try not to read ahead.
* Do one task at a time. The trick is to learn to work incrementally.
* Make sure you only test for correct inputs. there is no need to test for invalid inputs for this kata



## Requirements

We need the next tools to develop application:

* [ASDF](https://asdf-vm.com/)

And dependencies:

~~~bash
sudo apt update
sudo apt install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl git \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
~~~

Then, we install tools:

~~~bash
asdf plugin-add python
asdf plugin-add poetry https://github.com/asdf-community/asdf-poetry.git
asdf install
~~~~



## Installation

We should install project environment:

~~~bash
poetry install
~~~~


## Run test

Execute below command to run tests of the project:

~~~bash
poetry run pytest 
~~~
