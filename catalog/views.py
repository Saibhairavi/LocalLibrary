from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Author,Book,BookInstance,Genre
# Create your views here.
from django.views.generic import ListView,DetailView
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('index')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request,"login.html",context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("login")

@login_required
def index(request):
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()

    #to implement session
    num_visits=request.session.get('num_visits',0)
    request.session['num_visits']=num_visits+1


    context={
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits':num_visits,
    }

    return render(request,'index.html',context=context)

class BookListView(ListView):
    model=Book
    
class BookDetailView(DetailView):
    model=Book    
    def book_detail_view(request,pk):
        try:
            book=get_object_or_404(Book,pk=pk)
        except Book.DoesNotExist:
            raise Http404('Book doesnt exists')
        return render(request,'book_detail.html',context={'book':book})

class AuthorListView(ListView):
    model=Author

class AuthorDetailView(DetailView):
    model=Author
    def author_detail_view(request,pk):
        try:
            author=get_object_or_404(Author,pk=pk)
        except Author.DoesNotExist:
            raise Http404('Author doesnt exists')
        return render(request,'author_detail.html',context={'author':author})






