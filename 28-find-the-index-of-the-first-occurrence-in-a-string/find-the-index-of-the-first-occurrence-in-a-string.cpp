class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle == "") {
            return 0;
        }
        int haystack_len = haystack.length();
        int needle_len = needle.length();
        
        // Ensure haystack is long enough to contain needle
        for (int i = 0; i <= haystack_len - needle_len; i++) {
            if (haystack.substr(i, needle_len) == needle) {
                return i;
            }
        }
        return -1;
    }
};
