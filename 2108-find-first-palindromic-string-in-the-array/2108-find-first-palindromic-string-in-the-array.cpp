class Solution {
public:
    bool check(string& str) {
        int i = 0, j = str.size() - 1;
        while (i < j) {
            if (str[i++] != str[j--])
                return false;
        }
        return true;
    }

    string firstPalindrome(vector<string>& words) {
        for (auto& str : words) {
            if (check(str))
                return str;
        }
        return "";
    }
};