from rest_framework.pagination import PageNumberPagination

class PageNumberCountPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 20
    page_size = 10