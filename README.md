## 前提
- Docker Desktopがインストールされていること
- 一連の操作はDockerfileとcompose.yamlファイルが存在する階層で実行すること(cdコマンドでDockerfileが存在する階層へ行く)

## コンテナを起動
- **-d**を使うことで、バックグラウンドで起動(-dなしバージョンと比較した方がわかりやすいので試してみると良いかも)

`docker compose up -d`

Webサイトにアクセス => http://localhost:50001/

## 起動中のコンテナを確認
`docker container ps`

## コンテナを停止
`docker compose down`

## 停止中のコンテナも含めて確認
`docker container ps -a`

## 起動中のコンテナを削除
- 「**docker container ps**」を実行した時に表示される[CONTAINER ID]または[NAMES]を指定して削除可能

`docker rm -f docker_python-scraping_job_site-1`

## 存在しているイメージを確認
`docker image ls`

## イメージを削除
- 「**docker image ls**」を実行した時に表示される[REPOSITORY]を指定して削除可能

`docker rmi docker_python-scraping_job_site`
