import requests
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def proxy_view(request, servicio, ruta):
    """
    Recibe cualquier petición a /api/<servicio>/<ruta> y la reenvía
    al microservicio correspondiente, devolviendo su respuesta tal cual.
    """
    base_url = settings.MICROSERVICIOS.get(servicio)

    if not base_url:
        return JsonResponse(
            {"error": f"Servicio '{servicio}' no reconocido. "
                      f"Servicios disponibles: {list(settings.MICROSERVICIOS.keys())}"},
            status=404
        )

    url_destino = f"{base_url}/api/{servicio}/{ruta}"

    headers_reenviados = {
        key: value for key, value in request.headers.items()
        if key.lower() != 'host'
    }
    # Forzamos JSON, sin importar qué pidió el navegador
    headers_reenviados['Accept'] = 'application/json'

    try:
        respuesta = requests.request(
            method=request.method,
            url=url_destino,
            headers=headers_reenviados,
            params=request.GET,
            data=request.body,
            timeout=5,
        )
    except requests.exceptions.ConnectionError:
        return JsonResponse(
            {"error": f"El microservicio '{servicio}' no está disponible en este momento."},
            status=503
        )
    except requests.exceptions.Timeout:
        return JsonResponse(
            {"error": f"El microservicio '{servicio}' tardó demasiado en responder."},
            status=504
        )

    return JsonResponse(
        data=respuesta.json() if respuesta.content else {},
        status=respuesta.status_code,
        safe=False,
    )