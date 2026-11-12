# Python Programming Class

Pythonプログラミング演習の**解答例（サンプルコード）**を公開するリポジトリです。授業中の復習だけでなく、卒業後も参照できるようにしています。

各プログラムは学習用の例です。授業での課題条件や開発環境によって、実行方法や結果が異なる場合があります。

## プログラム一覧

ファイル名の `programX-Y.py` は、授業で使用している課題番号に対応します。

| 回 | 主な内容 | プログラム |
|---|---|---|
| 第2回 | 基本的な入出力・演算 | [2-1](program2-1.py) / [2-2](program2-2.py) / [2-3](program2-3.py) |
| 第3回 | リストと集計 | [3-1](program3-1.py) / [3-2](program3-2.py) |
| 第4回 | 条件分岐と繰り返し | [4-1](program4-1.py) / [4-2](program4-2.py) / [4-3](program4-3.py) |
| 第5回 | リスト処理と条件 | [5-1](program5-1.py) / [5-2](program5-2.py) / [5-3](program5-3.py) |
| 第6回 | データ処理・可視化 | [6-1](program6-1.py) / [6-2](program6-2.py) / [6-3](program6-3.py) |
| 第7回 | 関数 | [7-1](program7-1.py) / [7-2](program7-2.py) / [7-3](program7-3.py) / [7-4](program7-4.py) |
| 第8回 | クラスの基礎 | [8-1](program8-1.py) / [8-2](program8-2.py) / [8-3](program8-3.py) |
| 第9回 | クラス・継承 | [9-1](program9-1.py) / [9-2](program9-2.py) / [9-3](program9-3.py) / [9-4](program9-4.py) / [9-5](program9-5.py) |
| 第10回 | 画像処理の基礎 | [10-1](program10-1.py) |
| 第11回 | データクラス | [11-1](program11-1.py) / [11-2](program11-2.py) / [11-3](program11-3.py) |
| 第12回 | 画像処理の応用 | [12-1](program12-1.py) / [12-2](program12-2.py) / [12-3](program12-3.py) |

## プログラムの内容

| ファイル | 演習内容 |
|---|---|
| [`program2-1.py`](program2-1.py) | べき乗の計算 |
| [`program2-2.py`](program2-2.py) | 氏名・学籍番号の入出力 |
| [`program2-3.py`](program2-3.py) | 平方根の近似計算 |
| [`program3-1.py`](program3-1.py) | リストへの要素の挿入 |
| [`program3-2.py`](program3-2.py) | 科目得点の合計・平均 |
| [`program4-1.py`](program4-1.py) | 3つの数の最大値 |
| [`program4-2.py`](program4-2.py) | 数当てゲーム |
| [`program4-3.py`](program4-3.py) | 複数条件による判定 |
| [`program5-1.py`](program5-1.py) | 点数の条件判定 |
| [`program5-2.py`](program5-2.py) | 条件を満たす要素の抽出 |
| [`program5-3.py`](program5-3.py) | 型の確認とcontinue |
| [`program6-1.py`](program6-1.py) | Excelデータの散布図 |
| [`program6-2.py`](program6-2.py) | Excelデータの相関行列 |
| [`program6-3.py`](program6-3.py) | NumPy配列の行・列合計 |
| [`program7-1.py`](program7-1.py) | うるう年の判定 |
| [`program7-2.py`](program7-2.py) | 点数の合否判定 |
| [`program7-3.py`](program7-3.py) | 最大公約数 |
| [`program7-4.py`](program7-4.py) | 最大値と最小値の差 |
| [`program8-1.py`](program8-1.py) | Carクラス |
| [`program8-2.py`](program8-2.py) | Bookクラス |
| [`program8-3.py`](program8-3.py) | ShoppingCartクラス |
| [`program9-1.py`](program9-1.py) | Libraryクラス |
| [`program9-2.py`](program9-2.py) | BankAccountクラス |
| [`program9-3.py`](program9-3.py) | Animalクラスの継承 |
| [`program9-4.py`](program9-4.py) | Applianceクラスの継承 |
| [`program9-5.py`](program9-5.py) | Studentクラスの継承 |
| [`program10-1.py`](program10-1.py) | OpenCVによる画像の領域編集 |
| [`program11-1.py`](program11-1.py) | データクラスとリスト |
| [`program11-2.py`](program11-2.py) | データクラスと辞書 |
| [`program11-3.py`](program11-3.py) | データクラスとタプル |
| [`program12-1.py`](program12-1.py) | 領域の色変更 |
| [`program12-2.py`](program12-2.py) | 色成分の変更 |
| [`program12-3.py`](program12-3.py) | グレースケール画像のしきい値処理 |

## 公開時に確認したPython環境

以下は2026年11月に、教材作成者のMac上で確認した**使用環境のバージョン**です。
この環境で、Excelファイルを使用するデータ処理とOpenCVによる画像処理が正常に動作することを教材作成者が確認しました。

| ソフトウェア | バージョン |
|---|---|
| macOS | 26.6.2 |
| Python | 3.15.2 |
| NumPy | 2.5.4 |
| pandas | 3.1.1 |
| Matplotlib | 3.11.2 |
| openpyxl | 3.1.5 |
| OpenCV（`opencv-python`） | 5.0.0.93 |

- 上記のパッケージバージョンは `python3 -m pip list` の結果から記録しています。
- **Excelデータ処理および画像処理については動作確認済みです（2026年11月、教材作成者による確認）。**
- **全33プログラムの一括動作確認が完了したことを意味するものではありません。** その他の課題については、必要に応じて実行を確認してください。
- Pythonやライブラリのバージョンが異なる環境で、同じ結果になるとは限りません。特にパッケージの対応OS・Pythonバージョンによっては、指定バージョンのインストールができない場合があります。

## 実行方法（macOS・VS Codeの例）

Python 3.15.2を利用する場合、リポジトリをダウンロードして展開し、VS Codeで展開先のフォルダを開いてください。ターミナルで次を実行します。

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python program2-1.py
```

VS Codeでは、`Python: Select Interpreter` から `.venv/bin/python` を選択してください。既に仮想環境が有効な場合は、新しく作り直す必要はありません。`requirements.txt` には上表のバージョンを記載しています。

- `input()` を使うプログラムでは、実行中にキーボード入力が必要です。
- [`program2-3.py`](program2-3.py) の平方根の近似計算は、**0より大きい数**の入力を前提としています。0を入力するとゼロ除算エラーになります。
- [`program4-3.py`](program4-3.py) は条件分岐の学習用に単純化した例であり、実際の法令・健康上の判断を示すものではありません。
- `dataclasses` や `random` はPythonの標準ライブラリなので追加インストールは不要です。
- 第6回・第10回・第12回の一部のプログラムでは、追加ライブラリ（`requirements.txt` を参照）と同梱のデータファイルを使用します。

## 演習用データファイル・画像ファイル

以下の**4ファイルはこのリポジトリに同梱**しています。Pythonプログラムと同じフォルダに配置しているため、リポジトリをダウンロードしてそのフォルダで実行すれば、コード中のファイル名を変更せずに読み込めます。

| プログラム | 使用するファイル | 内容 |
|---|---|---|
| [`program6-1.py`](program6-1.py) | [`shintyou_taijyuu.xlsx`](shintyou_taijyuu.xlsx) | 身長・体重データの散布図 |
| [`program6-2.py`](program6-2.py) | [`test_data.xlsx`](test_data.xlsx) | データの相関行列 |
| [`program10-1.py`](program10-1.py), [`program12-1.py`](program12-1.py), [`program12-3.py`](program12-3.py) | [`sample.jpg`](sample.jpg) | 画像の領域編集・しきい値処理 |
| [`program12-2.py`](program12-2.py) | [`building.jpg`](building.jpg) | 画像の色成分の変更 |

> **公開データに関する注意**：この公開リポジトリのExcelファイルや画像は誰でも閲覧・取得できます。データの個人情報、および画像の公開・再配布に必要な権限を継続して確認してください。

OpenCVを使うプログラムでは `cv2.imshow()` による画像ウィンドウ表示を利用しています。そのため、GUIを使用できるローカルPCでの実行を想定しています。Google Colabなどのブラウザ環境では、表示処理の変更が必要です。

## ソースコードの利用について

これらのコードは教材として公開しています。再配布や改変を許可する場合は、授業・大学の方針に合わせて `LICENSE` を追加することを検討してください。

## 運用に関するメモ

- GitHub上でファイル名をクリックするとコードを読めます。
- `Code` → `Download ZIP` で一式を保存できます。
- ソースコードの修正履歴はGitHubのコミット履歴から確認できます。
- **解答例の公開時期**は、履修中の課題の公平性に配慮して判断してください。
