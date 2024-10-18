from django.db import DEFAULT_DB_ALIAS
from dynamic_db_router import DynamicDbRouter


class CustomRouter(DynamicDbRouter):

    # マスタDBにアクセスするアプリケーションのリスト
    route_app_labels = {"master"}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return DEFAULT_DB_ALIAS
        return super().db_for_read(model, **hints)

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return DEFAULT_DB_ALIAS
        return super().db_for_write(model, **hints)
