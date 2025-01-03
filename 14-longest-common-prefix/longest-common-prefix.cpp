class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string res = "";

        if (strs.empty()) return res;

        for (size_t i = 0; i < strs[0].size(); ++i) {
            for (const string& s : strs) {
                if (i >= s.size() || s[i] != strs[0][i]) {
                    return res;
                }
            }
            res += strs[0][i];
        }

        return res;
    }
};