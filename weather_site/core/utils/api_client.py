from typing import Any, Dict, Optional

import requests

from core.exceptions import ExternalApiError, TokenIsNotValid


class ApiClient:
    """Клиент для работы со сторонними веб-ресурсами."""

    def __init__(self, base_url: str, timeout: Optional[float] = 10.0) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def _make_request(
        self, method: str, endpoint: str, **kwargs: Any
    ) -> Dict[str, Any]:
        """Выполняет запрос к API."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        headers = kwargs.pop("headers", {})
        kwargs["headers"] = headers
        kwargs.setdefault("timeout", self.timeout)

        try:
            response = requests.request(method, url, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            if response.status_code == 403:
                raise TokenIsNotValid(
                    "Указанный токен недействителен."
                ) from http_err
            if response.status_code == 404:
                return {"error": "Not found"}
            raise ExternalApiError(
                f"HTTP ошибка: {response.status_code}, сообщение: {http_err}"
            ) from http_err
        except requests.exceptions.RequestException as req_err:
            raise ExternalApiError(
                f"Ошибка при запросе к API: {req_err}"
            ) from req_err

    def get(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """GET запрос к API."""
        return self._make_request(
            "GET", endpoint, params=params, headers=headers
        )

    def post(
        self,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Any] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """POST запрос к API."""
        return self._make_request(
            "POST", endpoint, data=data, json=json, headers=headers
        )

    def put(
        self,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Any] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """PUT запрос к API."""
        return self._make_request(
            "PUT", endpoint, data=data, json=json, headers=headers
        )

    def delete(
        self,
        endpoint: str,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """DELETE запрос к API."""
        return self._make_request("DELETE", endpoint, headers=headers)
