from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import state_choices, bedroom_choices, price_choices
from .models import listing


def listings(request):
    # listings = listing.objects.all()
    listings = listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    return render(request, 'listings/index.html', {'listings':paged_listings})

def _listing(request, listing_id):
    listing_ = get_object_or_404(listing, pk = listing_id)
    context = {
        'listing' : listing_
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    # listingsQuery = listing.objects.all().order_by('-list_date')
    queryset_list = listing.objects.order_by('-list_date').filter(is_published=True)


    # GET Incoming Information
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__iexact=price)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__iexact=bedrooms)


    context={
        'prices' : price_choices,
        'bedrooms' : bedroom_choices,
        'states' : state_choices,
        'listings' : queryset_list,
        'values' : request.GET
    }
    return render(request, 'listings/search.html', context)
