function compare (a, b) {
    let first = a.split("").sort().join(""),
        second = b.split("").sort().join("");
    console.log(first === second
        ? a + " and " + b + " are anagrams!"
        : a + " and " + b + " are not anagrams."
    );
}

console.log (compare ('asdf', 'qwer'));