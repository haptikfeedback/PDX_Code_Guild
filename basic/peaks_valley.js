/**
 * PEAK: Returns the indices of peaks. A peak has a lower number on both the left and the right.
 */
function peak(data){
    var dataArray = data.split("");
    var length = data.length;
    var peaksList = []
    // console.log(dataArray)
    for (var i = 0; i < length; i++){
        // dataArray[i] = parseInt(dataArray[i])
        if ((dataArray[i] > dataArray[i - 1]) && (dataArray[i] > dataArray[i + 1])){
            console.log("Peak")
            console.log(dataArray[i]) //prints the number that the peak
            console.log(i)
            peaksList.push({index: i, type: "Peak"})
        }
    }
    return peaksList
}


/**
 * VALLEY: Returns the indices of valleys. A valley is a number with a higher number on both the left and the right.
 */
function valley(data){
    var dataArray = data.split("");
    var length = data.length;
    var valleyList = []
    for (var i = 0; i < length; i++){
        if ((dataArray[i] < dataArray[i - 1]) && (dataArray[i] < dataArray[i + 1])){
            console.log("Valley")
            console.log(dataArray[i]) //prints the number that the valley
            console.log(i)
            valleyList.push({index: i, type: "Valley"})
        }
    }
    return valleyList
}


/**
 * PEAK_AND_VALLEY: Uses the PEAK and VALLEY functions to compile a single list of the peaks and valleys in order of appearance in the original data.
 */
function peakValley(data){
    var combinedList = peak(data).concat(valley(data))
    return combinedList.sort(function(a, b) {
        return a.index > b.index
    })
}

/**
 * CHOP: Uses the above functions to generate a data structure: a list of lists, each list representing a single "slope" or area from peak to valley (terminally inclusive).
 */


// console.log(peak("12345654343212"))
// console.log(valley("12345654343212"))
console.log(peakValley("12345654343212"))