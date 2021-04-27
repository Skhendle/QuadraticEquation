# **Quadratic Equation Web-Application**


## **Introduction**
> ***This web appplication accepts three float inputs (a, b, and c) and returns possible solutions to the quadratic equation ax^(2) + bx + c = 0. Depending on the inputs, one can get two solutions, one solution, or none (no possible solutions). This application comprises of a backend and frontend which both have instructions in their respective folders on how to start them***
<br>


## **Architecture**
> Micro-Services. Most modern systems use this architecture because it is in line with agile methods of development. It helps create easy to maintain APIs and fast iterations during development. But more could be done on the backbone of this architecture. Here we created a fast method of developing any API regardless of its requirements. The file system of all the APIs is the same: main.py, service.py, input.py, route.py, test_unit.py, and __init__.py for imports. This uniform filing system ensures that everyone involved in the same project can easily understand what their teammates are up to and breaks up the code such that each file implements a single task. For example: service.py holds only the excecution logic of the API.

<br>

## **File structure and logic of each file**
```html
Backend:

Folder: quadratic_equation (API):

1.__init__.py : Allows imports between different folders.<br>
2. input.py : Models inputs and declares the type of data for each input<br>
3. route.py : Contains routeting logic. Since each folder has exactly one API, then this file contains only one route function.<br>
4. service.py : Contains the execution logic of the API (carries the logic for the requirements).<br>
5. main.py : Contains the logic to start the API (each API can launch on its own)<br>
6. test_unit.py : Contains the unit test for the function with exucuting logic in service.py.
```

