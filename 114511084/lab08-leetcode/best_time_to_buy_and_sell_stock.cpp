#include <vector>
using namespace std;

// LeetCode #121 Best Time to Buy and Sell Stock
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minPrice = prices[0];
        int max = 0;
        for(int i=1;i<prices.size();i++){
            if(prices[i]-minPrice>max) max=prices[i]-minPrice;
            if(prices[i]<minPrice) minPrice=prices[i];
        }
        return max;
    }
};
