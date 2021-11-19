# 63. HT: Interview Question

Given two lists, determine if they have at least one item in common. 

e.g. this scenario should return true

| 1 | 3 | 5 |    
| - | - | - |  

| 2 | 4 | 5 |    
| - | - | - |  

e.g. this scenario should return false

| 1 | 3 | 5 |    
| - | - | - |  

| 2 | 4 | 6 |    
| - | - | - |

The code shows 2 approaches of doing this using hash tables and a third approach using hash sets (not covered in this course). The interviewer would want to see the second approach if you are using hash tables as the time complexity is O(n) (side-by-side loops) whereas the first case is O(n<sup>2</sup>) (loop within a loop).

