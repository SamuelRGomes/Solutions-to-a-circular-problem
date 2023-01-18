//k in this case is the step value
function findWinner(n, k) {
  if (n == 1) return 1;
  return ((findWinner(n - 1, k) + k - 1) % n) + 1;
}
let result = findWinner(41, 2);
console.log(result);
