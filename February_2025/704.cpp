using namespace std;
class Solution {
public:
    int search(vector<int>& nums, int target) {
        bool found = binary_search(nums.begin(), nums.end(), target);

        auto it = find(nums.begin(), nums.end(), target);

        int idx = it-nums.begin();

        if (!found) return -1;
        else return idx;

    }
};