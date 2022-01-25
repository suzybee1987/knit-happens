from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    weight = None
    if 'product_size' or 'product_weight' in request.POST:
        if 'product_size' in request.POST:
            size = request.POST.get('product_size', False)
        else:
            weight = request.POST.get('product_weight', False)

    bag = request.session.get('bag', {})

    if size or weight:
        if size:
            if item_id in list(bag.keys()):
                if size in bag[item_id]['items_by_size'].keys():
                    bag[item_id]['items_by_size'][size] += quantity
                    messages.success(
                        request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
                else:
                    bag[item_id]['items_by_size'][size] = quantity
                    messages.success(
                        request, f'Added size {size.upper()} {product.name} to your bag')
            else:
                bag[item_id] = {'items_by_size': {size: quantity}}
                messages.success(
                    request, f'Added size {size.upper()} {product.name} to your bag')
        else:
            if item_id in list(bag.keys()):
                if weight in bag[item_id]['items_by_weight'].keys():
                    bag[item_id]['items_by_weight'][weight] += quantity
                    messages.success(
                        request, f'Updated weight {weight.capitalize()} {product.name} quantity to {bag[item_id]["items_by_weight"][weight]}')
                else:
                    bag[item_id]['items_by_weight'][weight] = quantity
                    messages.success(
                        request, f'Added {weight.capitalize()} {product.name} to your bag')
            else:
                bag[item_id] = {'items_by_weight': {weight: quantity}}
                messages.success(
                    request, f'Added {weight.capitalize()} {product.name} to your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    weight = None
    if 'product_size' or 'product_weight' in request.POST:
        if 'product_size' in request.POST:
            size = request.POST.get('product_size', False)
        else:
            weight = request.POST.get('product_weight', False)

    bag = request.session.get('bag', {})
    if size or weight:
        if size:
            if quantity > 0:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request, f'Updated {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
            else:
                del bag[item_id]['items_by_size'][size]
                if not bag[item_id]['items_by_size']:
                    bag.pop(item_id)
                messages.success(
                    request, f'Removed {size.upper()} {product.name} from your bag')
        else:
            if quantity > 0:
                bag[item_id]['items_by_weight'][weight] = quantity
                messages.success(
                    request, f'Updated {weight.capitalize()} {product.name} quantity to {bag[item_id]["items_by_weight"][weight]}')
            else:
                del bag[item_id]['items_by_weight'][weight]
                if not bag[item_id]['items_by_weight']:
                    bag.pop(item_id)
                messages.success(
                    request, f'Removed {weight.capitalize()} {product.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        weight = None

        if 'product_size' or 'product_weight' in request.POST:
            if 'product_size' in request.POST:
                size = request.POST.get('product_size', False)
            else:
                weight = request.POST.get('product_weight', False)

        bag = request.session.get('bag', {})
        if size or weight:
            if size:
                del bag[item_id]['items_by_size'][size]
                if not bag[item_id]['items_by_size']:
                    bag.pop(item_id)
                messages.success(
                    request, f'Removed {size.upper()} {product.name} from your bag')
            else:
                del bag[item_id]['items_by_weight'][weight]
                if not bag[item_id]['items_by_weight']:
                    bag.pop(item_id)
                messages.success(
                    request, f'Removed {weight.capitalize()} {product.name} from your bag')

        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
