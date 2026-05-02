# NumGen

具有Luhn验证的卡号生成器。

## 要求

- Python 3.x
- Tkinter（包含在Python中）

## 安装

```bash
pip install pyinstaller
```

## 运行

```bash
python NumGen.py
```

## 编译为.exe

```bash
pyinstaller --onefile --windowed NumGen.py
```

可执行文件将在 `dist/NumGen.exe` 中。

## 使用方法

- **BIN**：第一数字决定品牌
  - 3 = American Express
  - 4 = Visa
  - 5 = Mastercard
  - 6 = Discover
  - X = 随机

- **日期**：选择月份/年份或RND随机
- **CVV**：3位数字或XXX随机
- **数量**：要生成的卡片数量

## 输出格式

```
BIN|月|年|CVV
```

## 警告

本软件仅供教育使用。非法使用被禁止。