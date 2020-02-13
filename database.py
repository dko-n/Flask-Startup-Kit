import os
from pathlib import Path
import importlib
import sqlalchemy
from sqlalchemy.orm import sessionmaker

URL = 'mysql+pymysql://root:@localhost/flask?charset=utf8'
PJ_ROOT = Path().cwd()
MODEL_DIR = "models"
MODELS_NAME = ["{0}.{1}".format(MODEL_DIR, model.stem) for model in Path().cwd().joinpath(MODEL_DIR).iterdir() if model.is_file()]

class Database:
    def __init__(self, URL):
        self.sqlalchemy_ver = sqlalchemy.__version__
        self.url = URL
        self.engine = None
        self.models = {}
        self.model_class = {}
        self.session = None

    def main(self):
        """
        [name]: main
        [description]: main実行時に使用。
        """
        self._connect()
        self._autoloader()
        self._migration()
        self._load_model_class()

    def setup(self):
        """
        [name]: setup
        [description]: モジュールimport時に使用。
        """
        self._connect()
        self._autoloader()
        self._load_model_class()

    def _connect(self):
        """
        [name]: connect
        [description]: engineインスタンスの作成。
        """
        self.engine = sqlalchemy.create_engine(self.url, echo=False)
        self.session = sessionmaker(bind=self.engine)()

    def _autoloader(self):
        """
        [name]: autoloader
        [description]: src/modelsディレクトリ以下に存在するモジュールをimportします。
        """
        self.models = {str(model.split(".")[1]) : importlib.import_module(model) for model in MODELS_NAME}

    def _load_model_class(self):
        """
        [name]: load_model
        [description]: src/modelsディレクトリ以下に存在するモジュールをimportします。
        """
        for model, module in self.models.items():
            try:
                _class = getattr(module, model)
                self.model_class[model] = _class
            except ImportError:
                print('モジュールが見つかりません。')
            except AttributeError:
                print('クラスが見つかりません。')

    def _migration(self):
        """
        [name]: migration
        [description]: src/modelsディレクトリ以下に存在するモジュール内のmodelクラスのmigrationメソッドを実行する。
        """
        for model, module in self.models.items():
            try:
                _class = getattr(module, model)
                _class.migration(self.engine)
            except ImportError:
                print('モジュールが見つかりません。')
            except AttributeError:
                print('クラスが見つかりません。')
    
if __name__ == "__main__":
    db = Database(URL)
    db.main()
    # テストデータ挿入
    test = db.model_class["Test"]("1", "Database is Ready!!!")
    user = db.model_class["User"]("Panda", "Panda")
    db.session.add_all([test, user])
    db.session.commit()


