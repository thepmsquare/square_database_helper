from unittest.mock import patch

from square_database_helper import (
    InsertRowsV0Response,
    GetRowsV0Response,
    EditRowsV0Response,
    DeleteRowsV0Response,
)
from square_database_helper.main import SquareDatabaseHelper


def test_init_sets_base_url_correctly(helper: SquareDatabaseHelper):
    assert helper.global_str_square_database_url_base == "https://127.0.0.1:1234"


@patch("square_database_helper.main.make_request")
def test_make_request_forwards_arguments(
    mock_make_request, helper: SquareDatabaseHelper
):
    expected_result = {"ok": True}
    mock_make_request.return_value = expected_result

    result = helper._make_request(
        method="GET",
        endpoint="health",
        json={"a": 1},
        data={"b": 2},
        params={"q": "x"},
        headers={"Authorization": "token"},
    )

    assert result == expected_result
    mock_make_request.assert_called_once_with(
        method="GET",
        url="https://127.0.0.1:1234",
        endpoint="health",
        json={"a": 1},
        data={"b": 2},
        params={"q": "x"},
        headers={"Authorization": "token"},
        return_type="json",
    )


@patch("square_database_helper.main.make_request")
def test_insert_rows_v0_builds_correct_payload(
    mock_make_request, helper: SquareDatabaseHelper
):
    data = [
        {"id": 1, "name": "alpha"},
        {"id": 2, "name": "beta"},
    ]
    mock_make_request.return_value = {
        "affected_count": 2,
        "main": data,
    }

    result = helper.insert_rows_v0(
        data=data,
        database_name="db_main",
        schema_name="public",
        table_name="users",
        skip_conflicts=True,
        response_as_pydantic=True,
    )

    assert isinstance(result, InsertRowsV0Response)
    assert result.affected_count == 2
    assert result.main == data

    mock_make_request.assert_called_once()
    call_kwargs = mock_make_request.call_args.kwargs

    assert call_kwargs["method"] == "POST"
    assert call_kwargs["url"] == "https://127.0.0.1:1234"
    assert call_kwargs["endpoint"] == "insert_rows/v0"

    payload = call_kwargs["json"]
    assert payload["data"] == data
    assert payload["database_name"] == "db_main"
    assert payload["schema_name"] == "public"
    assert payload["table_name"] == "users"
    assert payload["skip_conflicts"] is True


@patch("square_database_helper.main.make_request")
def test_get_rows_v0_defaults_and_payload(mock_make_request, helper, dummy_filters):
    mock_make_request.return_value = {"main": [], "total_count": 0}

    result = helper.get_rows_v0(
        filters=dummy_filters,
        database_name="db_main",
        schema_name="public",
        table_name="users",
        response_as_pydantic=True,
    )

    assert isinstance(result, GetRowsV0Response)
    assert result.total_count == 0
    assert result.main == []

    mock_make_request.assert_called_once()
    call_kwargs = mock_make_request.call_args.kwargs

    assert call_kwargs["method"] == "POST"
    assert call_kwargs["endpoint"] == "get_rows/v0"

    payload = call_kwargs["json"]
    assert payload["database_name"] == "db_main"
    assert payload["schema_name"] == "public"
    assert payload["table_name"] == "users"
    assert payload["filters"] == {"some": "filter", "another": 123}
    assert payload["apply_filters"] is True
    assert payload["columns"] is None
    assert payload["order_by"] == []  # default applied
    assert payload["limit"] is None
    assert payload["offset"] == 0  # default applied


@patch("square_database_helper.main.make_request")
def test_get_rows_v0_with_all_arguments(mock_make_request, helper, dummy_filters):
    data = [{"id": 1}]
    mock_make_request.return_value = {"main": data, "total_count": 1}

    result = helper.get_rows_v0(
        filters=dummy_filters,
        database_name="db_main",
        schema_name="public",
        table_name="users",
        apply_filters=False,
        columns=["id", "name"],
        order_by=["id DESC"],
        limit=10,
        offset=5,
        response_as_pydantic=True,
    )

    assert isinstance(result, GetRowsV0Response)
    assert result.total_count == 1
    assert result.main == data
    mock_make_request.assert_called_once()
    payload = mock_make_request.call_args.kwargs["json"]

    assert payload["apply_filters"] is False
    assert payload["columns"] == ["id", "name"]
    assert payload["order_by"] == ["id DESC"]
    assert payload["limit"] == 10
    assert payload["offset"] == 5


@patch("square_database_helper.main.make_request")
def test_edit_rows_v0_builds_correct_payload(mock_make_request, helper, dummy_filters):
    data = {"name": "updated name"}
    mock_make_request.return_value = {"affected_count": 1, "main": [data]}

    result = helper.edit_rows_v0(
        data=data,
        filters=dummy_filters,
        database_name="db_main",
        schema_name="public",
        table_name="users",
        apply_filters=True,
        response_as_pydantic=True,
    )

    assert isinstance(result, EditRowsV0Response)
    assert result.affected_count == 1
    assert result.main == [data]

    mock_make_request.assert_called_once()
    call_kwargs = mock_make_request.call_args.kwargs

    assert call_kwargs["method"] == "PATCH"
    assert call_kwargs["endpoint"] == "edit_rows/v0"

    payload = call_kwargs["json"]
    assert payload["data"] == data
    assert payload["filters"] == {"some": "filter", "another": 123}
    assert payload["database_name"] == "db_main"
    assert payload["schema_name"] == "public"
    assert payload["table_name"] == "users"
    assert payload["apply_filters"] is True


@patch("square_database_helper.main.make_request")
def test_delete_rows_v0_builds_correct_payload(
    mock_make_request, helper, dummy_filters
):
    data = [{"id": 1}]
    mock_make_request.return_value = {"affected_count": 1, "main": data}

    result = helper.delete_rows_v0(
        filters=dummy_filters,
        database_name="db_main",
        schema_name="public",
        table_name="users",
        apply_filters=False,
        response_as_pydantic=True,
    )

    assert isinstance(result, DeleteRowsV0Response)
    assert result.affected_count == 1
    assert result.main == data

    mock_make_request.assert_called_once()
    call_kwargs = mock_make_request.call_args.kwargs

    assert call_kwargs["method"] == "POST"
    assert call_kwargs["endpoint"] == "delete_rows/v0"

    payload = call_kwargs["json"]
    assert payload["filters"] == {"some": "filter", "another": 123}
    assert payload["database_name"] == "db_main"
    assert payload["schema_name"] == "public"
    assert payload["table_name"] == "users"
    assert payload["apply_filters"] is False
