from django.http import HttpResponse


def home(request):
    """
    The whole website is one page.

    YIKE.
    """
    return HttpResponse("Hello world!")
