import pytest


@pytest.mark.bedrock
def test_bedrock_client_creation(bedrock_client):
    client = bedrock_client
    assert client is not None
    #assert client.is_connected()