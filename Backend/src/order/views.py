from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from order.models import Order, OrderItem
from order.serializer import OrderSerializer, OrderUpdateSerializer


class MyPagination(PageNumberPagination):
    page_size = 3  # Кількість об'єктів на сторінці
    page_query_param = 'page'


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()

    serializer_class = OrderSerializer
    pagination_class = MyPagination
    # permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user

            if user.is_superuser:
                orders = Order.objects.all().order_by('-closed_at')
            else:
                orders = Order.objects.filter(email=user.email).order_by('-closed_at')
        else:
            return Response({"message": "you don`t have any orders yet"})

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
                serializer = OrderUpdateSerializer(instance)
                return Response(serializer.data)
            else:
                return Response({'message': 'Not found', 'status': '404'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'message': 'Not found', 'status': '404'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        order = self.get_object()
        if request.user.is_superuser:
            serializer = OrderUpdateSerializer(order, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.user.email == order.email:
            serializer = self.get_serializer(order, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Not found', 'status': '404'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        review = self.get_object()
        if request.user.is_authenticated:
            if review.email == request.user.email or request.user.is_superuser:
                return super(OrderViewSet, self).destroy(request, *args, **kwargs)
        return Response({'message': 'Not found', 'status': '404'}, status=status.HTTP_404_NOT_FOUND, )
