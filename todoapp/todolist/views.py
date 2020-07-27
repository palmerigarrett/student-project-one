from django.shortcuts import render, redirect
from .models import Todo, Category
import logging

logger = logging.getLogger(__name__)

# Create your views here.
 
def index(request): #the index view
    todos = Todo.objects.all() #querying all todos with the object manager
    categories = Category.objects.all() #getting all categories with object manager
    notStarted = Todo.objects.filter(progress="notStarted")
    inProgress = Todo.objects.filter(progress="inProgress")
    completed = Todo.objects.filter(progress="completed")

    for todo in todos:
       todo.dueness_calculator()
       todo.save()
       logger.info(todo)
       logger.info(todo.dueness)

    num_completed = 0
    num_todos = 0

    for todo in completed:
        num_completed += 1

    for todo in todos:
        num_todos += 1

    if(num_todos == 0):
        currentProgress = 0
    else:
        currentProgressPercent = num_completed / num_todos
        currentProgress = int(currentProgressPercent * 100)
        logger.info(currentProgress)

    if (request.method == "POST"): #checking if the request method is a POST
        if ("todoAdd" in request.POST): #checking if there is a request to add a todo
            logger.info(request.POST)
            title = request.POST["description"] #title
            todo_date = str(request.POST["date"]) #date
            category = request.POST["category_select"] #category
            content = title + " -- " + todo_date + " " + category #content
            current_todo = Todo(title=title, content=content, due_date=todo_date, category=Category.objects.get(name=category))
            current_todo.save() #saving the todo
            return redirect("/") #reloading the page
    
        if ("todoDelete" in request.POST): #checking if there is a request to delete a todo
            todo_id = request.POST["todoDelete"]
            current_todo = Todo.objects.get(id=int(todo_id)) # getting todo id
            current_todo.delete() # deleting todo
            return redirect("/") # reloading the page

        if ("startingTodo" in request.POST):
            todo_id = request.POST["startingTodo"]
            current_todo = Todo.objects.get(id=int(todo_id)) # getting todo id
            current_todo.progress = "inProgress"
            current_todo.save()
            return redirect("/") # reloading the page

        if ("didNotStart" in request.POST):
            todo_id = request.POST["didNotStart"]
            current_todo = Todo.objects.get(id=int(todo_id)) # getting todo id
            current_todo.progress = "notStarted"
            current_todo.save()
            return redirect("/") # reloading the page
    
        if ("completed" in request.POST):
            todo_id = request.POST["completed"]
            current_todo = Todo.objects.get(id=int(todo_id)) # getting todo id
            current_todo.progress = "completed"
            current_todo.save()
            return redirect("/") # reloading the page
        
        if ("didNotComplete" in request.POST):
            todo_id = request.POST["didNotComplete"]
            current_todo = Todo.objects.get(id=int(todo_id)) # getting todo id
            current_todo.progress = "inProgress"
            current_todo.save()
            return redirect("/") # reloading the page

        if ("categoryAdd" in request.POST):
            name = request.POST["addCategory"]
            new_cat = Category(name=name)
            new_cat.save()
            return redirect("/") # reloading the page

        if ("categoryDelete" in request.POST):
            cat_id = request.POST["categoryDelete"]
            current_cat = Category.objects.get(id=int(cat_id))
            current_cat.delete()
            return redirect("/") # reloading the page

    return render(request, "index.html", {"todos": todos, 
                                        "categories":categories, 
                                        "notStarted": notStarted,
                                        "inProgress": inProgress,
                                        "completed": completed,
                                        "currentProgress": currentProgress,
                                        })