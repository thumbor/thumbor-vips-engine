import pytest
from thumbor.config import Config
from thumbor.context import Context, ServerParameters
from thumbor.importer import Importer


@pytest.fixture()
def context():
    security_key = "ACME-SEC"
    cfg = Config(SECURITY_KEY=security_key)

    importer = Importer(cfg)
    importer.import_modules()
    server = ServerParameters(
        8889, "localhost", "thumbor.conf", None, "info", None
    )
    server.security_key = security_key
    return Context(server, cfg, importer)
