# Algorithm Visualiser

Visualising algorithms in python.  
Created by Thomas Gibson.

---
| Table of contents                                              | 
| -------------------------------------------------------------- |
|   [1. Searching Algorithms](#searching-algorithms)             |  
|   [2. Searching Algorithms: Conventions](#searching-algorithms-conventions) |
|   


---

## Searching Algorithms:  
A list of each search algorithm the platform visualises.<br>
Each list entry contains some information on each algorithm.

---
### Linear Search:
---
Algorithm Steps:<br>
1. Starting at the beginning of the array 
2. Compare current value to the target
3. If the value is equal to the target then return true
4. If the value is not equal to the target then go to the next element
5. Repeat steps 2 - 5 until the end of array is reached or target is found
6. If the end of the array has been reached and target has not beem found, return false

Time Complexity: O(n)<br>
Space Complexity: O(1)

---
## Searching Algorithms: Conventions:
Please follow these conventions for files, classes and functions when adding new searching algorithms.<br> 
If any one of these conventions aren't met the automated system will not display the algorithm to the user and <br>subsequently won't visualise the algorithm.

--- 
### Naming Files: 
---
Please follow this format:
- algorithm_name_search.py 
- e.g. binary_search.py 
- e.g. linear_search.py 
---
### Naming Classes:
---
Please follow this format:
- AlgorithmNameSearch.py 
- e.g. BinarySearch 
- e.g. LinearSearch  
--- 

### Algorithm - Parent Class: 
--- 
Every new search algorithm must be a child of the Algorithm class. The Algorithm class contains an abstract method<br> called 'getName'. The 'getName' method should just return a string containing the algorithms name. <br> 
For example the equivalent method in the  BinarySearch class would return the string "Binary Search".

---
### Mandatory Function Naming and Arguments:

--- 

The function that actually executes the algorithm needs to be named in a specific way and take in certain arguments.<br><br> 
Please follow this convention:

- algorithmNameSearch(self, Searching)
- e.g. BinarySearch would have the follwing function - binarySearch(self, Searching)  
- e.g. LinearSearch would have the follwing function - linearSearch(self, Searching) 

The "Searching" arguement is an object that contains the array, target and displayArray() method the algorithm needs to run.

---


