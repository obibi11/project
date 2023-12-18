from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json

# Функція для імітації отримання даних з бази даних
def get_test_user_data(user_id):
    test_users = {
        1: {'name': 'Аліса', 'age': 25},
        2: {'name': 'Боб', 'age': 30}
    }
    return test_users.get(user_id, None)

# Функція для обробки GET запитів
@require_http_methods(["GET"])
def user_view(request, user_id):
    user_data = get_test_user_data(user_id)
    if user_data:
        return JsonResponse(user_data)
    else:
        return HttpResponse("Користувача не знайдено", status=404)

# Функція для обробки POST запитів
@csrf_exempt
@require_http_methods(["POST"])
def post_view(request):
    try:
        data = json.loads(request.body)
        # Тут можна додати валідацію даних
        if 'name' in data and 'age' in data:
            return JsonResponse({'status': 'success', 'data': data})
        else:
            return HttpResponse('Невалідні дані', status=400)
    except json.JSONDecodeError:
        return HttpResponse('Невалідний JSON', status=400)

# Функція для обробки інших запитів
@csrf_exempt
@require_http_methods(["GET", "POST"])
def my_view(request):
    if request.method == 'GET':
        return HttpResponse("Це відповідь на GET запит")
    elif request.method == 'POST':
        return HttpResponse("Це відповідь на POST запит")
