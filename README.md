# object-detection-bbox-art
 バウンディングボックスの装飾用の関数群です。
 
 今までに作ったものが雑多に入っています。

# Requirement
 
* OpenCV 3.4.2
* Pillow 6.1.0
* Tensorflow 1.14.0(sample.pyを動かす場合のみ)
 
# Installation
 
利用したいPythonプログラムと同階層にboundingbox_artディレクトリをコピーしてください。

使用方法はsample.pyを参考にしてください。

# Usage
 
サンプルの実行方法は以下です。
 
```bash
python sample.py
```

# Contents
|01：|02：|
:---:|:---:
|![01](https://user-images.githubusercontent.com/37477845/75368668-6ad0d180-5905-11ea-93c0-635ba29a2a05.gif)|![02](https://user-images.githubusercontent.com/37477845/75368708-77edc080-5905-11ea-9c11-f80373aa9ec2.gif)|

|03：|04：|
:---:|:---:
|![03](https://user-images.githubusercontent.com/37477845/75368731-84721900-5905-11ea-9794-1921e867120c.gif)|![04](https://user-images.githubusercontent.com/37477845/75368740-86d47300-5905-11ea-98ad-ee367e4fbe3b.gif)|

|05：|06：|
:---:|:---:
|![05](https://user-images.githubusercontent.com/37477845/75368749-8b009080-5905-11ea-97d3-8b857a18748e.gif)|![06](https://user-images.githubusercontent.com/37477845/75368756-8fc54480-5905-11ea-8dff-4f4f9437c76b.gif)|

|07：|08：|
:---:|:---:
|![07](https://user-images.githubusercontent.com/37477845/75368779-9653bc00-5905-11ea-889e-b5e5c7e5be76.gif)|![08](https://user-images.githubusercontent.com/37477845/75368785-994eac80-5905-11ea-9383-b3e0f96582eb.gif)|


# Note

サンプル用に同梱している手検出用の「frozen_inference_graph.pb」もご自由に利用していただいて構いません。

また、モデルは別途訓練し直して精度アップ版に差し替える予定です。

 
# Author
高橋かずひと(https://twitter.com/KzhtTkhs)
 
# License 
tensorflow2-keras-learn is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
