import requests
import sys

#  プロンプトを表示して検索ワードを取得
title = input('何を検索しますか？ >')
#  MediawikiのAPIへアクセスするためのURL
url = 'https://ja.wikipedia.org/w/api.php'

# 検索キーワードにマッチしたページが属するカテゴリ一覧を取得するためのクエリ情報
api_params1 = {
    # 実行するアクションをキーワード検索にする
    'action': 'query',
    # titleに格納された値を検索キーワードにする
    'titles': title,
    # 取得するデータをカテゴリの一覧にする
    'prop': 'categories',
    # 取得するデータの形式をJSONに指定
    'format': 'json'
}
# 検索キーワードにマッチしたページのデータをHTML形式で取得するためのクエリ情報
api_params2 = {
    # 実行するアクションをキーワード検索にする
    'action': 'query',
    # titleに格納された値を検索キーワードにする
    'titles': title,
    # 'prop'の値を'revisions'にするとページのデータを取得できる
    'prop': 'revisions',
    # 'rvprop'の値を'content'にするとページの本文が取得できる
    'rvprop': 'content',
    # 'format'に'xmlfm'を指定するとXMLをHTMLとして取得できる
    'format': 'xmlfm'
}
# APIのURLとカテゴリ一覧を取得するクエリ情報を引数にしてrequestsのget()関数を実行
# get()関数の戻り値にjson()メソッドを適用して、JSON形式のデータとして取得する
categories = requests.get(url,params=api_params1).json()
# 取得したJSONデータの'query'キー以下、'pages'キーの値として
# ページのidをキーとするカテゴリ情報が格納されているので取得してpage_idに格納する
page_id = categories['query']['pages']

if '-1' in page_id:
    # 検索キーワードがヒットしなかった時の処理
    # page_idに'-1'が含まれている場合はヒットするページがない
    # メッセージを表示してプログラムを終了する
    print('該当するページがありません')
    sys.exit()
else:
    # 検索キーワードがヒットした時の処理
    # カテゴリ情報はページidをキーとするデータなので
    # キーのみを取り出してリストに変換する
    id = list(page_id.keys())
    if 'categories' in categories['query']['pages'][id[0]]:
        # 「あいまい検索」対策として'query'→'pages'以下に
        # 'id'キーが存在する場合のみ処理を行う
        # 'categories'キーの値（カテゴリ一覧）を取り出してリストにする
        categories = categories['query']['pages'][id[0]]['categories']
        for t in categories:
            # リストからカテゴリ情報を取り出して出力する
            print(t['title'])
    else:
        # 「あいまい検索」にマッチした時の処理
        # メッセージを表示してプログラムを終了する
        print('保存できるページを検索できませんでした')
        sys.exit()

# ここからヒットしたページを保存するための処理
admit = input('検索結果を保存しますか？（yes） >')
if admit == 'yes':
    # yesが入力された場合
    # ヒットしたページをHTML形式で取得するためのクエリ情報を
    # 第2引数にしてget()関数を実行
    data = requests.get(url, params=api_params2)
    # ファイル名を「検索キーワード.html」として
    # 取得したデータをファイルに書き込む
    with open(title + '.html', 'w', encoding='utf_8') as f:
        f.write(data.text)
else:
    # yesが入力されなかった場合はメッセージを表示してプログラムを終了する
    print('プログラムを終了します')
    sys.exit()
