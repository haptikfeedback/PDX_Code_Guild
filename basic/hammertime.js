/**
 * Checks the entered time and displays what is currently scheduled
 */
function scheduleCheck(clock){
    if (clock >= 700 && clock <= 900){
        return "It's currently Breakfast time!"
    } else if (clock >= 1200 && clock < 1400){
        return "It's currently Lunch time!"
    } else if (clock >= 1900 && clock < 2100){
        return "It's currently dinner time!"
    } else if (clock >= 2200 && clock < 2400){
        return "It's currently H A M M E R time!!!"
    } else if (clock >= 0 && clock < 400){
        return "It's currently H A M M E R time!!!"
    } else{
        return "Do whatever you wanna do right now... I'm no micromanager"
    }
}

console.log(scheduleCheck(930))