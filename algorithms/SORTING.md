## Sorting Algorithms:

Below is a table containing the sorting algorithms this project visualises. <br>
The links in the table direct to a information about the algorithm and its implementation steps. 

| Algorithm                                     |
| --------------------------------------------- |
| [Bubble Sort](#bubble-sort)                   |
| [Merge Sort](#merge-sort)                     |
| [Bogo Sort](#bogo-sort)                       |
| [Quick Sort](#quick-sort)                     |
| [Selection Sort](#selection-sort)             |
| [Insertion Sort](#insertion-sort)             |
| [Tim Sort](#tim-sort)                         |
| [Cocktail Shaker Sort](#cocktail-shaker-sort) |

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


#### A note on the Space Complexity 

An O(1) space complexity can be achieved by merging the sub arrays in-place. 

---

### Bogo Sort:
---

Algorithm Steps: 

1. Randomly shuffle array 
2. If array is sorted, stop.
3. If array is not sorted repeat step 1. 

Time Complexity: O((n + 1)!)<br>
Space Complexity: O(1)

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

Time Complexity: O(n log n) <br>
Space Complexity: O(1)  

#### A note on the Time Complexity 

If the pivot is not chosen efficiently, the worst case time complexity becomes O(n<sup>2</sup>)

#### Median of three

- Get the elements at low, high and (low + high) / 2 
- Place the element in an array and sort 
- The pivot is the middle value (element in index 1)

---

### Selection Sort:
---

Algorithm Steps: 

1. Iterate through the array
2. Set a variable called minIdx to the current index
3. In a nested loop from the current index plus one to the end of the array
4. Find the index of the smallest element and store it in minIdx 
5. Shift all elements between the current index and the smallest element index one place right 
6. Place the smallest element into the current index

Time Complexity: O(n<sup>2</sup>)<br>
Space Complexity: O(1)

---

### Insertion Sort:
---

Algorithm Steps: 

1. Consider the first element in the array as already sorted 
2. Iterate through the array (starting at the second element)
3. Iterate from the current index minus one to the first index of the array 
4. Compare the current unsorted element with the current element in the sorted array 
5. If the unsorted element is greater than the sorted element, swap them 
6. If sorted element is less than the unsorted, break the nested loop (the unsorted element is in the right place)

Time Complexity: O(n<sup>2</sup>)<br>
Space Complexity: O(1)

---

### Tim Sort:
---

Algorithm Steps: 

1. Calculate the minimum run size 
2. Split the array into sub-arrays with sizes equal to the run size
3. Perform insertion sort on each of these sub arrays
4. Merge the sub-arrays using the same method as the merge sort 
5. Repeatedly merge the sub-arrays until only one sorted array is lefy

Time Complexity: O(n log n)<br>
Space Complexity: O(n) 

#### A note on the Space Complexity 

An O(1) space complexity can be achieved by merging the sub arrays in-place. 

#### Calculating run size 

Tim sort calculated the run size between the rangge of 32 - 64 (inclusive). <br>
For arrays that are smaller than 64, the algorithm just performs an insersion sort on the whole array. <br>
The process Tim Sort uses to calculate the run size can be found [here.](https://en.wikipedia.org/wiki/Timsort)

--- 

### Cocktail Shaker Sort 

Algorithm steps:

1. Set a variables named swapped to true 
2. While swapped is true do, 
3. Set swapped to false
4. Iterate from the beginning of the array until the end comparing adjacent elements
5. If the element to the left if larger than the element to the right swap them and set swapped to true
6. If swapped is false, halt algorithm 
7. Iterate from the end of the array to the beginning comparing adjacent elements
8. If the element to the left if larger than the element to the right swap them and set swapped to true

Time Complexity: O(n<sup>2</sup>)<br>
Space Complexity: O(1) 

---

Go to [README.md](../README.md)