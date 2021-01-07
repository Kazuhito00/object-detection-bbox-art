# object-detection-bbox-art
OpenCV上でのバウンディングボックスの装飾用の関数群です。 <br>
今までに作ったものが雑多に入っています。 <br>
そもそも「ボックス」じゃない物が大半ですが、心の目で見るとボックスが見えます。。。

# Requirement
 
* OpenCV 3.4.2
* Pillow 6.1.0
* Tensorflow 1.14.0(sample.pyを動かす場合のみ)
 
# Installation
 
利用したいPythonプログラムと同階層にboundingbox_artディレクトリをコピーしてください。

使用方法はsample.pyを参考にしてください。

# Usage
 
サンプルの実行方法は以下です。 <br>
サンプルプログラムでは手を検出し、検出箇所にバウンディングボックスを描画します。 <br>
バウンディングボックスの種類は、Nキー(次へ)、または、Pキー(前へ)を押下することで切り替わります。
 
```bash
python sample.py
```

# Contents
|01：3連通信リング|02：和風 黒円|
:---:|:---:
|![01](https://user-images.githubusercontent.com/37477845/75368668-6ad0d180-5905-11ea-93c0-635ba29a2a05.gif)|![02](https://user-images.githubusercontent.com/37477845/75368708-77edc080-5905-11ea-9c11-f80373aa9ec2.gif)|

|03：半透明矩形|04：半透明円形|
:---:|:---:
|![03](https://user-images.githubusercontent.com/37477845/75368731-84721900-5905-11ea-9794-1921e867120c.gif)|![04](https://user-images.githubusercontent.com/37477845/75368740-86d47300-5905-11ea-98ad-ee367e4fbe3b.gif)|

|05：銃口|06：レトロフィーチャー矩形|
:---:|:---:
|![05](https://user-images.githubusercontent.com/37477845/75368749-8b009080-5905-11ea-97d3-8b857a18748e.gif)|![06](https://user-images.githubusercontent.com/37477845/75368756-8fc54480-5905-11ea-8dff-4f4f9437c76b.gif)|

|07：スクエアローディング風|08：注釈線|
:---:|:---:
|![07](https://user-images.githubusercontent.com/37477845/75368779-9653bc00-5905-11ea-889e-b5e5c7e5be76.gif)|![08](https://user-images.githubusercontent.com/37477845/75455153-7979c000-59bb-11ea-97e8-e10a781c6ff3.gif)|

|09：すりガラス|10：SOUND ONLY モノリス|
:---:|:---:
|![09](https://user-images.githubusercontent.com/37477845/75457241-a16b2280-59bf-11ea-890e-d78535bb0d15.gif)|![10](https://user-images.githubusercontent.com/37477845/75578386-19604800-5aa7-11ea-9506-d468e8273d4e.gif)|

|11：3本追いかけっこ|12：-|
:---:|:---:
|![11](https://user-images.githubusercontent.com/37477845/76773952-9d743880-67e6-11ea-8a69-0504017d6721.gif)|![00](https://user-images.githubusercontent.com/37477845/75458245-e479c580-59c0-11ea-9217-360160b4775e.gif)|


その他、順次追加予定。。。

# Note

サンプル用に同梱している手検出用の「frozen_inference_graph.pb」もご自由に利用していただいて構いません。 <br>
また、モデルは別途訓練し直して精度アップ版に差し替える予定です。

 
# Author
高橋かずひと(https://twitter.com/KzhtTkhs)
 
# License 
object-detection-bbox-art is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).

# License(Font)
文字描画には、それぞれ以下のフォントを利用しています。

各フォントの著作権は各作者に属します。
* 02：衡山毛筆フォント(https://opentype.jp/kouzanmouhitufont.htm)
* 06：x12y20pxScanLineフォント(http://www17.plala.or.jp/xxxxxxx/00ff/)
* 08：M+ C Type-1フォント(http://mplus-fonts.osdn.jp/about.html)
* 10：Chicagoフォント(http://fonts3.com/fonts/c/Chicago.html) ※ライセンス不明なため同梱していません
