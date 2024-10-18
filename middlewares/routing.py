from asgiref.sync import iscoroutinefunction
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from dynamic_db_router import in_database


class RoutingByDomainMiddleware(MiddlewareMixin):
    """
    リクエスト受信時にサブドメインに応じてDBスキーマを切り替えるミドルウェア
    """

    def __call__(self, request):
        # Exit out to async mode, if needed
        if iscoroutinefunction(self):
            return self.__acall__(request)
        # アクセス先DB設定名を取得
        db_setting_name = settings.DYNAMIC_DB_ROUTES.get(request.get_host())
        if db_setting_name:
            # アクセス先DBを設定
            with in_database(db_setting_name, write=True):
                response = self.get_response(request)
        else:
            # デフォルトDBを設定
            response = self.get_response(request)
        return response

    async def __acall__(self, request):
        """
        Async version of __call__ that is swapped in when an async request
        is running.
        """
        # アクセス先DB設定名を取得
        db_setting_name = settings.DYNAMIC_DB_ROUTES.get(request.get_host())
        if db_setting_name:
            # アクセス先DBを設定
            with in_database(db_setting_name, write=True):
                response = await self.get_response(request)
        else:
            # デフォルトDBを設定
            response = await self.get_response(request)
        return response
