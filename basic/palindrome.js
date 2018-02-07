/**
 * 
 */
function palindrome(phrase){
    var cleaned = phrase.replace(/\s/g, "");
    var reversed = cleaned.reverse();
    return (cleaned + " " + reversed)
}

console.log(palindrome('te s t'))