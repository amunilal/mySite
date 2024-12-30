from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from . models import Product, Review, ReviewForm


def index(request):
    """Index View"""
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "index.html", context)


def detail(request, product_id):
    """
    Display the details of a specific product along with its associated reviews,
    and allow users to submit reviews for the product.

    :param request:
        The HTTP request object containing metadata about the request
        (e.g., method, user, POST data).
    :type request: HttpRequest
    :param product_id:
        The ID of the product to retrieve and display.
    :type product_id: int

    :returns:
        Renders the `detail.html` template with the product details,
        associated reviews, and the review form. If a valid review is submitted,
        redirects back to the same page with the `#reviews` anchor.
    :rtype: HttpResponse
    """
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(
        product_id=product_id).order_by("-id")

    # If the form is submitted we check if the inputs are valid then
    # proceed to allow the user to login, otherwise present them with
    # the registration form.
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.instance.user_name = request.user.first_name
            review_form.instance.product = product
            review_form.save()
            return HttpResponseRedirect(
                request.path_info + "#reviews"
            )
    else:
        review_form = ReviewForm()

    context = {"product": product, "reviews": reviews,
               "review_form": review_form}
    return render(request, "detail.html", context)


def about(request):
    """About View"""
    return render(request, "about.html")
