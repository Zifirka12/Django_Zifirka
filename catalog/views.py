from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from catalog.models import Product
from catalog.forms import ProductForm


def home(request):
    return render(request, "home.html")


def contacts(request):
    return render(request, "contacts.html")


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:products_list")


class EditProductView(LoginRequiredMixin, UserPassesTestMixin):
    model = Product
    template_name = 'edit_product.html'
    fields = ['title', 'description']

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user

    def handle_no_permission(self):
        return redirect('product_detail', pk=self.kwargs['pk'])

    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.object.pk})

    def get_form_class(self):
        if self.request.user == self.get_object().owner:
            return self.form_class
        else:
            return None

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
