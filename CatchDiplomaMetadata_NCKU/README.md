
# CatchDegree - 成功大學數位畢業證書資訊解讀工具

## 簡介
CatchDegree 是一款專為讀取並解析成功大學（國立成功大學 NCKU）中文數位畢業證書上資訊的工具。本工具能自動識別畢業證書上的學號、姓名、生日等重要資訊，幫助用戶快速獲取和整理畢業證書數據。

## 功能
- **識別資訊**：自動從畢業證書的數位圖像中識別出學生的學號、姓名、生日。

## 安裝需求
CatchDegree 需要安裝以下工具和套件：
- Pillow
- pytesseract
- pdf2image
- poppler-utils
- tesseract-ocr
- tesseract-ocr 語言包（繁體中文）

## 安裝指南
在安裝 CatchDegree 前，請依照以下步驟進行環境設定和套件安裝：

1. 安裝必要的 Python 套件：
```bash
pip install Pillow pytesseract pdf2image
```

2. 安裝 poppler-utils（PDF 轉換工具）：
```bash
apt-get install -y poppler-utils
```

3. 安裝 Tesseract-OCR 和中文語言包：
```bash
sudo apt install tesseract-ocr
sudo apt install tesseract-ocr-chi-tra
```

## 使用方法
1. 將 PDF 畢業證書上傳至工具能夠訪問的目錄。
2. 執行 CatchDegree 程式，程式將自動處理並顯示識別結果。
3. 查看輸出結果，包括學號、姓名、生日資訊。

## 輸出範例
以下是執行 CatchDegree 後可能得到的輸出結果：
```
Student ID: 4105123456
Name: 王小明
Birthday: 中華民國一百零三年五月二十日
```

## 注意事項
- 本工具目前僅支援國立成功大學的中文數位畢業證書。
- 確保 PDF 檔案的清晰度足夠，以提高識別準確率。
- 若遇到識別錯誤或無法識別的情況，請檢查原始 PDF 檔案是否清晰，並確認已正確安裝所有依賴套件。

## 開發者聯繫方式
如在使用過程中遇到問題或需要技術支援，請透過以下方式聯繫開發者：
- Website: darrenlu.com
- GitHub: [CatchDegreeRepo](https://github.com/CatchDiplomaMetadata_NCKU)

CatchDegree 致力於提供一個簡單易用且高效的畢業證書資訊解讀工具，感謝您的使用與支持！
