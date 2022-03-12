/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/roman-to-integer/}
 * @description Given a roman numeral, convert it to an integer.
 */

/**
 * @param {string} s
 * @return {number}
 */
const romanToInt = function (s) {
    const roman_num = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }

    let num = 0;
    const length = s.length;

    for (let index = 0; index < length; index++) {
        if (index + 1 <= length - 1 && roman_num[`${s[index]}${s[index+1]}`]) {
            num += roman_num[`${s[index]}${s[index+1]}`]
            index++
        }else{
            num += roman_num[s[index]]
        }
    }

    return num;
};