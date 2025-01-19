# KATAS

Repository of the katas I have done. 

Each kata is in a different PR with a commit for each step to solve it.



## Requirements

We need the next tools to develop application:

* [ASDF](https://asdf-vm.com/):

Then, we install tools:

~~~bash
asdf plugin-add python
asdf plugin-add poetry https://github.com/asdf-community/asdf-poetry.git
asdf install
~~~~

And compile project:

~~~bash
poetry install
~~~~


## Run test

Execute below command to run tests of the project:

~~~bash
poetry run pytest 
~~~
