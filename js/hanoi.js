let n = prompt('好きな数値を入力してください。');
hanoi(n, '一', '二', '三');

function hanoi(n,a,b,c) {
  if(n<1) return;
  hanoi(n-1,a,c,b);
  console.log(`${n}番目の円盤: ${a}の棒 -> ${c}の棒`);
  status(1,2,3,'1','2','3');
  hanoi(n-1,b,a,c);
}

function status(x,y,z,i,j,k) {
  console.log(`${i}の棒: ${z}番目の円盤`)
  console.log(`${j}の棒: ${y}番目の円盤`)
  console.log(`${k}の棒: ${x}番目の円盤`)
}
