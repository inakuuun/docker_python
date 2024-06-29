## イメージをビルド
- **「.」** で、相対的にdockerファイルが存在する階層のパスを指定
- **--no-cache**を使うことで、イメージビルド時にキャッシュを使わない(イメージを削除しなおさなくて良くなる)
 
`docker image build　--no-cache -t scraping_job_site .`

## コンテナを起動(通常)

`docker container run -d --name scraping_job_site_co -p 50001:50001 scraping_job_site`

-  **-it** と **/bin/sh** を追記することで、コンテナが立ち上がり次第、コンテナの中身をCLIで触れる。

## コンテナを起動(コンテナの中に入るパターン)
`docker container run -it --name scraping_job_site_co -p 50001:50001 scraping_job_site sh`

- **-it** と **/bin/sh**で起動した場合は、コンテナ内で下記コマンドを実行することでWebサーバを起動することができる

`uvicorn app.main:app --host 0.0.0.0 --port 50001`

## Webサイトにアクセス

http://localhost:50001/

## 起動中のコンテナを確認
`docker ps`

## 起動中のコンテナを削除
`docker rm -f scraping_job_site_co`

## イメージを削除
`docker rmi scraping_job_site`

## 存在しているイメージを確認
`docker image ls`
