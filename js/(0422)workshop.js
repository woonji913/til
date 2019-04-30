const conCat = (str1, str2) => `${str1}-${str2}`

const checkLongStr = string => {
    if (string.length > 10) {
        return true
    } else {
    return false
    }
}

if (checkLongStr(conCat('Happy', 'Hacking'))) {
    console.log('Long String')
} else {
    console.log('Short String')
}