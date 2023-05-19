from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from order.models import Order, OrderItem
from order.serializer import OrderSerializer


class MyPagination(PageNumberPagination):
    page_size = 3  # Кількість об'єктів на сторінці
    page_query_param = 'page'


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = MyPagination
    # permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = request.user

        if user.is_superuser:
            orders = Order.objects.all()
        else:
            orders = Order.objects.filter(email=user.email)

        page = self.paginate_queryset(orders)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(orders, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            instance = self.get_object()
            if request.user.is_superuser or request.user.email == instance.email:
                serializer = self.get_serializer(instance)
                return Response(serializer.data)
            else:
                return Response({'message': 'Not found', 'status': '404'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'message': 'Not found', 'status': '404'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        review = self.get_object()
        if review.email == request.user.email or request.user.is_superuser:
            return super(OrderViewSet, self).update(request, *args, **kwargs)
        return Response({'message': 'Not found', 'status': '404'}, status=status.HTTP_404_NOT_FOUND, )

    def destroy(self, request, *args, **kwargs):
        review = self.get_object()
        if review.email == request.user.email or request.user.is_superuser:
            return super(OrderViewSet, self).update(request, *args, **kwargs)
        return Response({'message': 'Not found', 'status': '404'}, status=status.HTTP_404_NOT_FOUND, )
