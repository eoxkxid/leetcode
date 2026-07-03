#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int currentMax = nums[0];
        int currentMin = nums[0];
        int answer = nums[0];

        for (int i = 1; i < nums.size(); i++) {
            int x = nums[i];

            int prevMax = currentMax;
            int prevMin = currentMin;

            currentMax = max({x, prevMax * x, prevMin * x});
            currentMin = min({x, prevMax * x, prevMin * x});

            answer = max(answer, currentMax);
        }

        return answer;
    }
};