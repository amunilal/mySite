import datetime
from django.db import models
from django.forms import ModelForm


class Customer(models.Model):
    """Customer profile- TODO"""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Category(models.Model):
    """
    Represents a category for grouping products.

    Attributes:
        name (str): The name of the category, limited to 50 characters.
    """
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        """
        Returns the string representation of the category.

        :returns: The category name.
        :rtype: str
        """
        return self.name


class Product(models.Model):
    """
    Represents a product available in the store.

    Attributes:
        name (str): The name of the product, limited to 50 characters.
        price (Decimal): The price of the product with up to 2 decimal places.
        category (ForeignKey): A reference to the category the product belongs to.
            If the category is deleted, the related products are also deleted (CASCADE).
        description (str): A short description of the product, optional.
        details (str): A detailed description of the product, optional.
        image (ImageField): The primary image of the product. This is required.
        image_hover (ImageField): An optional secondary image that appears on hover.
    """
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(
        max_length=250, default='', blank=True, null=True)
    details = models.TextField(default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
    image_hover = models.ImageField(upload_to='uploads/product/', blank=True)

    def __str__(self) -> str:
        """
        Returns the string representation of the product.

        :returns: The product name.
        :rtype: str
        """
        return self.name


class Review(models.Model):
    """
    Represents a review submitted by a user for a specific product.

    Attributes:
        product (ForeignKey): A reference to the associated product. If the product is deleted,
            all related reviews are also deleted (CASCADE).
        user_name (str): The name of the user who submitted the review.
        date (date): The date when the review was submitted. Defaults to the current date.
        comment (str): The review content or feedback. Limited to 250 characters.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    user_name = models.CharField(max_length=50)
    date = models.DateField(default=datetime.datetime.today)
    comment = models.CharField(
        max_length=250, default='')

    def __str__(self) -> str:
        """
        Returns the string representation of the review.

        :returns: The review comment.
        :rtype: str
        """
        return self.comment


class ReviewForm(ModelForm):
    """Review submission form"""
    class Meta:
        model = Review
        fields = ["comment"]


class Order(models.Model):
    """Order details - TODO"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self) -> Product:
        return self.product
