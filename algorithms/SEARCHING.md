## Searching Algorithms:  

Below is a table containing the searching algorithms this project visualises. <br>
The links in the table direct to a information about the algorithm and its implementation steps. 

| Algorithm                             |
| ------------------------------------- |
| [Linear Search](#linear-search)       |
| [Binary Search](#binary-search)       | 
| [Jump Search](#jump-search)           | 
| [Tenary Search](#tenary-search)       | 
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


Go to [README.md](../README.md)
