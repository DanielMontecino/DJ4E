from ads.models import Ad
from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView


class AdListView(OwnerListView):
    model = Ad
    # By convention:
    # template_name = "ads/ad_list.html"


class AdDetailView(OwnerDetailView):
    model = Ad


class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ['title', 'text', 'price']


class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'text', 'price']


class AdDeleteView(OwnerDeleteView):
    model = Ad

def owner(request):
       return HttpResponse("Hello, world. 89332a47 is the polls index.")
