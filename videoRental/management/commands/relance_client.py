from django.core.management.base import BaseCommand
from videoRental.models import Movie, MovieRent, Customer
from datetime import timedelta, datetime
from django.utils import translation
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

from django.template.loader import render_to_string

class Command(BaseCommand):
    help = "Super Commande "

    def handle(self, *args, **options):
        translation.activate('en')

        date_limit = datetime.now() - timedelta(days=14)
        liste_loc = {}
        locations = MovieRent.objects.filter(return_date=None, checkout_date__lte = date_limit)

        for loc in locations:
           
            d = {
                'username' : loc.customer.user,
                'movie' : loc.movie.title,
            }

            text_content = render_to_string('mails/mail.txt',context=d)
            html_content = render_to_string('mails/mail.html',context=d)
            subject, from_email, to = 'hello', 'from@example.com', loc.customer.user.email  
            
            print (text_content)

            # msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()

            