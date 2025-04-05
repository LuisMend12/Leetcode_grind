//this is a solution for this question. However, this is not optimal as it uses recursion.


class Solution {
    public:
        int xorRecur(int i, int sum, vector<int> &arr) {
            if (i == arr.size()) return sum;
    
            int take = xorRecur(i+1, sum^arr[i], arr);
    
            int notake = xorRecur(i+1, sum, arr);
    
            return take + notake;
        }
    
        int xorSum(vector<int> &arr) {
            return xorRecur(0, 0, arr);
        }
    
        int subsetXORSum(vector<int>& nums) {
            return xorSum(nums);
        }
    };