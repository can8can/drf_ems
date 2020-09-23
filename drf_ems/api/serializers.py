from rest_framework.serializers import ModelSerializer

from api.models import User, Employee
from rest_framework import exceptions


class UserModelSerializer(ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

        extra_kwargs = {
            "username": {
                "required": True,
                "min_length": 2,
                "error_messages": {
                    "required": "用户名不能为空",
                    "min_length": "用户名长度太短了",
                }
            },
            "password": {
                "required": True,
                "min_length": 6,
                "error_messages": {
                    "required": "密码不能为空",
                    "min_length": "密码不能少于6位",
                }
            },
            # "re_pwd": {
            #     "required": True,
            #     "min_length": 6,
            #     "error_messages": {
            #         "required": "重复密码不能为空",
            #         "min_length": "重复密码不能少于6位",
            #     }
            # },
            "real_name": {
                "required": True,
                "min_length": 2,
                "error_messages": {
                    "required": "用户名不能为空",
                    "min_length": "用户名不能少于2位",
                }
            },
        }

    # def validate_username(self, attrs):
    #     user = User.objects.filter(username=attrs).first()
    #
    #     if user:
    #         raise exceptions.ValidationError("用户名已存在")
    #
    #     return attrs


    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        request = self.context.get("request")
        re_pwd = request.data.get("re_pwd")
        # print(password, type(password), "密码校验", re_pwd, type(re_pwd))
        res = User.objects.filter(username=username).first()
        if res:
            raise exceptions.ValidationError("用户名已存在，请重新输入")
        else:
            if password != re_pwd:
                raise exceptions.ValidationError("两次密码不一致，请重新输入")
            print(attrs)
            return attrs

class EmployeeModelSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

        extra_kwargs = {
            "emp_name": {
                'required': True,
                'min_length': 2,
                "error_messages": {
                    'required': '用户名必填',
                    'min_length': '用户长度不够'
                }
            }
        }