//円盤の数を指定する
let n = Number(prompt("円盤の数を入力してください"));

// 三本の塔を作成し、それぞれの塔をリスト配列にする
let tower = {};
tower['1本目'] = [];
tower['2本目'] = [];
tower['3本目'] = [];

// 最初に指定した数まで円盤を作成し、1本目の塔へ大きいものから入れていく
for (var i=n;i>=1;i--){
  tower['1本目'].push(i);
}

// ハノイの塔を計算していく
function hanoi(n, a, b, c) {
  if (n>1) {
    hanoi(n-1,a,c,b);
    console.log(`${n}番目の円盤: ${a} -> ${c}`);
    tower[c].push(tower[a].pop());
    printStatus('1本目','2本目','3本目');
    hanoi(n-1,b,a,c);
  } else {
    console.log(`${n}番目の円盤: ${a} -> ${c}`);
    tower[c].push(tower[a].pop());
    printStatus('1本目','2本目','3本目');
  }
  
  // 3本の塔に重なっている円盤の状態をコンソール上に出力
  function printStatus(x,y,z) {
    console.log(`${x}: ${tower[x]}`);
    console.log(`${y}: ${tower[y]}`);
    console.log(`${z}: ${tower[z]}`);
  }
}

hanoi(n,'1本目','2本目','3本目');