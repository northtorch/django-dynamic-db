from __future__ import annotations

from typing import Any

from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView

from apps.main.factories import CountDataFactory
from apps.main.models import CountData
from apps.master.factories import MasterCountDataDataFactory
from apps.master.models import MasterCountData


class IncrementView(TemplateView):
    template_name = "main/increment.html"

    def get_context_data(self, **kwargs: dict) -> dict[str, Any]:
        context: dict[str, Any] = super().get_context_data(**kwargs)
        count_data, _ = CountData.objects.get_or_create(id=1)
        master_count_data, _ = MasterCountData.objects.get_or_create(id=1)
        context["current_count"] = count_data.count
        context["master_count"] = master_count_data.count
        return context

    def post(self, request: HttpRequest, *args: list, **kwargs: dict) -> HttpResponse:
        target = request.POST.get("target")
        opetype = request.POST.get("opetype")
        obj = None
        if opetype == "factory":
            # factory_boy経由でデータを取得・更新
            if target == "master":
                # マスタ側カウンタを取得
                obj = MasterCountDataDataFactory(id=1)
            else:
                # メイン側カウンタを取得
                obj = CountDataFactory(id=1)
        else:
            # Django経由でデータを取得・更新
            if target == "master":
                # マスタ側カウンタを取得
                obj, _ = MasterCountData.objects.get_or_create(id=1)
            else:
                # メイン側カウンタを取得
                obj, _ = CountData.objects.get_or_create(id=1)
        if obj:
            obj.count += 1
            obj.save()
        return self.get(request=request, *args, **kwargs)
