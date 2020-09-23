from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.views import APIView
from api.models import User, Employee
from api.serializers import UserModelSerializer, EmployeeModelSerializer
from utils.response import APIResponse

class UserAPIView(APIView):
    # authentication_classes = []
    # permission_classes = []

    def post(self,request,*args,**kwargs):
        request_data=request.data
        ums=UserModelSerializer(data=request_data, context={"request": request},)
        ums.is_valid(raise_exception=True)
        ums_save=ums.save()
        ums_data=UserModelSerializer(ums_save).data
        return APIResponse(200, True, results=ums_data)

    def get(self,request,*args,**kwargs):
        username=request.query_params.get("username")
        password=request.query_params.get("password")
        uof=User.objects.filter(username=username,password=password).first()
        if uof:
            ums=UserModelSerializer(uof).data
            print(ums)
            return APIResponse(200,True,ums)
        return APIResponse(400,False)


class EmployeeGenericAPIView(ListModelMixin, CreateModelMixin, GenericAPIView,DestroyModelMixin,UpdateModelMixin,RetrieveModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer
    lookup_field = "id"

    def get(self,request,*args,**kwargs):
        if "id" in kwargs:
            self_list = self.retrieve(request, *args, **kwargs)
            return APIResponse(200,True,self_list.data)
        self_list=self.list(request,*args,**kwargs)
        return APIResponse(200,True,self_list.data)

    def post(self,request,*args,**kwargs):
        self_create=self.create(request,*args,**kwargs)
        return APIResponse(200,True,self_create.data)
    def delete(self,request,*args,**kwargs):
        print(request.query_params.get("id"))
        id = request.GET.get('id')
        employee = Employee.objects.filter(id=id)[0].delete()
        return APIResponse(200,True,employee)

    def put(self, request, *args, **kwargs):
        response = self.update(request, *args, **kwargs)
        return APIResponse(results=response.data)
