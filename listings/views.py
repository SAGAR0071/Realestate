from django.shortcuts import get_object_or_404 , render
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from .models import Listing
from listings.choices import bedroom_choice,price_choice,state_choices



# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator=Paginator(listings,6)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)
    context1 = {
                 'listings': paged_listings
               }
    return render(request, 'listings/listings.html', context1)


def listing(request , listing_id):
     listing=get_object_or_404(Listing, pk=listing_id)
     context={
                  'listing':listing
           }

     return render (request, 'listings/listing.html', context)


def search(request):
    queryset_list= Listing.objects.order_by('-list_date')
    #Keyword
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
              queryset_list = queryset_list.filter(description__icontains=keywords)
     # City
    if 'city' in request.GET:
         city = request.GET['city']
         if  city :
                queryset_list = queryset_list.filter(city__iexact=city)
     # STate
    if 'state' in request.GET:
        state = request.GET['state']
        if state :
            queryset_list = queryset_list.filter(state__iexact = state)
            # Bedroom
    if 'bedrooms' in request.GET:
            bedrooms = request.GET['bedrooms']
            if bedrooms :
                queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
                # Bedroom
    if 'bathroom' in request.GET:
                bathroom = request.GET['bathroom']
                if bathroom:
                    queryset_list = queryset_list.filter(bathrooms__lte=bathroom)

    context =  {
                        'state_choices' : state_choices ,
                        'price_choice' : price_choice ,
                        'bedroom_choice' : bedroom_choice ,
                        'listings': queryset_list,
                         'values': request.GET
                            }
    return render (request , "listings/search.html",context)
