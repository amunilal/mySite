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
    """Represents a category of products in the system.

    Attributes:
        name (CharField): The name of the category. Max length: 50.

    Methods:
        __str__: Returns the name of the category as a string.
    """
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        """Returns the name of the category.

        Returns:
            str: The name of the category.

        Example:
            >>> category = Category(name="Decoration")
            >>> str(category)
            'Decoration'
        """
        return self.name


class Product(models.Model):
    """Represents a product in the system.

    Attributes:
        name (CharField): The name of the product. Max length: 50.
        price (DecimalField): The price of the product with up to 6 digits and 2 decimal places. Default: 0.
        category (ForeignKey): A foreign key to the Category model. Default: 1.
        description (CharField): A brief description of the product. Max length: 250. Default: blank.
        details (TextField): Additional details about the product. Default: blank.
        image (ImageField): The main image of the product. Uploaded to 'uploads/product/'.
        image_hover (ImageField): An optional hover image of the product. Uploaded to 'uploads/product/'.

    Methods:
        __str__: Returns the name of the product as a string.
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
        """Returns the name of the product.

       Returns:
           str: The name of the product.

       Example:
           >>> product = Product(name="Lamp")
           >>> str(product)
           'Lamp'
       """
        return self.name


class Review(models.Model):
    """Customer reviews"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    user_name = models.CharField(max_length=50)
    date = models.DateField(default=datetime.datetime.today)
    comment = models.CharField(
        max_length=250, default='')

    def __str__(self) -> str:
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
