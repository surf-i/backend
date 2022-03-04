from ..models import Website
from ..models import Categoria
def get_websites():
    websites = Website.objects.all()
    return websites

def get_websites_by_name(ws_pk):
    websites = Website.objects.filter(nombre=ws_pk)
    return websites

def get_websites_by_url(ws_pk):
    websites = Website.objects.filter(url=ws_pk)
    return websites

"""def update_website(ws_pk, new_ws):
    website = get_website(ws_pk)
    website.nombre = new_ws["nombre"]
    website.save()
    return website"""

def create_website(ws):
    categorias = Categoria.objects.get(pk=ws["categorias"])
    website = Website(nombre=ws["nombre"], url=ws["url"], calificacionPromedio=ws["calificacionPromedio"], categorias=categorias)
    website.save()
    return website