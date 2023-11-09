from pdf2image import convert_from_path
import pytesseract
import re


# 將 PDF 頁面轉換為圖像列表
images = convert_from_path('your_file_path')

# 認定識字的文字
all_text = ""
for image in images:
    text = pytesseract.image_to_string(image, lang='chi_tra')  # 假定是繁體中文
    all_text += text

# 提取姓名、生日和學號
student_id_pattern = r'學號: (\S+)'
name_pattern = r'學生\s+([\u4e00-\u9fff]+)'  # 調整以符合實際的證書格式
birthday_pattern = r'中華民國([\u4e00-\u9fff零一二三四五六七八九十百千]+)年([\u4e00-\u9fff零一二三四五六七八九十]+)月([\u4e00-\u9fff零一二三四五六七八九十]+)日生'  # 調整以符合實際的證書格式
# 調整以符合實際的證書格式

# 使用正則表達式提取姓名、生日、學號
student_id_match = re.search(student_id_pattern, all_text)
name_match = re.search(name_pattern, all_text)
birthday_match = re.search(birthday_pattern, all_text)

# 检查是否找到了姓名、生日、學號，并提取
student_id = student_id_match.group(1) if student_id_match else None
name = name_match.group(1) if name_match else None
birthday = "中華民國{}年{}月{}日".format(*birthday_match.groups()) if birthday_match else None

# 輸出結果
print(f'Student ID: {student_id}')
print(f'Name: {name}')
print(f'Birthday: {birthday}')  # 直接輸出匹配到的生日全文

