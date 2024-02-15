import json
import pytest
from click.testing import CliRunner
from cli import cli, handle_response  # Assuming handle_response is part of your module

class MockResponse:
    def __init__(self, status_code, content):
        self.status_code = status_code
        self.content = content

    def json(self):
        return json.loads(self.content)

@pytest.fixture
def mock_post(monkeypatch):
    def mock_post_function(url, data, verify):
        if "login" in url:
            return MockResponse(200, '{"user_id": 5, "is_admin": 1, "username": "admin"}')
        elif "title" in url:
            return MockResponse(200, '{"title_id": 929, "title_name": "Test Title"}')
        elif "searchtitle" in url:
            return MockResponse(200, '[{"title_id": 123, "title_name": "Search Result 1"}, {"title_id": 456, "title_name": "Search Result 2"}]')
        elif "bygenre" in url:
            return MockResponse(200, '[{"title_id": 789, "title_name": "Genre Result 1"}, {"title_id": 321, "title_name": "Genre Result 2"}]')
        elif "name" in url:
            return MockResponse(200, '{"name_id": 1, "name_value": "Test Name"}')
        elif "searchname" in url:
            return MockResponse(200, '[{"name_id": 234, "name_value": "Search Name 1"}, {"name_id": 567, "name_value": "Search Name 2"}]')

    monkeypatch.setattr("requests.post", mock_post_function)

def test_handle_response_json():
    response_content = '{"user_id": 1, "is_admin": 0}'
    result = handle_response(MockResponse(200, response_content), 'json')
    assert result == json.loads(response_content)

#def test_handle_response_invalid_format():
#    response_content = '{"user_id": 1, "is_admin": 0}'
#    result = handle_response(MockResponse(200, response_content), 'invalid_format')
#    assert result is None  # Adjust based on your actual handling of invalid format

def test_login(mock_post):
    runner = CliRunner()
    result = runner.invoke(cli, ["login", "--username", "admin", "--password", "0"])
    assert result.exit_code == 0
    assert "{'is_admin': 1, 'user_id': 5, 'username': 'admin'}" in result.output

def test_title(mock_post):
    runner = CliRunner()
    result = runner.invoke(cli, ["title", "--titleID", "929"])
    assert result.exit_code == 0
    assert "929" in result.output

def test_searchtitle(mock_post):
    runner = CliRunner()
    result = runner.invoke(cli, ["searchtitle", "--titlepart", "Air America"])
    assert result.exit_code == 0
    assert "Air America" in result.output

def test_bygenre(mock_post):
    runner = CliRunner()
    result = runner.invoke(cli, ["bygenre", "--genre", "Comedy", "--min", "5.2", "--start", "1990", "--end", "2000"])
    assert result.exit_code == 0

def test_name(mock_post):
    runner = CliRunner()
    result = runner.invoke(cli, ["name", "--nameID", "1"])
    assert result.exit_code == 0
    assert "1" in result.output

def test_searchname(mock_post):
    runner = CliRunner()
    result = runner.invoke(cli, ["searchname", "--namepart", "James"])
    assert result.exit_code == 0
    assert "James" in result.output
