# ベースイメージとしてPythonの公式イメージを使用
FROM python:3.12.4

# ワークディレクトリを指定(存在しない場合は生成)
WORKDIR /app

# 実行されているdockerfileが位置する階層のリソースをコンテナのルートディレクトリにコピーする
# 'docker build'時に実行
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# コンテナ起動時に実行するコマンドを設定
# 'docker run'のタイミングで実行
CMD ["python", "myapp/app.py"]
