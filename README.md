# Flask-StartUp-Kit
* Flaskは自由な構成が可能なWeb Application Frameworkなので、PJを始めるに当たり必要最小限の構成を持ったひな型があると便利だと思い作成いたしました。

![main](https://user-images.githubusercontent.com/13768156/74444176-cf2c7380-4eb7-11ea-8167-2cf2968694c1.png)

# Dependency
* Python3.3 >=
* 使用したライブラリはrequirements.txtに記載。

# Setup
1. git clone git@github.com:dko-n/Flask-Startup-Kit.git
2. Databaseの準備。
3. config.py内のDATABASE_CONFIG定数を設定したDatabaseに合わせて書き換える。

![config.py](https://user-images.githubusercontent.com/13768156/74444166-cc318300-4eb7-11ea-8943-1b5ccbd1707b.png)


4. PJトップディレクトリでコマンド実行。```python database.py```
5. PJトップディレクトリでコマンド実行。```python app.py```

# Usage
* Setupを終えたら、ブラウザのアドレスバーに http://127.0.0.1:5001/ と入力する。

# Author
* おんてゃん(⋈◍＞◡＜◍)。✧♡

# References
* https://a2c.bitbucket.io/flask/
* https://docs.sqlalchemy.org/en/13/index.html