# php-python
 
# Features
 
Djangoやflaskを使わずにブラウザからサーバー経由でpythonを起動させ、計算させることができた。
 
# Requirement
 
* php
* python3

# Usage
 
ブラウザで[合計値・平均値・最大値・最小値]を選択し、csvファイルをアップロードする。その後、phpでファイル形式を判別し、
csvファイルであればexec()を用いてlinuxコマンドを実行してpythonでそのscvファイル内の数値を計算。求めた値を出力し、phpのexec()で受け取り
その値をブラウザで表示。最後にuploadしたcsvファイルをunlink()で削除。
 
# Note
 
MAMPを使ってローカルサーバーで実装した時は問題なく動いたが、レンタルサーバーで実行するとphpの「exec()」が禁止されていた。
 
# Author
 
nokyyy

* E-mail

laxinfo11@gmail.com
 
# License

These codes are copyrighted by nokyyy
 
