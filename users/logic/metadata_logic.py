from websites.logic import websites_logic as wl
from websites.models import ReviewMetadata, DatosCategoria
def update_metadata(review, website):
    try:
        metadata = wl.get_website_review_metadata(website.id)
        metadata.numReviews += 1
        metadata.sumaCalificacion += review["calificacion"]
        metadata.sumaVeracidad += review["gradoVeracidad"]
        if review["calificacionDiseno"] != None and review["calificacionDiseno"] != None:
            metadata.sumaDiseno += review["calificacionDiseno"]
            metadata.sumaUsabilidad += review["calificacionUsabilidad"]
            metadata.numReviewsOptionalParams += 1
        metadata.save()
    except ReviewMetadata.DoesNotExist:
        metadata = wl.create_review_metadata(review, website)
    try:
        category_metadata = wl.get_website_category_metadata(website.id)
        if category_metadata:
            category_metadata = category_metadata.get(tipo=review["categoria"])
            category_metadata.cantReviews += 1
            category_metadata.save()
        else:
            category_metadata = wl.create_category_metadata(review, website)
    except DatosCategoria.DoesNotExist:
        category_metadata = wl.create_category_metadata(review, website)
    wl.update_website_metadata(website, metadata, review)
    return metadata