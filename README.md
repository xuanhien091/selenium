#  SELENIUM ...

## Docker のインストール手順

#### Dockerをダウンロードする
```
https://www.docker.com/products/docker-desktop
```

#### Dockerをインストールする
ダウンロードしたファイルをダブルクリックしてインストール。
途中で認証を要求されるので、パスワードとか入力。

<img width="420" alt="スクリーンショット 2021-07-07 16 36 09" src="https://user-images.githubusercontent.com/11476618/124718803-71337c80-df41-11eb-9ad3-43f7e7eb86f5.png">

クジラのマークが出てきたらOK。かわいい。
クリックして「Docker Desktop is runnning」があれば起動中。



## イメージ作成

#### Imageのビルド
```
sudo docker-compose build
```

#### コンテナを起動してバックグラウンドで起動
```
sudo docker-compose up -d
```

#### コンテナの起動の確認
```
sudo docker ps -a
```

## Dockerのコンテナに入ってこのプログラムを実行してみましょう。

#### コンテナに入る
```
sudo docker exec -it selenium_sample_python_app_1 bash
```

#### 作業ディレクトリに移動
```
cd /selenium
```

#### プログラムの実行
```
python twitter_like.py
```
