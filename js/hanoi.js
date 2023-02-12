function hanoi(n, a, b, c) {
  if (n>1) {
    hanoi(n-1,a,c,b);
    console.log(`${n}番目の円盤: ${a} -> ${c}`);
    hanoi(n-1,b,a,c);
  } else {
    console.log(`${n}番目の円盤: ${a} -> ${c}`);
  }
}

hanoi(3, "A", "B", "C");