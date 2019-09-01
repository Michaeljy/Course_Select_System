from conf import settings
import os
import pickle


def select(cls, username):
    cls_name = cls.__name__
    cls_path = os.path.join(
        settings.DB_PATH, cls_name
    )
    if os.path.isdir(cls_path):
        user_path = os.path.join(
            cls_path, username
        )
        if os.path.exists(user_path):
            with open(user_path, 'rb') as fr:
                obj = pickle.load(fr)
                return obj

def save(self):
    cls_name = self.__class__.__name__
    cls_dir = os.path.join(settings.DB_PATH, cls_name)
    if not os.path.isdir(cls_dir):
        os.mkdir(cls_dir)
    self_path = os.path.join(cls_dir, self.name)
    with open(self_path, 'wb') as fw:
        pickle.dump(self, fw)
        fw.flush()