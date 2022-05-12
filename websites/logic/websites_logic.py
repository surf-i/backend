from ..models import Website, ReviewMetadata, DatosCategoria
from ..models import Categoria
from django.db.models import Max

def get_websites():
    websites = Website.objects.all()
    return websites

def get_websites_by_name(ws_pk):
    websites = Website.objects.filter(nombre=ws_pk)
    return websites

def get_website_by_url(ws_pk):
    try:
        website = Website.objects.get(url=ws_pk)
        return website
    except Website.DoesNotExist:
        return None

def get_multiple_websites_by_urls(urls):
    websites = Website.objects.filter(url__in=urls)
    return websites
    

def create_website(ws):
    categorias = Categoria.objects.get(pk=ws["categorias"])
    website = Website.objects.create(nombre=ws["nombre"], url=ws["url"], calificacionPromedio=ws["calificacionPromedio"], categorias=categorias)
    website.save()
    return website

def get_website_review_metadata(ws_pk):
    try:
        metadata = ReviewMetadata.objects.get(website=ws_pk)
        return metadata
    except ReviewMetadata.DoesNotExist:
        return None

def create_review_metadata(review, website):
    numOpt = 0
    if review["calificacionDiseno"] != None and review["calificacionUsabilidad"] != None:
        numOpt = 1
    metadata = ReviewMetadata.objects.create(website=website, numReviews=1, sumaCalificacion=review["calificacion"], sumaVeracidad=review["gradoVeracidad"], sumaCalificacionDiseno=review["calificacionDiseno"], sumaCalificacionUsabilidad=review["calificacionUsabilidad"], numReviewsOptParams=numOpt)
    metadata.save()
    return metadata

def update_website_metadata(website, metadata, review):
    cat_metadata = get_website_category_metadata(website.id).latest('cantReviews')
    website.calificacionPromedio = metadata.sumaCalificacion / metadata.numReviews
    website.gradoVeracidadPromedio = metadata.sumaVeracidad / metadata.numReviews
    website.categoria = cat_metadata.tipo
    if review["calificacionDiseno"] != None and review["calificacionUsabilidad"] != None:
        website.calificacionDisenoPromedio = metadata.sumaDiseno / metadata.numReviewsOptionalParams
        website.calificacionUsabilidadPromedio = metadata.sumaUsabilidad / metadata.numReviewsOptionalParams
    website.save()
    return website

def get_website_category_metadata(ws_pk):
    cat_metadata = DatosCategoria.objects.filter(website=ws_pk)
    return cat_metadata

def create_category_metadata(review, website):
    cat_metadata = DatosCategoria.objects.create(website=website, tipo=review["categoria"], cantReviews=1)
    cat_metadata.save()
    return cat_metadata