import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

def epub_to_text(epub_path):
    # 讀取 EPUB 檔案
    book = epub.read_epub(epub_path)

    # 用於儲存轉換後的文本
    output_text = []

    # 遍歷每個文件項目
    for item in book.get_items():
        # 只處理文件類型的項目
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            # 使用 BeautifulSoup 解析 HTML 內容
            soup = BeautifulSoup(item.content, 'html.parser')
            text = soup.get_text()
            # 加入到結果中，並在每章之間加入分隔符
            output_text.append('\n\n' + text.strip())

    # 將所有文本合併，並返回
    return '\n\n'.join(output_text)

# 使用範例，請將 'path_to_your_epub.epub' 替換為您的 EPUB 檔案路徑
epub_text = epub_to_text('path_to_your_epub.epub')

# 將結果寫入到 TXT 或 MD 檔案
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(epub_text)
