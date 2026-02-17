from app.config.settings import settings


def test_settings_loads_environment_defaults():
    assert hasattr(settings, "POKEAPI_BASE_URL")
