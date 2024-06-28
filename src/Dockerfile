# ベースイメージとしてPythonの公式イメージを使用
FROM python:3.12.4

# ワークディレクトリを指定(存在しない場合は生成)
WORKDIR /app

# 依存関係をコピーしてインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# src配下のリソースをコンテナのワークディレクトリにコピーする
COPY . .

# コンテナ起動時に実行するコマンドを設定
CMD ["python", "myapp/app.py"]


