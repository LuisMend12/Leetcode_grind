class Solution {
    public:
        int maximumCount(vector<int>& nums) {
            int count_neg = binarySearch(nums, 0);
            int count_pos = nums.size() - binarySearch(nums, 1);
            return max(count_neg, count_pos);
        }
    
    
    private:
    
        int binarySearch(vector<int>& nums, int target) {
            int left = 0, right = nums.size() - 1, result = nums.size();
    
            while (left <= right) {
                int mid = (left+right)/2;
    
                if (nums[mid] < target ) {
                    left = mid + 1;
                } else {
                    result = mid;
                    right = mid - 1;
                }
            }
    
    
            return result;
        }
    };