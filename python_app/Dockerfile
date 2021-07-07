FROM python:3.7.4-stretch

# パッケージの更新確認
RUN apt-get -y update

#chromeブラウザのインストール 
RUN apt-get install -y unzip
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
RUN echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get -y update
RUN apt-get -y install google-chrome-stable


# chromeドライバのインストール 
RUN curl -OL https://chromedriver.storage.googleapis.com/91.0.4472.101/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip chromedriver
RUN mv chromedriver /usr/bin/chromedriver

# 作業ディレクトリの作成
RUN mkdir /selenium
COPY ./src /selenium
WORKDIR /selenium

# Seleiumのインストール
RUN pip install selenium==3.141.0