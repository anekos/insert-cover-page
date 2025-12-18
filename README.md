# insert-cover-page

PDF の先頭に表紙画像ページを挿入する CLI ツールです。

## セットアップ

```bash
uv sync  # または pip install -e .
```

## 使い方

```bash
uv run python main.py insert original.pdf output.pdf cover1.png cover2.jpg
```

- `original.pdf`: 元になる PDF
- `output.pdf`: 出力先 PDF
- `cover*.png/jpg`: 先頭に追加したい画像。複数指定可。

## 依存関係

- Python 3.13+
- Pillow / pypdf (自動でインストールされます)
