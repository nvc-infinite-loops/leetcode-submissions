#include <stdlib.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
  int* retArr = (int*) malloc(sizeof(int) * 2);
  
  for (int i = 0; i < numsSize; i++) {
    int nt = target - nums[i];
    *returnSize = 2;
    for (int j = 0; j < numsSize; j++) {
      if ((nums[j] == nt) && j != i) {
        retArr[0] = i;
        retArr[1] = j;
        return retArr;
      }
    }
  }
  return retArr;
}
