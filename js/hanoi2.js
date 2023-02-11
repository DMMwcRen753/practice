let tower = {};
tower['1本目'] = [5,4,3,2,1];
tower['2本目'] = [];
tower['3本目'] = [];

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
  
  function printStatus(x,y,z) {
    console.log(`${x}: ${tower[x]}`);
    console.log(`${y}: ${tower[y]}`);
    console.log(`${z}: ${tower[z]}`);
    
  }
}

hanoi(5,'1本目','2本目','3本目');