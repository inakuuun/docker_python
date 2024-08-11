## 前提
- Dockerがインストールされていること
- 一連の操作はDockerfileが存在する階層で実行すること(cdコマンドでDockerfileが存在する階層へ行く)

## イメージをビルド
- **「.」** で、相対的にdockerファイルが存在する階層のパスを指定
- **--no-cache**を使うことで、イメージビルド時にキャッシュを使わない(イメージを削除しなおさなくて良くなる)
  - `docker image build --no-cache -t i_scraping_job_site .`

## コンテナを起動
- **-d**を使うことで、バックグラウンドで起動(-dなしバージョンと比較した方がわかりやすいので試してみると良いかも)

`docker compose up -d`

Webサイトにアクセス => http://localhost:50001/

## 起動中のコンテナを確認
`docker container ps`

## 停止中のコンテナも含めて確認
`docker container ps -a`

## 起動中のコンテナを削除
- [CONTAINER ID]または[NAMES]を指定

`docker rm -f docker_python-scraping_job_site-1`

## 存在しているイメージを確認
`docker image ls`

## イメージを削除
- [REPOSITORY]を指定

`docker rmi docker_python-scraping_job_site`
