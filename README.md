# xbrl_analyze_book
This repository contains sample code for analyzing XBRL financial reports.

# リポジトリ説明
このリポジトリは技術同人で使用したサンプルコードを紹介するものです。

サンプルコードに関しては章別でファイルを保存しています。
ご自由にご使用ください。

# 環境
Windows 11

Google Chrome

Python 3.12.3

requests 2.32.3

Arelle-release 2.31.4

beatifulsoup4 4.12.3

pandas 2.2.2

# 7章：大量の由豊を自動でダウンロードする
7章『大量のデータを自動でダウンロードする』では、EDINET APIを利用してEDINETから任意の期間の有価証券報告書を自動ダウンロードする内容となっております。

また、6章ではEDINET APIを使用するまでの過程も説明しております。
良かったらご一読していただけると嬉しいです。
## 対象ファイル
book_code\Chapter_7\download_xbrl.py

# 8章：連結財務諸表から営業利益を自動で取得する
8章『財務諸表から売上高を自動抽出しよう』では、ダウンロードしたXBRLファイルを使用し、その中から連結財務諸表の営業利益（IFRS）を自動で抽出することについてまとめた内容となっております。

1社分の場合と10社分を分けて説明することでステップアップを図っております。
また、コラムではファイルのパスをいちいち指定するのではなく、パスを正規表現を用いて記述することによりディレクトリ内にあるXBRLファイルすべてに処理をかけることについて紹介しています。
## 対象ファイル
1社分を抽出する：book_code\Chapter_8\get_profit_one.py
10社分を抽出する：book_code\Chapter_8\get_profit_ten.py

# 9章：事業等のリスクのテキストデータを自動で取得する
9章『有報からテキストデータを自動抽出しよう』では、テキストデータである「事業等のリスク」という項目を抽出することについてまとめた内容になっております。
## 対象ファイル
book_code\Chapter_9\get_risk_text.py

# 10章：提出者別タクソノミのデータを取得する　～ソニーのコンテンツ価値を取得する～
10章『提出者別タクソノミのデータを取得する　～ソニーのコンテンツ価値を取得する～』では、提出者別タクソノミである「コンテンツ資産」という項目を抽出することについてまとめた内容になっております。

また、抽出したデータをもとにグラフを出力する方法についても紹介しております。
## 対象ファイル
book_code\Chapter_10\get_other_Taxonomy.py

# 11章：自前データベースを持つ
11章『自前データベースを持つ』では、XBRLで取得したデータを自身でデータベース管理することについてまとめた内容になっております。
## 対象ファイル
book_code\Chapter_11\db_operate.py

# 12章：独自のパーサーを作成する
12章『独自のパーサーを作成する』では、XBRLを読み込み情報抽出を行うパーサーを自作することについてまとめた内容になっております。
## 対象ファイル
パーサーの作成：
    book_code\Chapter_12\xb_parser\parser.py
    book_code\Chapter_12\xb_parser\__init__.py
    book_code\Chapter_12\setup.py
パーサーの使用例：
    book_code\Chapter_12\use_example_parser.py
