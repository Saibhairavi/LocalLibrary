from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance
# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(Genre)
# admin.site.register(BookInstance)

class AuthorAdmin(admin.ModelAdmin):
    list_display=('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


class BookInstanceInline(admin.TabularInline):
    model=BookInstance

# @admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    # Unfortunately we can't directly specify the genre field
    # in list_display because it is a ManyToManyField
    # display_genre function to get the information as a string
    inlines=[BookInstanceInline]
class BookInstanceAdmin(admin.ModelAdmin):
    list_display= ('book','status', 'due_back','imprint')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )



class GenreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(BookInstance,BookInstanceAdmin)
admin.site.register(Genre,GenreAdmin)
