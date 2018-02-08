/**
 * 
 */
function palindrome(phrase){
        //This takes the phrase and removes any spaces
        var cleaned = phrase.replace(/\s/g, "");
        console.log(cleaned, " This displays the cleaned phrase.")
        //This takes the phrase and makes a reversed array
        var splitString = cleaned.split("").reverse();
        console.log(splitString)
        //This takes the phrase and compares it to itself
        return splitString.join("") == cleaned
}

console.log(palindrome('solos'))
/**
 * Instructor example of utilizing a for loop to solve the problem
 * with an output to demonstrate what's happening.
 */
// function isPalindrome(phrase) {
//     var string = phrase.replace(/\s/g, '')
//     for(var i = 0; i < string.length; i++) {
//         console.log(string[i], string[(string.length - 1) - i])
//         if(string[i] !== string[(string.length - 1) - i]) {
//             return false;
//         }
//     }
//     return true;
// }

// console.log(isPalindrome('apple'))