int maxProfit(int* prices, int pricesSize) {
    int minPrice = prices[0];
    int maxProfit = 0;

    for (int i = 1; i < pricesSize; i++) {
        // 더 싼 가격을 발견하면 매수 가격 갱신
        if (prices[i] < minPrice) {
            minPrice = prices[i];
        }
        // 현재 가격에 팔았을 때의 이익으로 최대 이익 갱신
        else {
            int profit = prices[i] - minPrice;

            if (profit > maxProfit) {
                maxProfit = profit;
            }
        }
    }

    return maxProfit;
}