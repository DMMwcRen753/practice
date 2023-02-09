function hanoi(n, a, b, c) {
  if(n<1) return;
  hanoi(n-1,a,c,b);
  console.log(`${n}番目の円盤: ${a}の棒 -> ${c}の棒`);
  // console.log(`${a}の棒: `);
  console.log(`${c}の棒: ${n}番目の円盤`);
  console.log(`${b}の棒: ${n-1}番目の円盤`);
  hanoi(n-1,b,a,c);
}

hanoi(3, '一', '二', '三');