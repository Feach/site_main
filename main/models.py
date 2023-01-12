from  ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50)
    parent = TreeForeignKey(
        'self',
        related_name="children",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
        )

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='articles/')
    text = RichTextField()
    mini_text = RichTextField(max_length=150)
    price = models.IntegerField()
    category = models.ForeignKey(
        Category,
        related_name="product",
        on_delete=models.SET_NULL,
        null=True
    )
    tag = models.ManyToManyField(Tag, related_name="product")
    create_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, default='')

    def __str__(self):
        return self.title

    def get_absolut_url(self):
        return reverse("product_single", kwargs={"slug": self.category.slug, "product_slug": self.slug})


class Reviews(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name









