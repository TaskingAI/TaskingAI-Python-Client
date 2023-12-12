import pytest

if __name__ == "__main__":
    pytest.main(['-m test_sync'])
    pytest.main(['-m test_async'])

