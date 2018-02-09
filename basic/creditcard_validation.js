/**
 * Write a function which returns whether a string containing
 * a credit card number is valid as a boolean. 
 * Write as many sub-functions as necessary to solve the problem.
 * Write doctests for each function.
 */
function isCreditcard(numbers){
    // converts the cc number to an array
    var numberArray = numbers.split("");
    console.log(numberArray)
    // removes the last digit on the cc number
    var checkDigit = numberArray.pop(numberArray.length - 1);
    console.log(checkDigit)
    // console.log(numberArray)
    // reverse the cc number
    var reverseArray = numberArray.reverse();
    console.log(reverseArray)
    // doubles every element of the cc number
    var length = reverseArray.length;
    for (var i = 0; i < length; i++){
        reverseArray[i] = parseInt(reverseArray[i])
    }
    console.log(reverseArray)

    for (var i = 0; i < length; i+=2) {
        reverseArray[i] *= 2;
    }
    console.log(reverseArray)
    // subtract nine from numbers over nine
    for (var i = 0; i < length; i++){
        if (reverseArray[i] >= 10){
            reverseArray[i] -= 9;
        }
    }
    console.log(reverseArray)
    // the sum of the cc number
    var sum = reverseArray.reduce( function(total, amount){
        return total + amount
    });
    console.log(sum)
    // remove the second digit of the sum
    var secondDigit = sum.toString().split("")[1];
    console.log(secondDigit)
    return secondDigit == checkDigit

}

console.log(isCreditcard("4556737586899855"))