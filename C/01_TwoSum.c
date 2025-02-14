#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int key;
    int value;
} HashNode;

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {

    HashNode* hashMap = malloc(numsSize * sizeof(HashNode));
    int hashMapSize = 0;
    int diff = 0;

    for (int i = 0; i < numsSize; i++) {
        diff = target - nums[i];

        for (int j = 0; j < hashMapSize; j++) {
            if (hashMap[j].key == diff) {
                int* result = malloc(2 * sizeof(int));
                result[0] = hashMap[j].value;
                result[1] = i;
                *returnSize = 2;
                free(hashMap);
                return result;
            }
        }

        hashMap[hashMapSize].key = nums[i];
        hashMap[hashMapSize].value = i;
        hashMapSize++; 
    }
    * returnSize = 0;
    free(hashMap);
    return NULL;
}

int main() {
    // Test cases
    int nums1[] = {2, 7, 11, 15};
    int target1 = 9;
    int returnSize1;
    int* result1 = twoSum(nums1, 4, target1, &returnSize1);
    if (result1) {
        printf("Test Case 1 Passed: [%d, %d]\n", result1[0], result1[1]);
        free(result1);
    } else {
        printf("Test Case 1 Failed\n");
    }

    int nums2[] = {3, 2, 4};
    int target2 = 6;
    int returnSize2;
    int* result2 = twoSum(nums2, 3, target2, &returnSize2);
    if (result2) {
        printf("Test Case 2 Passed: [%d, %d]\n", result2[0], result2[1]);
        free(result2);
    } else {
        printf("Test Case 2 Failed\n");
    }

    int nums3[] = {3, 3};
    int target3 = 6;
    int returnSize3;
    int* result3 = twoSum(nums3, 2, target3, &returnSize3);
    if (result3) {
        printf("Test Case 3 Passed: [%d, %d]\n", result3[0], result3[1]);
        free(result3);
    } else {
        printf("Test Case 3 Failed\n");
    }

    return 0;
}
