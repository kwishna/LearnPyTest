import os


def is_feature_enabled():
    """
    Function that checks if a feature is enabled by looking up an environment variable.
    """
    return os.getenv("FEATURE_ENABLE", "false").lower() in ("true", "1", "yes")


def test_feature_enabled(mocker):
    """
    Test to ensure the function behaves correctly when the feature is enabled.
    """
    mocker.patch.dict(os.environ, {"FEATURE_ENABLE": "true"})
    assert is_feature_enabled()  


def test_feature_disabled(mocker):
    """
    Test to ensure the function behaves correctly when the feature is disabled.
    """
    mocker.patch.dict(os.environ, {"FEATURE_ENABLE": "false"})
    assert not is_feature_enabled()  
