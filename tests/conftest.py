import pytest


@pytest.fixture
def base_context():
    return {
        "full_name": "Roman Example",
        "email": "roman.example@example.com",
        "github_username": "example",
        "github_organization": "boardpack",
        "project_name": "Boardpack Project",
        "project_short_description": "A sample Boardpack project",
        "version": "0.1.0",
        "use_pytest": "y",
        "use_dependabot": "y",
        "use_pre_commit_hook": "y",
        "open_source_license": "MIT license",
    }
