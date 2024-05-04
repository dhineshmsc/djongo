from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render


# Create your views here.
def paginate_data(request):
    data =[
    {"name": {"2name","3name","Alice"}, "age": 28},
    {"name": "Bob", "age": 35},
    {"name": "Charlie", "age": 42},
    {"name": "David", "age": 29},
    {"name": "Eve", "age": 38},
    {"name": "Frank", "age": 45},
    {"name": "Grace", "age": 33},
    {"name": "Hank", "age": 50}
]


    # Set the number of items per page
    page_size = 2

    # Retrieve the page number from the request's GET parameters
    page_number = request.GET.get('page')
    if not page_number:
        page_number = 1

    paginator = Paginator(data, page_size)

    try:
        current_page = paginator.page(page_number)
    except EmptyPage:
        current_page = paginator.page(1)  # Show the first page if the requested page is out of range

    context = {
        "current_page": current_page
    }

    return render(request, 'index.html', context)

