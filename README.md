## Dockerイメージをビルド
- **src/.** で、相対的にdockerファイルが存在する階層のパスを指定

`docker build -t python-app src/.`

## Dockerコンテナを起動
- **--rm**を追記することで、コンテナから抜けたタイミングでコンテナを削除してくれる
- この時 **-it** と **/bin/sh** を追記することで、コンテナが立ち上がり次第、コンテナの中身をCLIで触れるようになる。

`docker run -it --rm python-app /bin/sh`
