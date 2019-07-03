#%%
class ToDoItem:
    item_id = 0

    def __init__(self, title):
        self.title = title
        self.done = []
        self.item_id = ToDoItem.item_id
        ToDoItem.item_id += 1

class ToDoList:
    def __init__(self):
        self.todolist = []

    def add(self, title):
        item = ToDoItem(title)
        self.todolist.append(item)

    def delete(self, item_id):
        item = [x for x in self.todolist if x.item_id == item_id]
        del item[0]

    def update(self, item_id):
        item = [x for x in self.todolist if x.item_id == item_id]
        item[0].done = not item[0].done

    def get_all(self):
        return self.todolist

    def delete_doneitem(self):
        self.todolist = [x for x in self.todolist if not x.done]

        


#%%
