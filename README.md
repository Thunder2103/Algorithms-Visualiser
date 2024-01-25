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

1. Initialise a variable called step and set it's value to $\sqrt{n}$ (where n is the length of the array)
2. Create a variable called prev and set it's value to 0
3. While step is less than n, set prev to the value of set and increment step by $\sqrt{n}$. <br>
If prev is greater than or equal to n, return false. Else if the value at index step is greater than target, break loop.   
4. Starting at index corresponding to prev value
5. If the current index is equal to the target, return true
6. If the current index is greater than the target, retirn false
7. Repeat steps 5 - 6 until reached index corresponding to prev + $\sqrt{n}$  

Time Complexity: O($\sqrt{n}$)<br>
Space Complexity: O(1)

---
## Adding a new Search Algorithm
To add a new search algorithm, the follwing requirements must be met.

| Requirement: | Description: |
| ------------ | ------------ | 
| Location     | New algorithm files must be found in the <b>algorithms/searching</b> directory | 
| File Name    | New files must be named in the following format: <b>algorithm_name_search.py.</b> <br> e.g. binary_search.py, linear_search.py |
| Class Implementation        | The algorithm must be implemented as a class. | 
| Class Name   | An algorithm class must be named in the following format: <b>AlgorithmNameSearch.</b> <br> e.g BinarySearch, Linearsearch
| Inheritance  | Each algorithm class must be a child of the Algorithm class | 
| Function Implementation | As each new algorithm class must be a child class of the <br>[Algorithm class](#parent-class---algorithm)</b>, they must provide an implementation for the getName() method.  |
| Function Naming | The function which implements the algorithm must be named in the following format: algorithmNameSearch <br> e.g. binary search would be binarySearch and linear search would be linearSearch |
| Function Parameters | Each function that implements the new algorithm must include [two manditory parameters](#algorithm-implementation---parameters) |

--- 

### Parent Class - Algorithm: 
--- 
Every new search algorithm must be a child of the Algorithm class. <br>
The algorithm class contains the abstract methid 'getName()' which each new algorithm class must provide an implementation for. <br>
The 'getName()' class should return a string which contains the algorithms namme. <br>
For the BinarySearch class 'getName()' would return "binary search". <br>
For the LinearSearch class 'getName()' would return "linear search".

---
### Algorithm Implementation - Parameters:

--- 

The function that actually executes the algorithm needs to take in certain arguments.<br>

| Argument: | Description: |
| self     | Allows function to be called and attributes from the Algorithm class to be entered
| Searching | Searching contains data the algorithm needs to execute such as the array to be searched and target to searched for |

---


