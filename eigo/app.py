app = Flask(__name__)

# todolist = ToDoList()

@app.route("/")
def show_():  
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