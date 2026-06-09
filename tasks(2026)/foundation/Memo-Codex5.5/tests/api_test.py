import sys
import time
from typing import Any

import requests

BASE_URL = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8000"


def assert_ok(response: requests.Response) -> dict[str, Any]:
    try:
        body = response.json()
    except Exception as exc:  # pragma: no cover
        raise AssertionError(f"Response is not JSON: {response.text}") from exc
    if response.status_code >= 400:
        raise AssertionError(f"HTTP {response.status_code}: {body}")
    if body.get("code") != 0:
        raise AssertionError(f"Business error: {body}")
    return body["data"]


def main() -> None:
    print(f"Testing {BASE_URL}")
    for _ in range(20):
        try:
            assert_ok(requests.get(f"{BASE_URL}/api/health", timeout=2))
            break
        except Exception:
            time.sleep(0.3)
    else:
        raise SystemExit("API server is not ready")

    first = assert_ok(requests.post(f"{BASE_URL}/api/todos", json={"title": "学习 FastAPI", "description": "完成作业后端", "tag": "学习"}))
    second = assert_ok(requests.post(f"{BASE_URL}/api/todos", json={"title": "买牛奶", "description": "晚上回家路上", "tag": "生活"}))
    third = assert_ok(requests.post(f"{BASE_URL}/api/todos", json={"title": "紧急修 bug", "description": "验证逻辑删除", "tag": "紧急"}))

    assert first["state"] == "todo"
    assert_ok(requests.patch(f"{BASE_URL}/api/todos/{first['id']}/complete"))
    assert_ok(requests.patch(f"{BASE_URL}/api/todos/{first['id']}/reopen"))
    tagged = assert_ok(requests.patch(f"{BASE_URL}/api/todos/{second['id']}/tag", json={"tag": "生活-采购"}))
    assert tagged["tag"] == "生活-采购"

    all_page = assert_ok(requests.get(f"{BASE_URL}/api/todos", params={"page": 1, "page_size": 10}))
    assert all_page["total"] >= 3
    keyword_page = assert_ok(requests.get(f"{BASE_URL}/api/todos", params={"keyword": "FastAPI", "page": 1, "page_size": 5}))
    assert any(item["id"] == first["id"] for item in keyword_page["items"])
    tag_page = assert_ok(requests.get(f"{BASE_URL}/api/todos", params={"tag": "紧急", "page": 1, "page_size": 5}))
    assert any(item["id"] == third["id"] for item in tag_page["items"])
    by_id = assert_ok(requests.get(f"{BASE_URL}/api/todos/{second['id']}"))
    assert by_id["id"] == second["id"]

    assert_ok(requests.patch(f"{BASE_URL}/api/todos/complete"))
    done_page = assert_ok(requests.get(f"{BASE_URL}/api/todos", params={"state": "done", "page": 1, "page_size": 10}))
    assert done_page["total"] >= 3
    assert_ok(requests.patch(f"{BASE_URL}/api/todos/reopen"))
    todo_page = assert_ok(requests.get(f"{BASE_URL}/api/todos", params={"state": "todo", "page": 1, "page_size": 10}))
    assert todo_page["total"] >= 3

    deleted = assert_ok(requests.delete(f"{BASE_URL}/api/todos/{third['id']}"))
    assert deleted["id"] == third["id"]
    missing = requests.get(f"{BASE_URL}/api/todos/{third['id']}")
    assert missing.status_code == 404
    after_delete = assert_ok(requests.get(f"{BASE_URL}/api/todos", params={"tag": "紧急", "page": 1, "page_size": 5}))
    assert all(item["id"] != third["id"] for item in after_delete["items"])

    assert_ok(requests.delete(f"{BASE_URL}/api/todos", params={"state": "done"}))
    assert_ok(requests.delete(f"{BASE_URL}/api/todos", params={"state": "todo"}))
    print("All API tests passed.")


if __name__ == "__main__":
    main()
