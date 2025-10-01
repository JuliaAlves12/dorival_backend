from django.contrib import admin
from .models import Livro, Autor, Liv_Aut, Liv_Categ, Nivel_Associacao, Usuario, Emprestimo, Categoria

admin.site.register(Livro),
admin.site.register(Autor),
admin.site.register(Liv_Aut),
admin.site.register(Liv_Categ),
admin.site.register(Nivel_Associacao),
admin.site.register(Usuario),
admin.site.register(Emprestimo),
admin.site.register(Categoria)

# Register your models here.
