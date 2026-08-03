from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Produit
from .forms import ContactForm


def accueil(request):
    """Page d'accueil : bannière + les 6 derniers produits disponibles."""
    derniers_produits = Produit.objects.filter(disponible=True)[:6]
    return render(request, 'accueil.html', {
        'produits': derniers_produits,
    })


def catalogue(request):
    """Catalogue complet des produits disponibles."""
    produits = Produit.objects.filter(disponible=True)
    return render(request, 'catalogue.html', {
        'produits': produits,
    })


def produit_detail(request, pk):
    """Fiche détaillée d'un produit."""
    produit = get_object_or_404(Produit, pk=pk)
    return render(request, 'produit_detail.html', {
        'produit': produit,
    })


def contact(request):
    """Formulaire de contact avec messages flash de confirmation."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Votre message a bien été envoyé. Nous vous répondrons très vite !"
            )
            return redirect('contact')
        else:
            messages.error(
                request,
                "Une erreur est survenue. Merci de vérifier les champs du formulaire."
            )
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form,
    })
