//Leetcode code 

/* 
code challenge 268. Missing Number
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?


Example 1:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.


Example 2:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
*/


var missingNumber = function(nums) {
    finalList=[];
    let sortedNumbers=nums.sort(function(a, b) {
        return a - b;
    });
    for(let i=0; i<=sortedNumbers.length; i++){
       if(sortedNumbers[i]!=i){
         finalList.push(i);
       }
    }
    return finalList[0];
  };

  console.log(missingNumber([9,6,4,2,3,5,7,0,1]));