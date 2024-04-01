# Algorithm Visualiser

Written in python by Thomas Gibson.

---
| Table of contents                                              | 
| -------------------------------------------------------------- |
|   [1. Searching Algorithms](#searching-algorithms)             |  
|   [2. Adding a new Search Algorithm](#adding-a-new-search-algorithm) |

---

## Searching Algorithms:  
--- 
Below is a table containing the algorithms this project visualises. <br>
The links in the table direct to a information about the algorithm and its implementation steps. 

| Algorithm |
| --------- |
| [Linear Search](#linear-search) |
| [Binary Search](#binary-search) | 
| [Jump Search](#jump-search) | 

---
### Linear Search:
---
Algorithm Steps:<br>
1. Starting at the beginning of the array 
2. Compare current value to the target
3. If the value is equal to the target then return true
4. If the value is not equal to the target then go to the next element
5. Repeat steps 2 - 4 until the end of array is reached
6. If the end of the array has been reached and target has not been found, return false

Time Complexity: O(n)<br>
Space Complexity: O(1)

---
### Binary Search 
---
Algorithm steps:

1. Intialise a variable called low with a value of 0
2. Intialise a variable called high that is equal to the length of the array minus one
3. While low is less than or equal to high 
4. Initialise a varible called mid and set it to, (low + high) // 2
5. If the value at index mid is equal to the target, return True
6. If the value at index mid is greater than the target, set low to mid plus one
7. If the value at index mid is less than the target, set high to mid minus one 
8. Repeat steps 3 - 7 until low is greater than high
9. If the loop terminates, return False

Time complexity: O(log n)<br>
Space Complexity: O(1)

---

### Jump Search 
--- 
Algorithm Steps:

1. Initialize a variable called step and set it's value to $\sqrt{n}$ (where n is the length of the array)
2. Create a variable called prev and set it's value to 0
3. While step is less than n, set prev to the value of step and then increment step by $\sqrt{n}$. <br>
If prev is greater than or equal to n, return false. Else if the value at index step is greater than target, break loop.   
4. Initialize a loop starting at the value of prev until prev + $\sqrt{n}$  
5. If the current index is equal to the target, return true
6. If the current index is greater than the target, return false
7. Else repeat steps 5 - 6 until reached index corresponding to prev + $\sqrt{n}$  

Time Complexity: O($\sqrt{n}$)<br>
Space Complexity: O(1)

---
## Adding a new Search Algorithm
New search algorithms can be added if they meet these requirements:

| Requirement: | Description: |
| ------------ | ------------ | 
| Location     | New algorithm files must be found in the <b>algorithms/searching</b> directory | 
| File Name    | New files must be named in the following format: <b>algorithm_name_search.py.</b> <br> e.g. binary_search.py, linear_search.py |
| Class Implementation        | The algorithm must be implemented as a class. | 
| Class Name   | An algorithm class must be named in the following format: <b>AlgorithmNameSearch.</b> <br> e.g BinarySearch, Linearsearch | 
| Inheritance  | Each algorithm class must be a child of the [Algorithm class](#algorithm-class). <br> The Algorithm class must be imported (See [imports](#Imports).) | 
| Constructor | Each new class must implement a constructor. (See [Constructor](#constructor)) |
| DataModel helper functions   | The DataModel class contains useful functions that will be needed (See [DataModel](#datamodel-class)) | 
| Function Naming | The function which implements the algorithm must be named in the following format: <b>algorithmNameSearch</b> <br> e.g. binarySearch and linearSearch |
| Function Implementation | Each new algorithm class must provide an implementation for the <b>getName()</b> method. (See [Algorithm class](#algorithm-class))  |

--- 

### Imports:

```python 
from ..algorithm import Algorithm 
```
<i> Import statement needed to import Algorithm parent class </i>

--- 

### Constructor 

```python 
def __init__(self, dataModel):
        super().__init__(dataModel)
```
<i> Constructor required (See [DataModel](#datamodel-class)) </i>

---

### Algorithm class: 

The algorithm class is a wrapper for some of the [DataModel](#datamodel-class) class functions. <br>
These functions are needed to interact with the visualizer properly. <br>
The methods in DataModel can still be called directly (not recommended).

| Function | Parameters | Returns  | Description: |
| -------- | ---------- | -------- | ------------ |
| getName()| None       | A String, contains the name of the algorithm being implemented | An abstract method. Every subclass must provide an implementation. | 
| getArray() | None     | The array to be processed | Returns the array to be iterated over. (See [DataModel](#datamodel-class)). |
| getTarget() | None    | The target to be searched for | Returns the target to be searched for. (See [DataModel](#datamodel-class)). |
| updateArrayOnScreen() | None     | None | Refreshes the screen to display any changes to the array. (See [DataModel](#datamodel-class)). |  
| changeBarColour() | index (int) : Position to have the colour changed. <br> colour (str) : The new colour | None | Changes the colour of the bar at the specified index. (See [DataModel](#datamodel-class)). | 
| sortArray() | None    | None     | Sorts the array and refreshes the screen to display it. (See [DataModel](#datamodel-class)).| 
| shuffleArray() | None | None     | Randomly shuffles the array and refreshes the screen to display it. (See [DataModel](#datamodel-class)). | 
| delay() | None        | None     | Pauses the execution of the program using <b> time.sleep().</b> |

### DataModel class:

Useful functions, most are wrapped by the [Algorithm](#algorithm-class) class. <br>
The functions can still be called directly, if an attribute containing the DataModel class is created (not recommended). 

| Function | Parameters | Returns  | Description: |
| -------- | ---------- | -------- | ------------ |
| getArray() | None     | The array to be processed | Returns the array to be iterated over |
| getTarget() | None    | The target to be searched for | Returns the target to be searched for |
| updateArrayOnScreen() | None | None | Redraws the array on screen | 
| setBarColour() | index (int) : Position to have the colour changed. <br> colour (str) : The new colour | None | Changes the colour of the bar at the specified index | 
| sortArray()    | None | None | Sorts the array and refreshes the screen to display it. |
| shuffleArray() | None | None | Randomly shuffles the array and refreshes the screen to display it. | 

---



