var INCH = 'inch'
var FEET = 'feet'
var YARD = 'yard'
var MILE = 'mile'
var MILLIMETER = 'millimeter'
var CENTIMETER = 'centimeter'
var METER = 'meter'
var KILOMETER = 'kilometer'

/**
 * Converts inch to ...
 */
function convertInch(to, value){
    if (to === INCH){
        return value * 1
    } else if (to === FEET){
        return value * 0.0833333
    } else if (to === YARD){
        return value * 0.0277778
    } else if (to === MILE){
        return value * 0.0000157828
    } else if (to === KILOMETER){
        return value * 0.0000254
    } else if (to === METER){
        return value * 0.0254
    } else if (to === CENTIMETER){
        return value * 2.54
    } else if (to === MILLIMETER){
        return value * 25.4
    }
}
/***
 *  Convert feet to ...
 */
function convertFeet(to, value){
    if (to === INCH){
        return value * 12
    } else if (to === FEET){
        return value * 1
    } else if (to === YARD){
        return value * 0.0277778
    } else if (to === MILE){
        return value * 0.000189394
    } else if (to === KILOMETER){
        return value * 0.0003048
    } else if (to === METER){
        return value * 0.3048
    } else if (to === CENTIMETER){
        return value * 30.48
    } else if (to === MILLIMETER){
        return value * 304.8
    }
}
/***
 *  Convert yard to ...
 */
function convertYard(to, value){
    if (to === INCH){
        return value * 36
    } else if (to === FEET){
        return value * 3
    } else if (to === YARD){
        return value * 1
    } else if (to === MILE){
        return value * 0.000568181818
    } else if (to === KILOMETER){
        return value * 0.0009144
    } else if (to === METER){
        return value * 0.9144
    } else if (to === CENTIMETER){
        return value * 91.44
    } else if (to === MILLIMETER){
        return value * 914.4
    }
}
/***
 * Convert mile to ...
 */
function convertMile(to, value){
    if (to === INCH){
    return value * 63360
    } else if (to === FEET){
        return value * 5280
    } else if (to === YARD){
        return value * 1760
    } else if (to === MILE){
        return value * 1
    } else if (to === KILOMETER){
        return value * 1.609344
    } else if (to === METER){
        return value * 1609.344
    } else if (to === CENTIMETER){
        return value * 160934.4
    } else if (to === MILLIMETER){
        return value * 1609344
    }
}
/***
 * Convert Millimeter to ...
 */
function convertMillimeter(to, value){
    if (to === INCH){
        return value * 0.0393700787
    } else if (to === FEET){
        return value * 0.0032808399
    } else if (to === YARD){
        return value * 0.0010936133
    } else if (to === MILE){
        return value * 0.00001
    } else if (to === KILOMETER){
        return value * 0.000001
    } else if (to === METER){
        return value * 0.001
    } else if (to === CENTIMETER){
        return value * 0.1
    } else if (to === MILLIMETER){
        return value * 1
    }
}

/***
 *  Convert Centimeter to ...
 */
function convertCentimeter(to, value){
    if (to === INCH){
        return value * 0.393700787
    } else if (to === FEET){
        return value * 0.032808399
    } else if (to === YARD){
        return value * 0.010936133
    } else if (to === MILE){
        return value * 0.00001
    } else if (to === KILOMETER){
        return value * 0.00001
    } else if (to === METER){
        return value * 0.01
    } else if (to === CENTIMETER){
        return value * 1
    } else if (to === MILLIMETER){
        return value * 10
    }
}

/***
 *  Convert Meter to ...
 */
function convertMeter(to, value){
    if (to === INCH){
        return value * 39.3700787
    } else if (to === FEET){
        return value * 3.2808399
    } else if (to === YARD){
        return value * 1.0936133
    } else if (to === MILE){
        return value * 0.000621371192
    } else if (to === KILOMETER){
        return value * 0.001
    } else if (to === METER){
        return value * 1
    } else if (to === CENTIMETER){
        return value * 100
    } else if (to === MILLIMETER){
        return value * 1000
    }
}

/**
 *  Convert Kilometer to ...
 */
function convertKilometer(to, value){
    if (to === INCH){
        return value * 39370.0787
    } else if (to === FEET){
        return value * 3280.8399
    } else if (to === YARD){
        return value * 1093.6133
    } else if (to === MILE){
        return value * 0.621371192
    } else if (to === KILOMETER){
        return value * 1
    } else if (to === METER){
        return value * 1000
    } else if (to === CENTIMETER){
        return value * 100000
    } else if (to === MILLIMETER){
        return value * 1000000
    }
}

/**
 * Generic converter to call specific 'from' functions
 */
function converter(from, to, value){
    if (from === INCH){
        return "Converting " + value + " " + from + " to " + to + "... " + convertInch(to, value) + " " + to + "."
    } else if (from === FEET){
        return "Converting " + value + " " + from + " to " + to + "... " + convertFeet(to, value) + " " + to + "."
    } else if (from === YARD){
        return "Converting " + value + " " + from + " to " + to + "... " + convertYard(to, value) + " " + to + "."
    } else if (from === MILE){
        return "Converting " + value + " " + from + " to " + to + "... " + convertMile(to, value) + " " + to + "."
    } else if (from === MILLIMETER){
        return "Converting " + value + " " + from + " to " + to + "... " + convertMillimeter(to, value) + " " + to + "."
    } else if (from === CENTIMETER){
        return "Converting " + value + " " + from + " to " + to + "... " + convertCentimeter(to, value) + " " + to + "."
    } else if (from === METER){
        return "Converting " + value + " " + from + " to " + to + "... " + convertMeter(to, value) + " " + to + "."
    } else if (from === KILOMETER){
        return "Converting " + value + " " + from + " to " + to + "... " + convertKilometer(to, value) + " " + to + "."
    }
}

console.log(converter(YARD, KILOMETER, 1589))

