function findWinner(n) {
  if (n == 1) return 1;
  let winner;
  let powerOf2;
  for (let i = 0; i < n; i++) {
    if (n == 2 ** i) {
      winner = 1;
      break;
    }
    if (2 ** i < n && n < 2 ** (i + 1)) {
      powerOf2 = 2 ** i;
      winner = (n - powerOf2) * 2 + 1;
      break;
    }
  }
  return winner;
}
let result = findWinner(41);
console.log(result);
