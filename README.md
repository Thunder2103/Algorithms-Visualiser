# Algorithm Visualiser

Written in python by Thomas Gibson.

---
| Table of contents                                                      | 
| ---------------------------------------------------------------------- |
|   [1. Searching Algorithms](#searching-algorithms)                     |  
|   [2. Sorting Algorithms](#sorting-algorithms)                         |
|   [3. Adding a new Search Algorithm](#adding-a-new-search-algorithm)   |
|   [4. Adding a new Sorting Algorithm](#adding-a-new-sorting-algorithm) |
---

## Searching Algorithms:  

Below is a table containing the searching algorithms this project visualises. <br>
The links in the table direct to a information about the algorithm and its implementation steps. 

| Algorithm |
| --------- |
| [Linear Search](#linear-search) |
| [Binary Search](#binary-search) | 
| [Jump Search](#jump-search) | 
| [Tenary Search](#tenary-search) | 
| [Fibonacci Search](#fibonacci-search) | 

---
### Linear Search:
---
Algorithm Steps:<br>
1. Starting at the beginning of the array 
2. Compare current value to the target
3. If the value is equal to the target then return 1
4. If the value is not equal to the target then go to the next element
5. Repeat steps 2 - 4 until the end of array is reached
6. If the end of the array has been reached and target has not been found, return 0

Time Complexity: O(n)<br>
Space Complexity: O(1)

---
### Binary Search: 
---
Algorithm steps:

1. Intialise a variable called low with a value of 0
2. Intialise a variable called high that is equal to the length of the array minus one
3. While low is less than or equal to high 
4. Initialise a varible called mid, it's value is calculated by [the formula](#mid-formula)
5. If the value at index mid is equal to the target, return 1
6. If the value at index mid is greater than the target, set low to mid plus one
7. If the value at index mid is less than the target, set high to mid minus one 
8. Repeat steps 3 - 7 until low is greater than high
9. If the loop terminates, return 0

Time complexity: O(log n)<br>
Space Complexity: O(1)

#### mid formula: 

$mid = {(low+high) \div 2}$

---
### Jump Search: 
--- 
Algorithm Steps:

1. Initialize a variable called step and set it's value to $\sqrt{n}$ (where n is the length of the array)
2. Create a variable called prev and set it's value to 0
3. While step is less than n, set prev to the value of step and then increment step by $\sqrt{n}$. <br>
If prev is greater than or equal to n, return false. Else if the value at index step is greater than target, break loop.   
4. Initialize a loop starting at the value of prev until prev + $\sqrt{n}$  
5. If the current index is equal to the target, return 1
6. If the current index is greater than the target, return 0
7. Else repeat steps 5 - 6 until reached index corresponding to prev + $\sqrt{n}$  

Time Complexity: O($\sqrt{n}$)<br>
Space Complexity: O(1)

---
### Tenary Search:
--- 
Algorithm Steps: 

1. Intialise a variable called left with a value of 0
2. Intialise a variable called right that is equal to the length of the array minus one
3. While left is less than or equal to right 
4. Initialise a varible called mid1, calculate it's value using [the formula](#mid1-formula)
5. Initialise a varible called mid2, calculate it's value using [the formula](#mid2-formula) 
6. If the value at index mid1 or mid2 is equal to the target, return 1 
7. If the value at index mid1 is less than the target, set right to mid1 - 1 
8. If the value at index mid2 is greater than the target, set left to mid2 + 1
9. Else, set left to mid1 + 1 and set right to mid2 - 1 
10. Repeat steps 3 - 9
11. If the loop terminates, return 0 

Time Complexity: O(log<sub>3</sub>n) <br>
Space Complexity: O(1) 

#### mid1 formula:

$mid1 = {left + (right - left) \div 3}$

#### mid2 formula: 

$mid2 = {right - (right - left) \div 3}$

---
### Fibonacci Search: 
--- 
Algorithm Steps: 

1. Calculate the largest Fibonacci number greater than or equal to the size of the array, store it in a variable called fibN
2. Calculate the Fibonacci number before fibN, store it in a variable called fibNMin1 
3. Calculate the Fibonacci number before fibNMin1, store it in a variable called fibNMin2  
4. Initialise a variable called offset, set it to -1 
5. Initialise a variable called n, set it to the length of the array
6. While fibN is greater than 1 
7. Initialise a variable called index, it's value is given by [the formula](#index-formula)
8. If the element at index is less than the target, move all the Fibonacci numbers, two Fibonacci numbers down. set offset to be equal to index 
9. Else if the element at index is greater than the target, move all the Fibonacci numbers, one Fibonacci number down  
10. Else, the target has been found, return 1 
11. Repeat steps 6 to 10 
12. If fibMin1 is greater than 0 and the last element in the array is the target, return 1 
13. Else, return 0

Time Complexity: O(log n) <br>
Space Complexity: O(1) 

#### index formula:

$index = {\min(offset + fibNMin2, n - 1)}$

---
### Exponential Search:
--- 
Algorithm Steps:

1. If the first element in the array is the target, return 1 
2. Initialise a variable called i, set it to 1 
3. Initialise a variable called n, set it to the length of the array 
4. While i is less than n and the element at index i is less than or equal to the target 
5. Double the value of i 
6. Repeat Steps 5 - 6 
7. Perform a [binary search](#binary-search), the initialise values for [low](#initial-low-value) and [high](#initial-high-value) are given below

Time Complexity: O(log n) <br>
Space Complexity: O(1) 

#### Starting low value:

$low = i \div 2$ 

#### Starting high value:

$high = \min(i, n - 1)$ 

---
### Interpolation Search: 
---
Algorithm Steps:

1. Initialise a variable called low and set it to 0 
2. Initialise a variable called high and set it to the length of the array - 1 
3. While low is less than or equal to high AND target is greater than or equal to the value at index low AND target is less than or equal to the value at index high
4. Initialise a value called pos and calculate it's value using [the formula](#pos-formula)
5. If the value at index pos is equal to the target, return 1 
6. If the value at index pos is greater than the target, set high to pos - 1 
7. If the value at index pos is less than the target, set low to pos + 1 
8. Repeat steps 3 - 7 
9. If the loop terminates and the target is not found, return 0

Time Complexity: O(log (log n)) <br>
Space Complexity: O(1) 

#### pos formula:

$$pos = {low+{(target-array[low])\times(high - low)\over(array[high]-array[low])}}$$

---

## Sorting Algorithms:

Below is a table containing the sorting algorithms this project visualises. <br>
The links in the table direct to a information about the algorithm and its implementation steps. 

| Algorithm |
| --------- |
| [Bubble Sort](#bubble-sort) |
| [Merge Sort](#merge-sort) |
| [Bogo Sort](#bogo-sort) |


---
### Bubble Sort:
--- 
Algorithm steps: 

1. Loop through the array from left to right
2. At the beginning of each iteration set a boolean flag to False 
3. In a nested loop, traverse from the beginning of the array to the end of the unsorted array using [this formula](#index-of-last-sorted-element-formula)
4. Compare the current element to the element adjacent to it 
5. If the current element is greater than the adjacent elment, swap them and set the boolean flag to True 
6. When the nested loop has terminated check the value of the boolean flag 
7. If the boolean flag is True, continue for another iteration 
8. If the boolean flag is False, the array is sorted and the algorithm should terminate. 

Time Complexity: O(n<sup>2</sup>) <br>
Space Complexity: O(1)

#### End of unsorted array formula: 

$$ index = n - i - 1$$

n -> length of the array <br>
i -> index of current element 

---
### Merge Sort:
---
Algorithm Steps:

1. Divide the array into sub-arrays of size one. (Arrays of size one are considered sorted)
2. Compare the elements in each of the sub-arrays, inserting them in numerical order into a new sub-array 
3. Repeat step 2 until all the sub-arrays have been merged leaving only one sorted array 

Time Complexity: O(n log n) <br>
Space Complexity: O(n)

---
### Bogo Sort:
---

Algorithm Steps: 

1. Randomly shuffle array 
2. If array is sorted, stop.
3. If array is not sorted repeat step 1. 

Time Complexity: O((n + 1)!)<br>
Space Complexity: O(1)

## Adding a new Search Algorithm
New search algorithms can be added if they meet these requirements:

---
### Quick Sort:
---

Algorithm Steps: 

1. Initialise a variable called low and assign it the value 0 
2. Initialise a variavle called high and assign it the length of the array minus one 
3. Select pivot using median of three 
4. All elements less than the pivot must be placed to the left of the pivot
5. All elements greater than the pivot must be places to the right of the pivot
6. Two new pivots need to be selected to sort the separate halves of the array 
7. The first pivot should be in the range, low to index of current pivot - 1
8. The second pivot should be in the range, index of current pivot + 1 to end
9. Repeat steps 3 - 8 until low is greater than pivot index - 1 and pivot index + 1 is greater than end 

Time Complexity: O(log n) <br>
Time Complexity: O(n<sup>2</sup>)  (If the pivot is chosen poorly)<br>
Space Complexity: O(1) 

#### Median of three

- Get the elements at low, high and (low + high) / 2 
- Place the element in an array and sort 
- The pivot is the middle value (element in index 1)

---
## Adding a new Search Algorithm
New search algorithms can be added if they meet these requirements:

| Requirement: | Description: |
| ------------ | ------------ | 
| Location     | New algorithm files must be found in the <b>algorithms/searching</b> directory | 
| File Name    | New files must be named in the following format: <b>algorithm_name_search.py.</b> <br> e.g. binary_search.py, linear_search.py |
| Class Implementation        | The algorithm must be implemented as a class. | 
| Class Name   | An algorithm class must be named in the following format: <b>AlgorithmNameSearch.</b> <br> e.g BinarySearch, LinearSearch | 
| Inheritance  | Each algorithm class must be a child of the [Algorithm class](#algorithm-class). <br> The Algorithm class must be imported (See [imports](#imports).) | 
| Constructor | Each new class must implement a constructor. (See [Constructor](#constructor)) |
| DataModel helper functions   | The DataModel class contains useful functions that will be needed (See [DataModel](#datamodel-class)) | 
| Function Naming | The function which implements the algorithm must be named in the following format: <b>algorithmNameSearch</b> <br> e.g. binarySearch and linearSearch |
| Function Implementation | Each new algorithm class must provide an implementation for the <b>getName()</b> method. (See [Algorithm class](#algorithm-class))  |
| Return value/s          | Each algorithm doesn't strictly need to return anything. <br> As a convention, 1 for success or -1 for failure should be returned | 

--- 

## Adding a new Sorting Algorithm 

New sorting algorithms can be added if they meet these requirements:

| Requirement: | Description: |
| ------------ | ------------ | 
| Location     | New algorithm files must be found in the <b>algorithms/sorting</b> directory | 
| File Name    | New files must be named in the following format: <b>algorithm_name_sort.py.</b> <br> e.g. bubble_sort.py, merge_sort.py |
| Class Implementation        | The algorithm must be implemented as a class. | 
| Class Name   | An algorithm class must be named in the following format: <b>AlgorithmNameSort.</b> <br> e.g BubbleSort, MergeSort | 
| Inheritance  | Each algorithm class must be a child of the [Algorithm class](#algorithm-class). <br> The Algorithm class must be imported (See [imports](#imports).) | 
| Constructor | Each new class must implement a constructor. (See [Constructor](#constructor)) |
| DataModel helper functions   | The DataModel class contains useful functions that will be needed (See [DataModel](#datamodel-class)) | 
| Function Naming | The function which implements the algorithm must be named in the following format: <b>algorithmNameSort</b> <br> e.g. bubbleSort and mergeSort |
| Function Implementation | Each new algorithm class must provide an implementation for the <b>getName()</b> method. (See [Algorithm class](#algorithm-class))  |
| Return value/s          | Each algorithm doesn't strictly need to return anything. <br> As a convention, 1 for success or -1 for failure should be returned | 
| Sorting in Ascending and Descending order | Code does not need to be written in an algorithms implementation to sort in ascending and descending order. A helper function in the [Algorithm class](#algorithm-class) returns True or False if two elements need to be swapped, another helper function can then be called to make this swap. |  

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
| getElement()     | index (int) : index of the element to be retieved | The value at the specified index, or -1 if the index is out of bounds | Gets the value of the element at the specified index (See [DataModel](#datamodel-class)) | 
| changeElement()  | index (int) : index of the element to be changed <br> value (int): The new value that the element is being replaced with| None | Changes the value at the specified index to the value passed (See [DataModel](#datamodel-class)) | 
| swapElements() | sourceIdx (int) : index of an element to be swapped destIdx (int): index of an element to be swapped | none | Swaps the elements at the specified indexes. (See [DataModel](#datamodel-class))|
| sortArray() | None    | delay (bool): By default there is a small delay when the array is sorted. Setting this parameter to False removed this delay | Sorts the array and refreshes the screen to display it. (See [DataModel](#datamodel-class)).| 
| shuffleArray() | None | delay (bool): By default there is a small delay when the array is shuffled. Setting this parameter to False removed this delay | Randomly shuffles the array and refreshes the screen to display it. (See [DataModel](#datamodel-class)). | 
| changeBarColour() | index (int) : Position to have the colour changed. <br> colour (str) : The new colour | None | Changes the colour of the bar at the specified index. (See [DataModel](#datamodel-class)). | 
| swapbarColours() | sourceIdx (int) : index of a bar colour to be swapped destIdx (int): index of a bar colour to be swapped | none | Swaps the bar colours at the specified indexes. (See [DataModel](#datamodel-class))|
| isSwapNeeded()   | sourceIdx (int) : index of an element to be checked. destIdx (int): index of an element to be checked | A boolean value, True if the elements need to be swapped otherwise False is returned | Checks if the elements at the passed indexes need to be swapped. (Works for both sorting in descending and ascending order) | 
| areElementsEqual() | sourceIdx (int) : index of an element to be checked. destIdx (int): index of an element to be checked | A boolean value, True if the elements at the specified index are true, else false | Compared the elements at the specified indexes and returns True if they are equal | 
| getTarget() | None    | The target to be searched for | Returns the target to be searched for. (See [DataModel](#datamodel-class)). |
| updateArrayOnScreen() | None     | None | Refreshes the screen to display any changes to the array. (See [DataModel](#datamodel-class)). |  
| delay() | None        | None     | Pauses the execution of the program using <b> time.sleep().</b> |


### DataModel class:

Useful functions, most are wrapped by the [Algorithm](#algorithm-class) class. <br>
The functions can still be called directly, if an attribute containing the DataModel class is created (not recommended). 

| Function | Parameters | Returns  | Description: |
| -------- | ---------- | -------- | ------------ |
| getArray() | None     | The array to be processed | Returns the array to be iterated over |
| getElementAtIndex()     | index (int) : index of the element to be retieved | The value at the specified index, or -1 if the index is out of bounds | Gets the value of the element at the specified index | 
| changeElement()  | index (int) : index of the element to be changed <br> value (int): The new value that the element is being replaced with| None | Changes the value at the specified index to the value passed | 
| swapElements() | sourceIndex (int) : index of an element to be swapped destinationIndex (int): index of an element to be swapped | none | Swaps the elements at the specified indexes. |
| updateArrayOnScreen() | None | None | Redraws the array on screen | 
| sortArray()    | None | None | Sorts the array and refreshes the screen to display it. |
| shuffleArray() | None | None | Randomly shuffles the array and refreshes the screen to display it. | 
| setBarColour() | index (int) : Position to have the colour changed. <br> colour (str) : The new colour | None | Changes the colour of the bar at the specified index | 
| swapbarColours() | sourceIndex (int) : index of a bar colour to be swapped destinationIndex (int): index of a bar colour to be swapped | none | Swaps the bar colours at the specified indexes. |
| isAscending()    | None | Returns True if the sorting direction is in ascending order. <br> Returns False if the sorting direction is in descending order | Returns the boolean value corresponding to the direction of the sort | 
| getTarget() | None    | The target to be searched for | Returns the target to be searched for |

---

