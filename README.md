## イメージをビルド
- **「.」** で、相対的にdockerファイルが存在する階層のパスを指定
- **--no-cache**を使うことで、イメージビルド時にキャッシュを使わない(イメージを削除しなおさなくて良くなる)
  - `docker image build　--no-cache -t i_scraping_job_site .`

## コンテナを起動(通常)
<!-- - `docker container run -d --name s_scraping_job_site -p 50001:50001 i_scraping_job_site` -->
- `docker container run -d --name s_scraping_job_site -v $pwd/app:/work/app -p 50001:50001 i_scraping_job_site`

- Webサイトにアクセス => http://localhost:50001/

## コンテナを起動(コンテナの中に入ってからWebサーバを起動するパターン)
- **-it** と **/bin/sh** を追記することで、コンテナが立ち上がり次第、コンテナの中身をCLIで触れる。
  <!-- - `docker container run -it --name s_scraping_job_site -p 50001:50001 i_scraping_job_site sh` -->
  - `docker container run -it --name s_scraping_job_site -v $pwd/app:/work/app -p 50001:50001 i_scraping_job_site sh`

- コンテナ内で下記コマンドを実行することでWebサーバを起動することができる
  - `uvicorn app.main:app --host 0.0.0.0 --port 50001`

- Webサイトにアクセス => http://localhost:50001/

## 起動中のコンテナを再起動
`docker restart s_scraping_job_site`

## 起動中のコンテナを確認
`docker ps`

## 起動中のコンテナを削除
`docker rm -f s_scraping_job_site`

## 存在しているイメージを確認
`docker image ls`

## イメージを削除
`docker rmi i_scraping_job_site`
