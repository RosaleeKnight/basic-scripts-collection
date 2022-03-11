const fibonacciTR = (n, a = 0, b = 1) => n === 0 ? a : fibonacciTR(n - 1, b, a + b);

console.log(fibonacciTR(1000))