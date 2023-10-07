# Algorithm Visualiser

Written in python by Thomas Gibson.

---
| Table of contents                                              | 
| -------------------------------------------------------------- |
|   [1. Searching Algorithms](#searching-algorithms)             |  
|   [2. Searching Algorithms - Conventions](#searching-algorithms) |
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
5. Repeat steps 2 - 4 until the end of array is reached or target is found
6. If the end of the array has been reached and target has not beem found, return false

Time Complexity: O(n)<br>
Space Complexity: O(1)

---
### Binary Search 
---
Algorithm steps:

1. Intialise a variable called low with a value of 0
2. Intialise a variable called high that is equal to the length of the array minus one
3. While low is less than or equal to high 
4. Calculate mid - (low + high) // 2
5. If the value at mid is equal to the target, return True
6. If the value at mid is greater than the target, set low to mid plus one
7. If the value at mid is less than the target, set high to mid minus one 
8. Repeat steps 3 - 7 
9. If the loop terminates, return False

Time complexity: O(log n)<br>
Space Complexity: O(1)

---
## Searching Algorithms - Conventions:
Please follow these conventions for files, classes and functions when adding new searching algorithms.<br> 
If any one of these conventions aren't met the automated system will not display the algorithm to the user and <br>subsequently won't visualise the algorithm.

--- 
### Naming Files: 
---
New algorithms must be in files created in the "searching_algorithms" directory.

Please follow this format:
- algorithm_name_search.py 
- e.g. binary_search.py 
- e.g. linear_search.py 

Please note the file <b>must</b> end in "search.py" otherwise the automated system won't show the algorithm as an option to the user.<br>
(Technically the file can be called anything as long as it ends with "search.py")

---
### Naming Classes:
---
New algorithms must be implemented as a class.<br>
Each class must be a child class of the [Algorithm class](#algorithm---parent-class) and implement a [mandatory method](#mandatory-function-naming-and-arguments)

Please follow this format:
- AlgorithmNameSearch
- e.g. BinarySearch 
- e.g. LinearSearch  
--- 

### Parent Class - Algorithm: 
--- 
Every new search algorithm must be a child of the Algorithm class. The Algorithm class contains an abstract method<br> called 'getName()' which must be implemented.<br> 
The 'getName()' method should return a string containing the algorithms name. Each word in the string should be capitalised.<br>
E.g. the binary search classes 'getName()' method would return the string "Binary Search"

---
### Mandatory Function Naming and Arguments:

--- 

The function that actually executes the algorithm needs to be named in a specific way and take in certain arguments.<br><br> 
Please follow this convention:

- algorithmnameSearch(self, Searching)
- e.g. BinarySearch would have the following function - binarySearch(self, Searching)  
- e.g. LinearSearch would have the follwing function - linearSearch(self, Searching) 

The "Searching" argument is an object that contains all the variables and methods a searching algorithm needs to actually run.

---


