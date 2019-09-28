
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def get_queryset(request):
    if request.user.is_authenticated:
        alleprojekte = allgEingaben.objects.filter(user=request.user).order_by('-edited_date')
        paginator = Paginator(alleprojekte, 16)
        page = request.GET.get('page_side')

        try:
            projekte = paginator.page(page)
        except PageNotAnInteger:
            projekte = paginator.page(1)
        except EmptyPage:
            projekte = paginator.page(paginator.num_pages)


        return {'projekte':projekte,}
    else:
        return allgEingaben.objects.none()
