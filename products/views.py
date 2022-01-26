from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Rating, Review
from .forms import ProductForm, ReviewForm, RatingForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)
    form = ReviewForm
    reviews = product.reviews.filter(active=True)
    new_review = None
    if request.method == 'POST':
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            new_review = form.save(commit=True)
            new_review.product = product
            new_review.save()
        else:
            form = ReviewForm()

    return render(request, 'products/product_detail.html',
                  {'product': product,
                   'form': form,
                   'reviews': reviews,
                   'new_review': new_review
                   })


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to add product. Please ensure the form is \
                    valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to update product. Please ensure the form is \
                    valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


# Reviews views
@login_required
def add_review(request, product_id):
    """ Add a review of a product """
    product = get_object_or_404(Product, pk=product_id)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.product = product
                review.review_author = request.user
                review.save()
                messages.success(
                    request, 'Successfully added your review!')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(
                    request, 'Failed to add review. Please ensure the form is \
                        valid')
    context = {
        'form': form
    }

    return render(request, context)


@login_required
def edit_review(request, review_id):
    """ Edit a review of a product """
    review = get_object_or_404(Review, pk=review_id)
    product = review.product
    if request.user.is_superuser or review.review_author == request.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                messages.info(request, 'Successfully updated your review')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(
                    request, 'Failed to update your review. Please ensure the \
                    form is valid.')

        else:
            form = ReviewForm(instance=review)
    else:
        messages.error(
            request, "You are not allowed to do that!")

    messages.info(request, f'You are editing the review for {product.name}')

    template = 'products/product_detail.html'

    context = {
        'form': form,
        'review': review,
        'product': product,
        'update': True,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """The view to delete a review from the site"""
    review = get_object_or_404(Review, pk=review_id)
    if request.user.is_superuser or review.review_author == request.user:
        review.delete()
        messages.success(request, 'That review has been deleted!')
        return redirect(reverse('reviews'))

    messages.error(request, 'Sorry, you can not do this.')
    return redirect(reverse('products'))
