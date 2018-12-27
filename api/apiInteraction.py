import requests

base_url = "http://jsonplaceholder.typicode.com/todos"

def get_todos():
    return requests.get(url=base_url)

def create_todo(userId, title, completed):
    data = {'userId': userId,
            'title': title,
            'completed': completed}
    return requests.post(url=base_url, data=data)

def delete_todo(id):
    return requests.delete(base_url + "/" + str(id))


get_todos()
create_todo(userId='15', title='new todo item', completed=False)

todo_to_delete = input("type the id of the todo you would like to delete: ")
delete_todo(todo_to_delete)