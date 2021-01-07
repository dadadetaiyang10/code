import json

from django.http import JsonResponse, HttpResponse, Http404
from django.views import View
from rest_framework.response import Response
from booktest.serializers import BookInfoSerializer
from rest_framework.viewsets import ViewSet, GenericViewSet, ReadOnlyModelViewSet, ModelViewSet
from booktest.models import BookInfo
from rest_framework.viewsets import mixins


# API: GET /books/
# API: POST /books/
class BookListView(View):
    """定义图书列表视图"""

    def get(self, request):
        """获取所有图书数据"""
        # 1.查询数据库获取所有图书数据
        books = BookInfo.objects.all()

        # 2.使用json格式返回数据
        books_list = []
        for book in books:
            book_dict = {
                'id': book.id,
                'btitle': book.btitle,
                'bpub_date': book.bpub_date,
                'bread': book.bread,
                'bcomment': book.bcomment
            }
            books_list.append(book_dict)

        # 3.返回数据
        return JsonResponse(books_list, safe=False)

    def post(self, request):
        """新增图书"""
        # 1.获取参数并进行校验
        req_dict = json.loads(request.body)
        btitle = req_dict.get("btitle")
        bpub_date = req_dict.get("bpub_date")

        # 2.创建图书数据并保存到数据库
        book = BookInfo.objects.create(btitle=btitle,
                                       bpub_date=bpub_date)

        # 3.将新增图书的数据通过json进行返回
        book_dict = {
            "id": book.id,
            "btitle": book.btitle,
            "bpub_date": book.bpub_date,
            "bread": book.bread,
            "bcomment": book.bcomment
        }
        return JsonResponse(book_dict, status=201)


# API: GET /books/[int:pk]/
# API: PUT /books/[int:pk]/
# API: DELETE /books/[int:pk]/
class BookDetailView(View):
    """定义类视图实现三个功能"""

    def get(self, request, pk):
        """获取指定图书的数据"""
        # 1.查询数据库获取指定的图书数据
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return JsonResponse({"detail": "not found"}, status=404)

        # 2.将指定图书数据通过json进行返回
        book_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment
        }
        return JsonResponse(book_dict)

    def put(self, request, pk):
        """修改指定图书的数据"""
        # 1.查询数据库获取指定的图书数据
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return JsonResponse({"detail": "not found"}, status=404)

        # 2.获取参数并进行校验
        req_dict = json.loads(request.body)
        btitle = req_dict.get("btitle")
        bpub_date = req_dict.get("bpub_date")

        # 3.修改图书数据并保存到数据库
        book.btitle = btitle
        book.bpub_date = bpub_date
        book.save()

        # 4.组织返回json数据
        book_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment
        }
        return JsonResponse(book_dict)

    def delete(self, request, pk):
        """删除指定图书的数据"""
        # 1.查询数据库获取指定的图书数据
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return JsonResponse({"detail": "not found"}, status=404)

        # 2.删除指定图书数据
        book.delete()

        # 3.返回响应
        return HttpResponse(status=204)


# 1.ViewSet
# GET /books/
# GET /books/(?P<pk>\d+)/
# class BookInfoViewSet(ViewSet):
#     """视图集的基本使用"""
#
#     # 1.获取所有图书数据
#     def list(self, request):
#         books = BookInfo.objects.all()
#         serializer = BookInfoSerializer(books, many=True)
#         return Response(serializer.data)
#
#     # 2.获取指定图书数据
#     def retrieve(self, request, pk):
#         try:
#             book = BookInfo.objects.get(pk=pk)
#         except BookInfo.DoesNotExist:
#             raise Http404
#
#         serializer = BookInfoSerializer(book)
#         return Response(serializer.data)


# 2.GenericViewSet
# class BookInfoViewSet(mixins.ListModelMixin,
#                       mixins.RetrieveModelMixin,
#                       GenericViewSet):
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoSerializer


# 3.ReadOnlyModelViewSet
# class BookInfoViewSet(ReadOnlyModelViewSet):
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoSerializer

# 4.ModelViewSet
# class BookInfoViewSet(ModelViewSet):
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoSerializer
#     # GET /books/ -> list
#     # POST /books/ -> create
#     # GET /books/(?P<pk>\d+)/ -> retrieve
#     # PUT /books/(?P<pk>\d+)/ -> update
#     # DELETE /books/(?P<pk>\d+)/ -> destroy

# 5.视图集中添加额外的 API(即：action处理方法)
class BookInfoViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    # API：GET /books/latest/
    def latest(self, request):
        """获取 ID 最新的一本图书的数据"""
        return Response({"message": "获取id最新的图书数据"})

    # API: PUT /books/(?P<pk>\d+)/read/
    def read(self, request, pk):
        """修改指定图书的阅读量(只修改阅读量)"""
        return Response({"message": "修改指定图书的阅读量"})