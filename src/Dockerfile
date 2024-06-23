# ベースイメージとしてPythonの公式イメージを使用
FROM python:3.12.4

# ワークディレクトリを指定(存在しない場合は生成)
WORKDIR /app

# 依存関係をコピーしてインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 
COPY . .

# コンテナ起動時に実行するコマンドを設定
CMD ["python", "app/app.py"]

# Dockerイメージをビルド
# docker build -t my-python-app . 

# この時/bin/shと末尾に追記することで、コンテナが立ち上がり次第、コンテナの中身をCLIで触れるようになる。
# '--rm'を追記することで、コンテナから抜けたタイミングでコンテナを削除していくれる
# docker run -it --rm my-python-app /bin/sh


