/*
Given the string, check if it is a palindrome.

Example

For inputString = "aabaa", the output should be
checkPalindrome(inputString) = true;
For inputString = "abac", the output should be
checkPalindrome(inputString) = false;
For inputString = "a", the output should be
checkPalindrome(inputString) = true.
Input/Output

[execution time limit] 3 seconds (cs)

[input] string inputString

A non-empty string consisting of lowercase characters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 105.

[output] boolean

true if inputString is a palindrome, false otherwise.
*/

bool checkPalindrome(string inputString) {
    int j = inputString.Length -1;
    for(var i = 0; i < inputString.Length -1 ; i++){
        if( i == j){
            return true;
        }
        if(inputString[i] != inputString[j] ){
            return false;
        }
        j--;
    }
    return true;
}
