class Solution {
    public:
        int maximumCandies(vector<int>& candies, long long k) {
            long long left = 0, right = *max(candies.begin(), candies.end());
            int result = 0;


            while (left <= right) {
                long long mid  = left + (right - left) / 2;
                long long children_count = 0;

                for (int pile : candies) children_count += pile/mid;

                if (children_count >= k) {
                    resutl = mid;
                    left = mid + 1;
                } else right = mid - 1;
            }
            return result;
        }
    };