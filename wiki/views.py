from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail
from .forms import ContactForm, CommentForm, PostForm

from .models import Category, Post


def index(request):
    """
    View for the main page of the site.
    """
    category_list = Category.objects.all()
    context = {
        'category_list': category_list
    }
    return render(request, 'index.html', context)

@login_required
def create_post(request):
    """
    View to create a post.
    """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            form.save_m2m()
            return HttpResponseRedirect('/')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


def edit_post(request, post_slug):
    """
    View to edit a post that has been already created.
    """
    post = get_object_or_404(Post, slug=post_slug)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/{post.category.slug}/{post.slug}/')
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})


def delete_post(request, post_slug):
    """
    View to delete a post that has already been created.
    """
    post = get_object_or_404(Post, slug=post_slug)
    postCategory = post.category.slug  # Access the 'slug' attribute of the category
    post.delete()
    return HttpResponseRedirect(reverse('wiki:post_page', args=[postCategory]))


class CategoryList(generic.ListView):
    """
    In this page we show a list with all the categories contained in the wiki.
    """
    model = Category
    template_name = "category_list.html"
    context_object_name = "category_list"

    def get_queryset(self):
        return Category.objects.all()


def post_list_view(request, category_slug):
    """
    View for the list of posts inside a certain category.
    """
    category = get_object_or_404(Category, slug=category_slug)
    post_list = Post.objects.filter(category=category)

    context = {
        "category": category,
        "post_list": post_list,
    }
    return render(request, "post_list.html", context)


class PostDetail(generic.DetailView):
    """
    Detail view of a single post.
    """
    model = Post

    def get(self, request, queryset=None, *args, **kwargs):
        """
        Override get_object function inside DetailView to get 'category-slug/post-slug url'
        """
        category_slug = self.kwargs.get('category_slug')
        post_slug = self.kwargs.get('post_slug')
        post = get_object_or_404(Post, slug=post_slug, category__slug=category_slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, queryset=None, *args, **kwargs):
        """
        Override get_object function inside DetailView
        to get 'category-slug/post-slug url'
        """
        category_slug = self.kwargs.get('category_slug')
        post_slug = self.kwargs.get('post_slug')
        post = get_object_or_404(Post, slug=post_slug, category__slug=category_slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class PostDetailLike(View):
    """
    View to like or unlike a post from the post detail page.
    """
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('wiki:post_detail', args=[post.category.slug, slug]))


def contact(request):
    """
    Contact form view with validation. When the form is completed, it
    redirects the user to the main page.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            send_mail(subject, message, 'djangorr.1998@gmail.com', [email])
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
