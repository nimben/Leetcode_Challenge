class Solution {
public:
    bool check(int num) {
        while (num != 0) {
            if (num % 10 == 0)
                return false;
            num = num / 10;
        }
        return true;
    }
    vector<int> getNoZeroIntegers(int n) {
        int i, j;
        for (i = 1; i < n; i++){
                j = n - i;
                if (check(i) && check(j))
                    return {i, j};
        }
        return {};
    }
};