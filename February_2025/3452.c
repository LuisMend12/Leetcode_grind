int sumOfGoodNumbers(int* nums, int numsSize, int k) {
    int sum = 0;
    for (int i = 0; i<numsSize; i++) {
        bool GoodNum = true;
        if (i-k>=0 && nums[i] <= nums[i-k]) GoodNum = false;
        if (i+k<numsSize && nums[i] <= nums[i+k]) GoodNum = false;
        if (GoodNum) sum += nums[i];
    }

    return sum;
}