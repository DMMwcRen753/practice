n = int(input()) #整数を入力
s = input() #整数と同じ文字数の文字列を入力
t = "" #空の変数t
for c in s: #変数cへ変数sの文字を一つずつ入れるのを繰り返す
    t = t.replace(c,"") + c #変数tの中に変数cの中身と同じ文字があるか調べ、あれば消去し、最後に変数cの中身の一文字を末尾に追加
print(t) #変数tを出力