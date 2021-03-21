from django.shortcuts import render, redirect
from.models import User, Book
from django.contrib import messages


# Create your views here.
def index(request):

    if not 'user' in request.session:
        request.session['user'] = ''
    
    user = User.objects.filter(user_id = request.session['user'])
    
    if user:
        return redirect('/books')
    
    else:
        request.session['user'] = ''
    return render (request, 'login.html')

def register(request):
    if request.method == "GET":
        return redirect('/')
    
    errors = User.objects.validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        new_user = User.objects.register(request.POST)
        request.session["user"] = new_user.user_id
        messages.success(request, "You have successfully registered!")
        return redirect ('/books')

def login(request):
    if request.method == "GET":
        return redirect('/')
    
    if not User.objects.authenticate(request.POST['email2'], request.POST['password2']):
        messages.error(request, 'Invalid Email/Password')
        return redirect('/')
    user = User.objects.get(email=request.POST['email2'])
    request.session['user'] = user.user_id
    messages.success(request, "You have successfully logged in!")
    return redirect('/books')

def books(request):
    check = User.objects.filter(user_id = request.session["user"])
    if check:
        context = {"book": Book.objects.all(),
        "user" : User.objects.get(user_id = request.session["user"])}
        return render(request, 'books.html', context)
    else:
        return redirect ('/')

def book_detail(request, id):
    pass
    check = User.objects.filter(user_id = request.session["user"])
    if check:
        c_book = Book.objects.get(id = id)
        context = {"book": Book.objects.get(id = id),
        "user" : check[0],
        "likes" : c_book.user_likes.all()}
        return render(request, 'book_detail.html', context)
    else:
        return redirect ('/')


def process_book(request):
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books')
    else:
        title = request.POST['title']
        first = request.POST['author_first']
        last = request.POST['author_last']
        desc = request.POST['desc']
        c_user = User.objects.get(user_id = request.session["user"])
        Book.objects.create(title = title, author_first_name = first, author_last_name = last, desc = desc, user_uploaded = c_user)
        c_book = Book.objects.get(title = title)
        c_book.user_likes.add(c_user)

    
    messages.success(request, "Book Successfully Added")

    return redirect('/books')

def edit(request, id):
    pass
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books')
    else:
        e_book = Book.objects.get(id = id)
        e_book.title = request.POST['title']
        e_book.author_first_name = request.POST['author_first']
        e_book.author_last_name = request.POST['author_last']
        e_book.desc = request.POST['desc']

        e_book.save()
    
    messages.success(request, "Edit Successfully Saved")

    return redirect(f"/book/{e_book.id}")

def process_like_1(request):
    if request.method == "GET":
        return redirect('/') 
    book = Book.objects.get(id =request.POST['book'])
    user = User.objects.get(user_id = request.session["user"])

    book.user_likes.add(user)
    book.save()
    messages.success(request, "You have successfully favorited book")

    return redirect('/books')

def process_like_2(request):
    if request.method == "GET":
        return redirect('/') 
    book = Book.objects.get(id =request.POST['book'])
    user = User.objects.get(user_id = request.session["user"])

    book.user_likes.add(user)
    messages.success(request, "You have successfully favorited book")

    return redirect(f"book/{book.id}")

def remove_like(request):
    if request.method == "GET":
        return redirect('/') 
    book = Book.objects.get(id =request.POST['book'])
    user = User.objects.get(user_id = request.session["user"])

    book.user_likes.remove(user)
    messages.success(request, "You have successfully unfavorited")

    return redirect(f"book/{book.id}")

def delete(request):
    if request.method == "GET":
        return redirect('/')
    d_book = Book.objects.get(id = request.POST['book'])
    d_book.delete
    messages.success(request, "Book successfully Deleted")
    return redirect('/books')



def logout(request):
    request.session.flush()
    messages.success(request, "You have successfully logged out")

    return redirect("/")

