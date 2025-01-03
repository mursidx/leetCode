/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if (x < 0 || x >= 2147483647) {
        return false;
    }

    let num = 0;
    let y = x;

    while (x > 0) {
        num = num * 10;
        if (num > 2147483647) {
            return false;
        }
        num = num + (x % 10);
        x = Math.floor(x / 10);
    }

    return num === y;
};
