import json
from click.testing import CliRunner
from cli import cli  

def test_login_functional():
    runner = CliRunner()
    result = runner.invoke(
        cli, ["login", "--username", "admin", "--password", "0"]
    )
    assert result.exit_code == 0
    assert "{'is_admin': 1, 'user_id': 5, 'username': 'admin'}" in result.output


def test_title_functional():
    runner = CliRunner()
    result = runner.invoke(
        cli, ["title", "--titleID", 929]
    )
    assert result.exit_code == 0
    assert "929" in result.output

def test_searchtitle_functional():
    runner = CliRunner()
    result = runner.invoke(
        cli, ["searchtitle", "--titlepart", "Air America"]
    )
    assert result.exit_code == 0
    assert "Air America" in result.output

def test_bygenre_functional():
    runner = CliRunner()
    result = runner.invoke(
        cli, ["bygenre", "--genre", "Comedy", "--min", 5.2, "--start", 1990, "--end", 2000]
    )
    assert result.exit_code == 0

def test_name_functional():
    runner = CliRunner()
    result = runner.invoke(
        cli, ["name", "--nameID", 1]
    )
    assert result.exit_code == 0
    assert "1" in result.output

def test_searchname_functional():
    runner = CliRunner()
    result = runner.invoke(
        cli, ["searchname", "--namepart", "James"]
    )
    assert result.exit_code == 0
    assert "James" in result.output