class Solution {
    public:
        int maxAbsoluteSum(vector<int>& nums) {
           int maxSum = INT_MIN;
           int sum = 0;
    
           for (int i: nums){
            sum += i;
    
            maxSum = max(sum, maxSum);
    
            if (sum < 0){
                sum = 0;
            }
           }
           int minSum = INT_MIN;
           int s = 0;
            for (int i: nums){
            s += i;
    
            minSum = max(abs(s), minSum);
    
            if (s > 0){
                s = 0;
            }
           } 
           return max(maxSum, minSum);
        }
    };