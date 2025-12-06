from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Post, Comment, Tag
from .forms import UserRegistrationForm, UserProfileForm, PostForm, CommentForm


# Authentication Views
class RegisterView(CreateView):
    """View for user registration."""
    form_class = UserRegistrationForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')


class ProfileView(LoginRequiredMixin, UpdateView):
    """View for user profile management."""
    model = User
    form_class = UserProfileForm
    template_name = 'blog/profile.html'
    success_url = reverse_lazy('blog_home')

    def get_object(self):
        return self.request.user


# Blog Post Views
class PostListView(ListView):
    """View for listing all blog posts with search, filtering, and ordering."""
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = Post.objects.all()
        query = self.request.GET.get('q')
        tag = self.request.GET.get('tag')

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(content__icontains=query) | Q(tags__name__icontains=query)
            ).distinct()
        if tag:
            queryset = queryset.filter(tags__name=tag)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['search_query'] = self.request.GET.get('q', '')
        context['selected_tag'] = self.request.GET.get('tag', '')
        return context


class PostDetailView(DetailView):
    """View for displaying a single blog post with comments."""
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['comment_form'] = CommentForm()
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    """View for creating a new blog post."""
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog_home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """View for editing a blog post."""
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog_home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """View for deleting a blog post."""
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog_home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# Comment Views
@login_required
def add_comment(request, post_id):
    """View for adding a comment to a post."""
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post_id)
    return redirect('post_detail', pk=post_id)


@login_required
def edit_comment(request, comment_id):
    """View for editing a comment."""
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        return redirect('post_detail', pk=comment.post.id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=comment.post.id)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'blog/comment_form.html', {'form': form, 'comment': comment})


@login_required
def delete_comment(request, comment_id):
    """View for deleting a comment."""
    comment = get_object_or_404(Comment, pk=comment_id)
    post_id = comment.post.id
    if request.user == comment.author:
        comment.delete()
    return redirect('post_detail', pk=post_id)


# Comment Class-Based Views
class CommentCreateView(LoginRequiredMixin, CreateView):
    """View for creating a comment."""
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['post_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.id})


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """View for updating a comment."""
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.id})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """View for deleting a comment."""
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.id})


# Tag Views
class TagPostListView(ListView):
    """View for listing posts by tag."""
    model = Post
    template_name = 'blog/tag_posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, name=self.kwargs['tag_name'])
        return Post.objects.filter(tags=self.tag)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context
