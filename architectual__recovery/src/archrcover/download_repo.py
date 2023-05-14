import os

from tempfile import mkdtemp
from git import Repo

def get_repo(repo_to_download, path = mkdtemp() + '/repo'):
    """
    Helper function to get repo - this might not work due to proxies on PFA network

    Args:
        repo_to_download (_type_): _description_
        path (_type_, optional): _description_. Defaults to mkdtemp()+'/repo'.

    Returns:
        path: returns path of downloaded repo
    """
    # If the file exists, it means we've already downloaded
    if not os.path.exists(path):
        Repo.clone_from("https://github.com/zeeguu/API", path)

    return path


