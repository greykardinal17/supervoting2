# tests/test_webapp.py
from pythonProject1.archive.webapp import get_title

def test_get_title_ok(mocker):
    # Патчим "там, где используется": webapp.requests.get
    mock_get = mocker.patch("pythonProject1.webapp.requests.get")

    # Настраиваем фейковый ответ
    mock_resp = mocker.Mock()
    mock_resp.raise_for_status.return_value = None
    mock_resp.json.return_value = {"title": "Hello"}
    mock_get.return_value = mock_resp

    # Проверяем поведение
    assert get_title("https://example.com/api") == "Hello"
    mock_get.assert_called_once_with("https://example.com/api", timeout=1)
    mock_resp.raise_for_status.assert_called_once()