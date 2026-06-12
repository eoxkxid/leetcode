int maxProfit(int* prices, int pricesSize) {
    int profit = 0;

    for (int i = 1; i < pricesSize; i++) {
        // 전날보다 오늘 가격이 올랐다면 그 차익을 얻는다
        if (prices[i] > prices[i - 1]) {
            profit += prices[i] - prices[i - 1];
        }
    }

    return profit;
}