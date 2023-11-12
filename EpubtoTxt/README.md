
# EPUB to Text Converter

這個 Python 程式可以將 EPUB 檔案轉換為 TXT 或 Markdown (.md) 檔案。它特別適用於需要將 EPUB 內容用於數據處理和分析的場景，並且會嘗試保留每個大章節的段落區分。

## 功能

- 讀取 EPUB 檔案並提取其中的文本。
- 保留原始文檔的大章節結構，便於後續處理。
- 輸出為易於處理的 TXT 或 Markdown 格式。

## 安裝需求

- Python 3.x
- `EbookLib`: 用於讀取 EPUB 檔案。
- `beautifulsoup4`: 用於解析 HTML 內容。

這些依賴可以通過以下命令安裝：

```bash
pip install EbookLib beautifulsoup4
```

## 使用說明

1. 確保已安裝所有必要的依賴。
2. 替換腳本中的 `'path_to_your_epub.epub'` 為您的 EPUB 檔案路徑。
3. 執行程式。轉換後的文本將保存在同目錄下的 `output.txt` 檔案中。

範例：

```python
epub_text = epub_to_text('path_to_your_epub.epub')

with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(epub_text)
```

## 自定義

- 根據 EPUB 檔案的不同，您可能需要調整文本處理的邏輯。
- 可以修改輸出格式或增加其他功能，如章節標題識別等。

## 開發者聯繫方式
如在使用過程中遇到問題或需要技術支援，請透過以下方式聯繫開發者：
- Website: darrenlu.com