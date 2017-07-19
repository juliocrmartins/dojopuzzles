from django.http import HttpResponse


def problems(request):
    return HttpResponse('List all problems')


def problems_published(request):
    return HttpResponse('List all published problems')


def problems_detail(request, slug):
    return HttpResponse(
        'Details of problem with slug {0}'.format(slug))


def problems_random(request):
    return HttpResponse(
        'Redirects to a random problem')


def problems_choose(request, slug):
    return HttpResponse(
        'Choose problem with slug {0}'.format(slug))
