from conf import settings
import os
import pickle


def save(obj):
    path_dir = os.path.join(settings.BASE_DB, obj.__class__.__name__.lower())
    if not os.path.isdir(path_dir):
        os.mkdir(path_dir)
    path_obj = os.path.join(path_dir, obj.name)
    with open(path_obj, 'wb') as f:
        pickle.dump(obj, f)
        f.flush()


def select(name, dir_type):
    path_dir = os.path.join(settings.BASE_DB, dir_type)
    if not os.path.isdir(path_dir):
        os.mkdir(path_dir)
    path_obj = os.path.join(path_dir, name)
    if os.path.exists(path_obj):
        with open(path_obj, 'rb') as f:
            return pickle.load(f)
    else:
        return None