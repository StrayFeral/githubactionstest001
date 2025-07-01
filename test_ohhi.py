import pytest

from ohhi import ohhi


class TestOhhi:
    def test_ohhi(self):
        assert ohhi("Whatever") == "Oh hi Whatever"
