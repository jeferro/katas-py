# Cupcake Kata

Este kata se hizo originalmente para implementar el patron decorador.

## Descripción del problema

Escribe un programa que pueda hacer muchos pasteles con muchos ingredientes como: "Cupcake con chocolate y nueces" O "🧁 con 🍫 negro y 🥜 y 🍬". Ten cuidado, el orden de las capas es muy importante.

Escribe una función o método que pueda mostrar el nombre del pastel.

Escribe una función que pueda mostrar el precio del pastel. El precio se compone del precio del pastel base y el precio de la cobertura.

## Casos de prueba sugeridos

En pseudocódigo para construir una magdalena con chocolate, nueces y azúcar, escribiríamos algo así como:

~~~nodejs
var myCake = Sugar(Nuts(Chocolate(Cupcake())))
~~~

Con la escritura, podemos empezar a probar:

* Puedo poner un cupcake en una variable de tipo Cake
* 
Acerca de la función o método de nombre del cupcake:

La función de nombre debería devolver "🧁"
La función de nombre debería devolver "🍪"
La función de nombre debería devolver "🧁 con 🍫"
La función de nombre debería devolver "🍪 con 🍫"
La función de nombre debe devolver "🍪 con 🍫 y 🥜"
La función de nombre debe devolver "🍪 con 🥜 y 🍫"

Acerca de la función o método de precio:

La función de precio debería devolver 1 $ para "🧁"
La función de precio debería devolver 2 $ para "🍪"
La función de precio debería devolver 1,1 $ para "🧁 con 🍫"
La función de precio debería devolver 2,1 $ para "🍪 con 🍫"
La función de precio debería devolver 2,2 $ por "🍪 con 🥜"

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
