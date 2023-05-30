import os
from archrcover.download_repo import get_repo
from tempfile import mkdtemp

# test does not run locally at pfa

# def test_can_download_repo():
#     path = mkdtemp()
#     downloaded = get_repo('https://github.com/zeeguu/API', path = path)
    
#     assert downloaded == path

# def test_can_download_repo():
#     downloaded = get_repo('https://github.com/zeeguu/API')

#     path = downloaded + '/setup.py'
#     print(path)
#     assert os.path.isfile(path)