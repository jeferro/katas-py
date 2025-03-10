# KATAS

Repository of the katas I have done. 

Each kata is in a different PR with a commit for each step to solve it.



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
