from django.db import models


class Personalise(models.Model):
    product_number = models.CharField(max_length=32, null=False, editable=False)
    background_choices = (
        ('standard', 'standard as sample'),
        ('simplify', 'less elements'),
        ('elaborate', 'more elements + £ 5.00'),
    )
    text_color_choices = (
        ('standard', 'standard as sample'),
        ('golden', 'golden tone'),
        ('silver', 'silverish tone'),
    )
    EXTRA_COST = {
        'standard': 0,
        'simplify': 0,
        'elaborate': 5,
        'golden': 0,
        'silver': 0,
    }
    background = models.CharField(max_length=10, choices=background_choices, default='standard',)
    text_color = models.CharField(max_length=10, choices=text_color_choices, default='standard',)
    text_content = models.TextField(max_length=20, null=False, blank=False,)
    extra_requirements = models.TextField(max_length=255, null=False, blank=True,)
    cost_extra = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.product_number
