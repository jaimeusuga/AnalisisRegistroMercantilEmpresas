"""Utilidades compartidas para consultar APIs de Socrata."""

import time

import requests


def consultar_api(session, url: str, parametros: dict) -> list:
    """Consulta Socrata con reintentos ante errores HTTP transitorios."""
    for intento in range(5):
        try:
            respuesta = session.get(
                url,
                params=parametros,
                timeout=120
            )
            respuesta.raise_for_status()
            return respuesta.json()

        except (requests.Timeout, requests.ConnectionError):
            if intento == 4:
                raise
            time.sleep(min(2 ** intento, 16))

        except requests.HTTPError as error:
            estado = (
                error.response.status_code
                if error.response is not None
                else None
            )
            if estado not in (429, 500, 502, 503, 504) or intento == 4:
                raise
            time.sleep(min(2 ** intento, 16))

    raise RuntimeError("La consulta a Socrata terminó sin respuesta.")
