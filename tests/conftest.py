
import pytest

from square_database_helper.main import SquareDatabaseHelper


class DummyFilters:
    def __init__(self, payload):
        self._payload = payload

    def model_dump(self):
        return self._payload

@pytest.fixture
def dummy_filters():
    return DummyFilters({"some": "filter", "another": 123})

@pytest.fixture
def helper():
    return SquareDatabaseHelper(
        param_int_square_database_port=1234,
        param_str_square_database_ip="127.0.0.1",
        param_str_square_database_protocol="https",
    )
