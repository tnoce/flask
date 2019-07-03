from flask import Flask, render_template, redirect, request

class ToDoItem: ## class ToDoItemを定義
    ## item_idを変数定義。0に初期化する
    item_id = 0
    
    def __init__(self, title): ## initを定義、titleを引数として受け取る
        self.title = title ## titleをインスタンス化
        self.done = []  ## doneを配列に入れる
        self.item_id = ToDoItem.item_id ## item_idは "class ToDoItem" から取得
        ToDoItem.item_id += 1 ## 数を増やす

class ToDoList: ## class ToDoListを定義
    def __init__(self): ## initを定義、引数は何も渡さない
        self.todolist = [] ## todolist を配列の変数として指定

    def add(self, title): ## 関数addを定義。titleを引数として渡す
        item = ToDoItem(title) ## ToDoItemを呼び出す。itemにはtitleを入れる
        self.todolist.append(item) ## todolistの配列にitemをappendする

    def delete(self, item_id): ## 関数deleteを定義。item_idを引数として渡す
        item = [x for x in self.todolist if x.item_id == item_id] ## 内包表記する(なぜかwa不明ｗ)
        del item[0] ## 

    def update(self, item_id):
        item = [x for x in self.todolist if x.item_id == item_id]
        item[0].done = not item[0].done

    def get_all(self): ## Listを返す
        return self.todolist ## todolist内の配列を戻り値として返す

    def delete_doneitem(self): ## 
        self.todolist = [x for x in self.todolist if not x.done]


app = Flask(__name__)

todolist = ToDoList()

@app.route("/")
def show_todolist():  
  return render_template("showtodo.html", todolist=todolist.get_all())

@app.route("/additem", methods=["GET","POST"])
def add_item():
  title = request.form["title"]
  if not title:
    return redirect("/")

  todolist.add(title)
  return redirect("/")

@app.route("/deleteitem/<int:item_id>")
def delete_todoitem(item_id):
  todolist.delete(item_id)
  return redirect("/")

@app.route("/updatedone/<int:item_id>")
def update_todoitemdone(item_id):
  todolist.update(item_id)
  return redirect("/")

@app.route("/deletealldoneitems")
def delete_alldoneitems():
  todolist.delete_doneitem()
  return redirect("/")

app.debug = True # デバッグモード有効化
app.run(host='0.0.0.0') # どこからでもアクセス可能 