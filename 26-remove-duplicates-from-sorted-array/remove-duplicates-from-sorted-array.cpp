class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int l = 1; // Pointer for the position of unique elements
        
        for (int r = 1; r < nums.size(); ++r) { // Iterate through the array
            if (nums[r] != nums[r - 1]) { // Check if the current number is different from the previous
                nums[l] = nums[r]; // Update the value at index l with nums[r]
                l++; // Increment the unique elements pointer
            }
        }
        
        return l; // Return the number of unique elements
    }
};
