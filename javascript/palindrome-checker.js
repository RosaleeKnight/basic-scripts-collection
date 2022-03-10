function palindrome(string) {
    const original = string.replace(/\s/g,'').toLowerCase();
    const reverse = original.split('').reverse().join('');
    return original === reverse;
}
  
  console.log(palindrome('race car'));

