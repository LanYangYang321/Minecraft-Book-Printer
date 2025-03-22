<!-- README.md -->
# Minecraft Book Printer

A tool to automatically format and print books in Minecraft—ideal for use on servers.

## Overview

Minecraft Book Printer helps you effortlessly convert plain text into the proper book format for Minecraft. The tool:
- Automatically formats text by wrapping lines and splitting pages according to Minecraft’s limitations.
- Simulates keyboard input to "print" the formatted pages directly into the game.
- Provides a preview mode for checking the output before sending it to Minecraft.

## Features

- **Automatic Text Formatting:** Splits input text into lines and pages based on configurable settings.
- **Customizable Settings:** Adjust the number of lines per page and maximum line width.
- **Preview Mode:** Use the `--preview` flag to view page formatting without executing input simulation.
- **Input Simulation:** Automatically pastes the formatted text into the game window upon trigger.
- **Detailed Logging:** Provides logs for easier debugging and tracking.

## Requirements

- **Operating System:** Windows (due to win32 API usage)
- **Python:** 3.6 or later
- **Dependencies:**
  - [pywin32](https://pypi.org/project/pywin32/)
  - [pyautogui](https://pypi.org/project/PyAutoGUI/)
  - [pyperclip](https://pypi.org/project/pyperclip/)
  - (Other built-in modules: argparse, logging, etc.)

Install dependencies via pip:
```bash
pip install -r requirements.txt
```
> If `requirements.txt` is not provided, install dependencies individually:
```bash
pip install pywin32 pyautogui pyperclip
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/LanYangYang321/Minecraft-Book-Printer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Minecraft-Book-Printer
   ```
3. (Optional) Set up a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```
4. Install the required dependencies as described above.

## Usage

### Running the Script

- If using the provided `run.bat`, it will activate the conda environment and launch the script:
  ```batch
  CALL conda activate base
  python main.py
  ```
- Alternatively, run the script directly:
  ```bash
  python main.py
  ```

### Command-Line Arguments

- **Input File:**  
  Specify an input file (default is `inputs/input2.txt`):
  ```bash
  python main.py input.txt
  ```
- **--lines:**  
  Set the number of lines per page (default is 14):
  ```bash
  python main.py --lines 16
  ```
- **--preview:**  
  Preview the formatted pages without simulating input:
  ```bash
  python main.py --preview
  ```
- **--verbose:**  
  Enable verbose logging for debugging:
  ```bash
  python main.py --verbose
  ```

### Workflow

1. **Prepare Input:**  
   Create a text file (default is `input.txt` or `inputs/input2.txt`) containing the content you want to print.
2. **Run the Script:**  
   Execute `python main.py` with the desired parameters.
3. **Trigger Input:**  
   After processing, switch to your Minecraft window. Press and hold the `Ctrl` key to start the automatic input simulation (press `ESC` to abort if needed).
4. **Automated Printing:**  
   The script will simulate the paste operation and input the formatted text into the game.

## Video Tutorial

For detailed instructions and a demonstration, please check out this video:  
[https://www.bilibili.com/video/BV144PHezE33](https://www.bilibili.com/video/BV144PHezE33)

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the tool.

## License

This project is licensed under the [MIT License](LICENSE).



<!-- readmecn.md -->
# 我的世界书籍打印工具

这是一个用于在《我的世界》服务器中自动格式化并打印书籍的工具。

## 概述

该工具可以帮助玩家将普通文本自动转换为符合《我的世界》书本格式的页面。它可以：
- 自动处理文本换行和分页，确保内容符合 Minecraft 的限制。
- 模拟键盘输入，将格式化后的文本自动“打印”到游戏中。
- 提供预览模式，让你在执行输入前先检查分页效果。

## 特性

- **自动文本格式化：** 根据设定自动将输入文本分割为行和页。
- **自定义配置：** 支持调整每页行数及最大行宽，满足不同需求。
- **预览模式：** 使用 `--preview` 参数预览分页效果，无需实际输入。
- **自动输入模拟：** 检测触发键后自动粘贴文本到游戏窗口。
- **详细日志记录：** 提供日志输出，便于调试和使用跟踪。

## 环境要求

- **操作系统：** Windows（由于使用了 win32 API）
- **Python：** 3.6 及以上版本
- **依赖库：**
  - [pywin32](https://pypi.org/project/pywin32/)
  - [pyautogui](https://pypi.org/project/PyAutoGUI/)
  - [pyperclip](https://pypi.org/project/pyperclip/)
  - 其他内置模块：argparse, logging 等

通过 pip 安装依赖：
```bash
pip install -r requirements.txt
```
> 如果没有提供 `requirements.txt`，请单独安装依赖：
```bash
pip install pywin32 pyautogui pyperclip
```

## 安装方法

1. 克隆仓库：
   ```bash
   git clone https://github.com/LanYangYang321/Minecraft-Book-Printer.git
   ```
2. 进入项目目录：
   ```bash
   cd Minecraft-Book-Printer
   ```
3. （可选）创建并激活虚拟环境：
   ```bash
   python -m venv env
   source env/bin/activate   # Windows系统下使用: env\Scripts\activate
   ```
4. 安装所需依赖，如上所述。

## 使用方法

### 运行脚本

- 如果使用提供的 `run.bat` 文件，会先激活 conda 环境再运行脚本：
  ```batch
  CALL conda activate base
  python main.py
  ```
- 或者直接运行脚本：
  ```bash
  python main.py
  ```

### 命令行参数

- **输入文件：**  
  可选输入文件参数（默认使用 `inputs/input2.txt`）：
  ```bash
  python main.py input.txt
  ```
- **--lines：**  
  设置每页行数（默认14行）：
  ```bash
  python main.py --lines 16
  ```
- **--preview：**  
  预览分页效果，不进行输入模拟：
  ```bash
  python main.py --preview
  ```
- **--verbose：**  
  启用详细调试日志：
  ```bash
  python main.py --verbose
  ```

### 使用流程

1. **准备输入：**  
   创建一个文本文件（默认为 `input.txt` 或 `inputs/input2.txt`），存放需要打印的内容。
2. **运行脚本：**  
   执行 `python main.py` 并传入相应参数。
3. **触发输入：**  
   脚本处理完毕后，切换到《我的世界》窗口，按住 `Ctrl` 键启动自动输入（如需中止，请按 `ESC` 键）。
4. **自动打印：**  
   脚本将模拟粘贴操作，将格式化后的文本输入到游戏中。

## 视频教程

详细说明和使用教程请参考视频：  
[https://www.bilibili.com/video/BV144PHezE33](https://www.bilibili.com/video/BV144PHezE33)

## 贡献

欢迎提出建议和提交 PR，共同完善该工具。

## 许可证

本项目遵循 [MIT 许可证](LICENSE).
