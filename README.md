# 🧪Flask-StartUp-Kit
Flaskは自由な構成が可能なWeb Application Frameworkなので、PJを始めるに当たり必要最小限の構成を持ったひな型があると便利だと思い作成いたしました。

![main](https://user-images.githubusercontent.com/13768156/74444176-cf2c7380-4eb7-11ea-8167-2cf2968694c1.png)

# 🖥Dependency
* Python3.3 >=
* 使用したライブラリはrequirements.txtに記載。

# 👩‍💻Setup
1. git clone git@github.com:obeke4353/Flask-Startup-Kit.git
2. Databaseの準備。
3. config.py内のDATABASE_CONFIG定数を設定したDatabaseに合わせて書き換える。

![config.py](https://user-images.githubusercontent.com/13768156/74444166-cc318300-4eb7-11ea-8943-1b5ccbd1707b.png)


4. PJトップディレクトリでコマンド実行。```python database.py```
5. PJトップディレクトリでコマンド実行。```python app.py```

# 👍Usage
1. Setupを終えたら、ブラウザのアドレスバーに http://127.0.0.1:5001/ と入力する。
2. うまくいっていれば、以下の画像のようなTOPページが表示されます。

![main](https://user-images.githubusercontent.com/13768156/74444176-cf2c7380-4eb7-11ea-8167-2cf2968694c1.png)

3. Databaseの準備が出来ているかは、Environmentの上から4番目の項目でわかるようになっています。Databaseの準備が出来ていない場合は、以下のような文言が表示されることになっています。

![database](https://user-images.githubusercontent.com/13768156/74445902-78746900-4eba-11ea-8e7f-1b31306121e5.png)

4. このアプリには、デフォルトでログインUserが作成されています。nameはPandaでPasswordもPandaです。アプリケーションのナビゲーションメニューのSignInページ内にログインフォームがあります。

![login](https://user-images.githubusercontent.com/13768156/74446266-fa649200-4eba-11ea-951a-a59562b0e144.png)

5. ログインが成功すると、画面のジャンボトロン上にログインユーザ名が表示されます。

![loggedin](https://user-images.githubusercontent.com/13768156/74446482-4b748600-4ebb-11ea-93c4-863786fd1a89.png)

# 📝Author
おべけ！？

# 📖References
* [Flask公式](https://a2c.bitbucket.io/flask/)
* [SQLAlchemy公式](https://docs.sqlalchemy.org/en/13/index.html)
