from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Comment,UserProfileInfo
from .forms import PostForm,CommentForm,SignUpForm,EditProfileForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth .mixins import LoginRequiredMixin
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.core.paginator import Paginator
# Create your views here.
#pk = primary key
class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    #sql_query
    #ordering the posts by publish date
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    #
    # def listing(request):
    #     post_list = Post.objects.all()
    #     paginator = Paginator(post_list, 3) # Show 25 contacts per page
    #     page = request.GET.get('page')
    #     contacts = paginator.get_page(page)
    #     return render(request, 'post_list.html', {'contacts': contacts})


class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    from_class = PostForm
    model = Post
    fields = ('author','title','text')

# class UserProfileView(LoginRequiredMixin,ListView):
#     login_url = '/login/'
#     model = Post
#     paginate_by = 3
#     #sql_query
#     #ordering the posts by publish date
#     def get_queryset(self):
#         return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    from_class = PostForm
    model = Post
    fields = ('author','title','text')

class PostDeleteView(LoginRequiredMixin,DeleteView):
    success_url = reverse_lazy("post_list")
    model = Post

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    #template_name = 'blog/post_draft_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('-created_date')


class UserListView(LoginRequiredMixin,ListView):
    login_url='/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.approve()
    return redirect('post_detail', pk=post_pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)


@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            messages.success(request,("Logged In successfully"))
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            messages.success(request,("Error Logging In - Please Try Again"))
            return redirect('login')
    else:
        return render(request,'registration/login.html',{})

@login_required(login_url='/')
def logout_user(request):
    logout(request)
    # Redirect to a success page.
    messages.success(request,("Logged Out Successfully!"))
    return redirect('/')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request,user)
            messages.success(request,("You have registered successfully"))
            return redirect('/')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request,'registration/register.html',context)

@login_required(login_url='/')
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,("You have edited successfully"))
            return redirect('/')
    else:
        form = EditProfileForm(instance=request.user)
    context = {'form': form}
    return render(request,'registration/edit_profile.html',context)

@login_required(login_url='/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,("You have edited successfully"))
            return redirect('/')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request,'registration/change_password.html',context)

@login_required(login_url='/')
def profile_user(request,username):
     u = User.objects.get(username=username)
     return render(request,'registration/profile.html')

@login_required(login_url='/')
def user_settings(request):
    # if request.method =="POST":

    return render(request,'registration/settings.html',{})
