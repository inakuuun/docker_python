# ベースイメージとしてPythonの公式イメージを使用
FROM python:3.12.4

# ワークディレクトリを指定(存在しない場合は生成)
WORKDIR /work

# 'docker build'時に実行
# 実行されているdockerfileが位置する階層のリソースをコンテナのルートディレクトリにコピーする
COPY ./requirements.txt /work/requirements.txt
# 開発で使用するパッケージをインストール
RUN pip install --no-cache-dir --upgrade -r /work/requirements.txt

# ADD ./app /work/app
COPY ./app /work/app

# 'docker run'時に実行
# コンテナ起動時に実行するコマンドを設定
# CMD ["python", "myapp/app.py"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "50001"]
