function hanoi(n, a, b, c) {
  if(n<1) return;
  console.log(`${a}の棒: ${n}番目の円盤`);
  hanoi(n-1,a,c,b);
  console.log(`${n}番目の円盤: ${a} -> ${c}`);
  console.log(`${c}の棒: 一番上は${n}番目の円盤`);
  hanoi(n-1,b,a,c);
}

hanoi(3, 'A', 'B', 'C');