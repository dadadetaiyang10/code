from django.http import JsonResponse
from django.views import View
from bookset.models import HeroInfo


class HeroInfomation(View):
    def get(self, request):
        """获取所有英雄的信息"""
        heros = HeroInfo.objects.all()  # 返回对象是QuerySet查询集
        hero_li = []

        for hero in heros:
            hero_data = {
                "id": hero.id,
                "hname": hero.hname,
                "hgender": hero.hgender,
                "hcomment": hero.hcomment,
                "hbook": hero.hbook.btitle,
                "hbook_id": hero.hbook_id
            }
            hero_li.append(hero_data)
        return JsonResponse({"code": "200",
                             "message": "OK",
                             "heros": hero_li})
