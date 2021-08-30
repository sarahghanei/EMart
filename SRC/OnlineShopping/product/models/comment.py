# from django.db import models
#
#
# # class Comment(models.Model):
#     class Meta:
#         verbose_name = 'نظر'
#         verbose_name_plural = 'نظرات'
#         ordering = ('date',)
#
#     text = models.TextField('متن', max_length=200)
#     product = models.ForeignKey('product.Product', on_delete=models.CASCADE, related_name='comments')
#     date = models.DateField('تاریخ', auto_now=True, auto_now_add=True)
#     owner = models.CharField('نام', max_length=40)
#     like_numbers = models.PositiveIntegerField()
