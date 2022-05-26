exports.palindrome = function(word) {
    if (typeof word != 'string') {
        word = word.toString() }

    let newString = word.toLowerCase()
    newString = newString.replace(/[^a-z0-9]/g, '') //remove special all chars not a-z and 0-9
    const reverse = newString.split("").reverse().join("")

    return reverse === newString

};

console.log(exports.palindrome(434))
