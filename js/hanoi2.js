function hanoi(n, a, b, c) {
  if (n>1) {
    hanoi(n-1,a,c,b);
    tower('1本目','2本目','3本目');
    console.log(`${n}番目の円盤: ${a} -> ${c}`);
    tower('1本目','2本目','3本目');
    hanoi(n-1,b,a,c);
  } else {
    console.log(`${n}番目の円盤: ${a} -> ${c}`);
  }
  
  function tower(x,y,z) {
    
    console.log(`${x}: `);
    console.log(`${y}: `);
    console.log(`${z}: `);
    
  }
}

hanoi(3,'1本目','2本目','3本目');