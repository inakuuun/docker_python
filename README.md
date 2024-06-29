## イメージをビルド
- **src/.** で、相対的にdockerファイルが存在する階層のパスを指定

`docker build -t python-app src/.`

## コンテナを起動
- **--rm**を追記することで、コンテナから抜けたタイミングでコンテナを削除してくれる
- この時 **-it** と **/bin/sh** を追記することで、コンテナが立ち上がり次第、コンテナの中身をCLIで触れるようになる。

`docker run -it --rm python-app /bin/sh`

`docker run --rm python-app`

## イメージを削除
`docker rmi python-app`

## 存在しているイメージを確認
`docker image ls`

## コンテナ内でpythonを実行
`docker image ls`
