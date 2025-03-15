# Keeper Kata

We need software to deliver the proper data to the scoreboard for a basketball team. Unfortunately the people using our software are not the brightest lights under the sun, so they need six buttons (each team can score either 1, 2 or 3 points with a single shot).

Your Task

Write a class ScoreKeeper which offers following methods:

~~~python
def score_team_a1():
    pass

def score_team_a2():
    pass

def score_team_a3():
    pass

def score_team_b1():
    pass

def score_team_b2():
    pass

def score_team_b3():
    pass

def get_score():
    pass
~~~

Rules

The returned String always has seven characters. An example would be `000:000`



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
