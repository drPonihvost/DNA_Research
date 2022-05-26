import functools
import logging
import traceback

from django.db import transaction
from django.http import JsonResponse, HttpResponseNotFound
from django.views import View

JSON_DUMPS_PARAM = {
    'ensure_ascii': False
}

logger = logging.getLogger('main')


def ret(json_object, status=200):
    """Отдает JSON с правильным HTTP заголовком и в читаемом
    в браузере виде в случае с кириллицей."""
    return JsonResponse(
        json_object,
        status=status,
        safe=not isinstance(json_object, list),
        json_dumps_params=JSON_DUMPS_PARAM
    )


def error_http_response():
    """Возвращает страницу NotFound"""
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def error_response(exception):
    """Подготовка ответа об ошибке"""
    res = {
        'errorMessage': str(exception),
        'traceback': traceback.format_exc()
    }
    logger.error(res)
    return ret(res, status=400)


def error_hadling(fn):
    """Обработка исключений на верхнем уровне"""

    @functools.wraps(fn)
    def inner(request, *args, **kwargs):
        try:
            with transaction.atomic():
                return fn(request, *args, **kwargs)
        except Exception as e:
            print('Ошибка')
            return error_response(e)

    return inner


class ErrorHadling(View):
    """Базовый класс View для обработки исключений"""

    def dispatch(self, request, *args, **kwargs):
        try:
            response = super().dispatch(request, *args, **kwargs)
        except Exception as e:
            print('У ошибки есть атрибут message')
            logger.info(str(e))
            return self._response({'errorMessage': str(e), 'traceback': traceback.format_exc()}, status=400)

        if isinstance(response, (dict, list)):
            return self._response(response)
        else:
            return response

    @staticmethod
    def _response(data, *, status=200):
        return JsonResponse(
            data,
            status=status,
            safe=not isinstance(data, list),
            json_dumps_params=JSON_DUMPS_PARAM
        )
