impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 {
            return false;
        }

        let mut original = x;
        let mut reversed = 0;

        while original != 0 {
            let digit = original % 10;
            reversed = reversed * 10 + digit;
            original /= 10;
        }

        x == reversed
    }
}
