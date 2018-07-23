from flask import Flask, request, render_template, redirect
import os

app = Flask(__name__)

todolist = []

@app.route("/")
def show_hi():
    return render_template("todo-contacts.html", todolist=todolist)

@app.route("/add", methods=["POST"])
def add_an_item():
    item = request.form['item']
    todolist.append(item)
    return redirect("/")


@app.route("/edit", methods=["POST", "GET"])
def edit_an_item():
    if request.method=="POST":
        newitem = request.form['item']
        olditem = request.form['olditem']

        index = todolist.index(olditem)
        todolist.remove(olditem)
        todolist.insert(index, newitem)
        
        return redirect("/")
    else:
        item = request.args['item']
        return render_template("todo-edititem.html", item=item)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)