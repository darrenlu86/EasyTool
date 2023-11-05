# ImageSlimmer 圖像壓縮工具

ImageSlimmer 是一款專為縮減圖片檔案大小而設計的工具，支持將 JPG 和 GIF（含動畫GIF）格式圖片壓縮至100KB以下，以利於網站加載或節省儲存空間。

## 功能

- 支援 JPG 和 GIF 格式圖片壓縮。
- 允許自定義壓縮後的目標檔案大小。
- 對 GIF 圖片提供分辨率調整和顏色數量減少的壓縮選項。

## 系統需求

- Python 3.x
- Pillow 庫

## 安裝指南

首先，您需要安裝 Python 和 Pillow。可以使用 pip 來安裝 Pillow：

```bash
pip install Pillow
```
## 使用說明
1. 確認您的輸入和輸出目錄路徑。
2. 在 ImageSlimmer.py 檔案中設定您的輸入輸出路徑。
3. 執行 ImageSlimmer.py 開始進行圖片壓縮

```bash
# 設定輸入輸出目錄路徑
input_folder_path = '/path/to/input/directory'
output_folder_path = '/path/to/output/directory'

# 呼叫函數開始壓縮圖片
compress_images_in_folder(input_folder_path, output_folder_path)
```

## 注意
- 壓縮 GIF 時，如果無法將檔案壓縮至100KB以下，將保留壓縮後的檔案並顯示警告。
- 壓縮過程中可能會降低圖片質量，尤其是在顯著降低分辨率或顏色數量時。
- 調整 resize_ratio 和 max_colors 可以幫助達成不同程度的壓縮效果。