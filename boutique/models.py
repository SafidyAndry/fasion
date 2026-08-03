from django.db import models


class Produit(models.Model):
    """Représente un article vendu dans la boutique."""

    class Couleur(models.TextChoices):
        NOIR = 'noir', 'Noir'
        BLANC = 'blanc', 'Blanc'
        ROUGE = 'rouge', 'Rouge'
        BLEU = 'bleu', 'Bleu'
        VERT = 'vert', 'Vert'
        ROSE = 'rose', 'Rose'
        BEIGE = 'beige', 'Beige'
        CHOCOLAT = 'chocolat', 'Chocolat'

    class Taille(models.TextChoices):
        XS = 'XS', 'XS'
        S = 'S', 'S'
        M = 'M', 'M'
        L = 'L', 'L'
        XL = 'XL', 'XL'
        XXL = 'XXL', 'XXL'

    nom = models.CharField('nom', max_length=200)
    description = models.TextField('description')
    prix = models.DecimalField('prix', max_digits=10, decimal_places=2)
    image = models.ImageField('image', upload_to='produits/')
    couleurs = models.CharField(
        'couleur', max_length=20, choices=Couleur.choices, default=Couleur.NOIR
    )
    tailles = models.CharField(
        'taille', max_length=5, choices=Taille.choices, default=Taille.M
    )
    date_ajout = models.DateTimeField('date d\'ajout', auto_now_add=True)
    disponible = models.BooleanField('disponible', default=True)

    class Meta:
        verbose_name = 'produit'
        verbose_name_plural = 'produits'
        ordering = ['-date_ajout']

    def __str__(self):
        return f"{self.nom} - {self.prix} Ar"


class ContactMessage(models.Model):
    """Message envoyé par un visiteur via le formulaire de contact."""

    nom = models.CharField('nom', max_length=150)
    email = models.EmailField('email')
    sujet = models.CharField('sujet', max_length=200)
    message = models.TextField('message')
    date_envoi = models.DateTimeField('date d\'envoi', auto_now_add=True)
    lu = models.BooleanField('lu', default=False)

    class Meta:
        verbose_name = 'message de contact'
        verbose_name_plural = 'messages de contact'
        ordering = ['-date_envoi']

    def __str__(self):
        return f"{self.sujet} - {self.nom} ({self.email})"
