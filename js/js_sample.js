// パラメーターで取得した数値が素数かを調べる関数
function primejudge(num){
  if (num == 1){
    // 素数は2以上なのでパラメーター値が1の時は空文字を返す
    return " ";
  } else if (num == 2) {
    // 2は素数のためパラメーターの値を返す
    return "prime";
  } else {
    // numが3以降の時は、iが(num-1)になるまで処理を繰り返し
    // numが素数であるか調べる
    for (i=2; i<num; i++){
      // numを2の数から順に割っていき、割り切れた場合は
      // iはnumの約数と判定
      if (num % i == 0){
        // numは素数ではないので空文字を返す
        return " ";
      }
      // i+1がパラメーター値と等しい場合
      // つまりnum自身以外には約数がない(1を除く)と判定
      if (i + 1 == num){
        // numは素数のためprimeを返す
        return "prime";
      }
    }
  }
}
// 定数max
const max = 100;

// 定数maxの数だけ繰り返す
for(let i = 1; i < max; i++){
  // カウンター変数iを引数にしてprimejudge()を実行
  // 関数の戻り値をコンソールに出力する
  console.log(i + ": " + primejudge(i));
}