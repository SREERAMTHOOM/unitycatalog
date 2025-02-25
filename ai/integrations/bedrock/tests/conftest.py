import pytest   
import boto3

# This file contains fixtures for the Bedrock integration tests.
# The fixtures are used to create a Bedrock client for testing purposes.

pytestmark = pytest.mark.bedrock


# Create fixtures
@pytest.fixture
def bedrock_client():
    return boto3.client('bedrock', region_name='us-west-2')
    