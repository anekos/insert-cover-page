# insert-cover-page

PDF の先頭に表紙画像ページを挿入する CLI ツールです。

## セットアップ

```bash
uv sync  # または pip install -e .
```

## 使い方

```bash
uv run python main.py insert original.pdf output.pdf backup/ cover1.png cover2.jpg
# 完了時に通知を出す場合
uv run python main.py insert -n original.pdf output.pdf backup/ cover1.png
```

- `original.pdf`: 元になる PDF
- `output.pdf`: 出力先 PDF
- `backup/`: 元 PDF をコピーしておく先のディレクトリ
- `cover*.png/jpg`: 先頭に追加したい画像。複数指定可。
- `-n/--notify`: 処理完了後にデスクトップ通知を送る（`notify-send` が必要）

## 依存関係

- Python 3.13+
- Pillow / pypdf (自動でインストールされます)
