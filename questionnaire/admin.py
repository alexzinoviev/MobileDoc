from django.contrib import admin
from .models import Questionnaire

# Register your models here.

@admin.register(Questionnaire)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'category')

#admin.site.register(Questionnaire, QuestionAdmin)



# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     #pass
#     prepopulated_fields = {'slug': ('name',)}
#     list_display = ('name','desc', 'cost', 'active')