# visual-chart
pythonでデスクトップアプリケーションの作成

## セットアップ

### 必須条件

- Python 3.11 (3.8以上)
- Streamlit 1.31以上
- npm or yarn (node v18以降)

### 仮想環境

venvを用いてインストールを行います。
venvは、Pythonの標準ライブラリです。

```sh
% cd (任意のフォルダ)
% python3 -m venv venv
% source venv/bin/activate
```


### インストール

```sh
(venv) % pip install -r requirements.txt
```

## ビルド 

```sh
% nvm use v20
% npm install
```

dumpを行い、必要なパッケージをパッケージング
dumpの後のフォルダー指定はプロジェクトフォルダー内のstreamlitがあるフォルダーを指定
```sh
% npm run dump visual-chart -- -r requirements.txt
```

ローカルでアプリを立ち上げて確認
```sh
% npm run serve
```

## デスクトップアプリ
デスクトップアプリにする場合、起動のpythonファイルをstreamlit_app.pyと命名する。
それ以外の場合はエラーが表示されてしまう

Windows
```shell
npm run dist -- --win
```
Mac
```shell
npm run dist -- --mac
```




