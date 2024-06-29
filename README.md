## イメージをビルド
- **「.」** で、相対的にdockerファイルが存在する階層のパスを指定
- **--no-cache**を使うことで、イメージビルド時にキャッシュを使わない(イメージを削除しなおさなくて良くなる)
 
`docker image build　--no-cache -t python-app .`

## コンテナを起動
- **--rm**を追記することで、コンテナから抜けたタイミングでコンテナを削除してくれる
- この時 **-it** と **/bin/sh** を追記することで、コンテナが立ち上がり次第、コンテナの中身をCLIで触れるようになる。

`docker container run -it --rm python-app /bin/sh`

`docker container run -it --rm python-app /bin/sh`

`docker container run --rm python-app`

## コンテナ内でpythonを実行
`python myapp/app.py`

## イメージを削除
`docker rmi python-app`

## 存在しているイメージを確認
`docker image ls`
