import pytest
import os

if __name__ == "__main__":
    pytest.main(['-m sync', '--clean-alluredir',  '--alluredir=./test/report'])
    pytest.main(['-m a_sync',  '--alluredir=./test/report'])
    os.system("allure serve ./test/report")
