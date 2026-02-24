class Solution {
public:
    string capitalizeTitle(string title) {
        stringstream ss(title);
        string word, res = "";

        while (ss >> word) {
            for(auto &c : word)
                if (c >= 'A' && c <= 'Z') 
                    c = c + 32;   
            if (word.size() >= 3) {
                    word[0] -= 32; 
            }
            res += word + " ";
        }
        res.pop_back();
        return res;
    }
};