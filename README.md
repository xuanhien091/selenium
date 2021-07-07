#  SELENIUM ...

## Installation

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
