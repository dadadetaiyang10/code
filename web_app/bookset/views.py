from django.http import JsonResponse
from django.views import View
from bookset.models import HeroInfo


class HeroInfomation(View):
    def get(self, request):
        """接口1：获取所有的英雄人物数据"""
        try:
            # 判断数据库是否连接
            heros = HeroInfo.objects.all()  # 返回对象是QuerySet查询集
        except Exception as e:
            print("异常报错：", e)
        else:
            if heros:
                hero_list = []
                for hero in heros:
                    hero_data = {
                        "id": hero.id,
                        "hname": hero.hname,
                        "hgender": hero.hgender,
                        "hcomment": hero.hcomment,
                        "hbook": hero.hbook.btitle,
                        "hbook_id": hero.hbook_id
                    }
                    hero_list.append(hero_data)
                return JsonResponse({"code": 0,
                                     "message": "OK",
                                     "heros": hero_list})
            else:
                return JsonResponse({"message": "查询不到英雄数据，检查数据库"})

    def post(self, request):
        """接口2：新增一个英雄人物数据"""
        # 1.将json数据转换为dict字典
        import json
        request_dict = json.loads(request.body)
        # 2.从字典里取值
        hname = request_dict.get("hname")
        hgender = request_dict.get("hgender")
        hcomment = request_dict.get("hcomment")
        hbook_id = request_dict.get("hbook_id")

        if hname != "" and hbook_id != "":
            try:
                # 3.create方法返回一个HeroInfo模型对象
                hero_obj = HeroInfo.objects.create(hname=hname,
                                                   hgender=hgender,
                                                   hcomment=hcomment,
                                                   hbook_id=hbook_id)
            except Exception as e:
                print("异常报错：", e)
                return JsonResponse({"code": 1, "message": "模型对象创建错误"})
            else:
                # 5.组织返回json数据
                data = {
                    "code": 0,
                    "message": "OK",
                    "hero": {
                        "id": hero_obj.id,
                        "hname": hero_obj.hname,
                        "hgender": hero_obj.hgender,
                        "hcomment": hero_obj.hcomment,
                        "hbook": hero_obj.hbook.btitle,
                        "hbook_id": hero_obj.hbook_id
                    }
                }
                return JsonResponse(data)
        else:
            return JsonResponse({"code": 1, "message": "传入参数不能为空"})
