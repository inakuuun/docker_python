## Dockerイメージをビルド
`docker build -t my-python-app . `

## Dockerコンテナを起動
- '--rm'を追記することで、コンテナから抜けたタイミングでコンテナを削除してくれる
- この時/bin/shと末尾に追記することで、コンテナが立ち上がり次第、コンテナの中身をCLIで触れるようになる。

`docker run -it --rm my-python-app /bin/sh`
