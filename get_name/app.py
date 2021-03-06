from flask import Flask, render_template, request, redirect, url_for
import numpy as np

# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__)

# Messageをランダムに表示するメソッド
def picked_up():
  messages = [
      "こんにちは、あなたの名前を入力してください",
      "やあ！お名前は何ですか？",
      "あなたの名前を教えてね"
  ]
  # NumPy の random.choice で配列からランダムに取り出す
  return np.random.choice(messages)

  
# ここからウェブアプリケーション用のルーティングを記述
# index にアクセスしたときの処理
@app.route('/')
def index():
  title = "ようこそ"
  message = picked_up()
  # index.html をレンダリングする
  return render_template('index.html',
                        message=message, title=title)

# /post にアクセスしたときの処理
@app.route('/post', methods=['GET', 'POST'])
def post():
  title = "こんにちは"
  if request.method == 'POST':
    # リクエストフォームから「名前」を取得して
    name = request.form['name']
    # index.htmlをレンダリングする
    return render_template('index.html',
                          name=name, title=title)
  else:
    # エラーなどでリダイレクトしたい場合はこんな感じ
    return redirect(url_for('index'))
  
app.debug = True # デバッグモード有効化
app.run(host='127.0.0.1') # どこからでもアクセス可能  