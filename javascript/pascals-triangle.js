const pascalTriangleRecursive = (n, arr) => {
    if (!arr) arr = [[1]]
    if (n < 2) return arr
    
    const prevLine = arr[arr.length - 1]
    const newLine = [1]
    
    prevLine.forEach((item, index) => {
        if (index === 0) return
        if (index === prevLine.length) return
        newLine.push(prevLine[index] + prevLine[index - 1])
    })
    
    newLine.push(1)
    arr.push(newLine)
    
    return pascalTriangleRecursive(n - 1, arr)
}

console.log(pascalTriangleRecursive(9));