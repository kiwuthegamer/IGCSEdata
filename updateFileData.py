import os, functools, json

def get_directory_structure(rootdir):
  """
  Creates a nested dictionary that represents the folder structure of rootdir
  """
  dir = {}
  rootdir = rootdir.rstrip(os.sep)
  start = rootdir.rfind(os.sep) + 1
  for path, dirs, files in os.walk(rootdir):
    folders = path[start:].split(os.sep)
    subdir = dict.fromkeys(files)
    parent = functools.reduce(dict.get, folders[:-1], dir)
    parent[folders[-1]] = subdir
  return dir

dir = get_directory_structure("DATA")

with open("fileData.json", "w") as f:
  f.write(json.dumps(dir))