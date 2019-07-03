# Flaskのインストール
from flask import Flask, render_template, request, redirect, url_for
# SQLAlchemyインストール
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # 自身のインスタンスを作成
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db' # SQLiteのDBのパスを指定

db = SQLAlchemy(app) # dbと連携？

class ToDo(db.Model): # classToDoを作成
    id = db.Column(db.Integer, primary_key=True) # カラムidを作成、主キーとして設定(True部)
    text = db.Column(db.String(200)) # 文字列を指定、200文字まで
    complete = db.Column(db.Boolean) # 0/1でステータスを判定 0 は問題なし 1 は問題あり

@app.route('/') # ルーティングを記載。'/'でトップを指定
def index(): # 関数 indexを定義
    incomplete = ToDo.query.filter_by(complete=False).all() # ToDo classインスタンスを作成。query.all で一覧を表示
    complete = ToDo.query.filter_by(complete=True).all()
    # render_templateで 'index.html'をレンダリングする。todos=todosでhtmlに 'todos'を引数として渡す
    return render_template('index.html' ,incomplete=incomplete, complete=complete)


@app.route('/add', methods=['POST']) # ルーティングを記載。'/add'で/addのアドレスに'POST'されたときの動きを定義
def add(): # 関数 addを定義
    # ToDo classインスタンスを作成。"request.form['引数名']”でformの入力値を受け取れる↓↓
    # complete=Flaseとは???
    todo = ToDo(text=request.form['todoitem'], complete=False) 
    db.session.add(todo) # SQLAlchemyのクエリでtodoに入ったinput値を管理対象にする
    db.session.commit() # commitすることで、DBに登録される
    return redirect(url_for('index')) # redirectクラスを使い、url_forで指定した'index'='/'のページへリダイレクトさせる

@app.route('/complete/<id>') # ルーティングを記載。'/update'で/updateのアドレスに'POST'されたときの動きを定義
def complete(id): # 関数 updateを定義
    todo = ToDo.query.filter_by(id=int(id)).first()
    todo.complete = True
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)