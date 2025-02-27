import re
import argparse
import time
import sys
import logging
from typing import List, Dict
import win32api
import win32con
import pyautogui
import pyperclip

# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class BookConfig:
    """书本格式配置类"""

    def __init__(
            self,
            lines_per_page: int = 14,
            max_line_width: float = 57.0,
            char_widths: Dict[str, float] = None,
            chinese_punctuation: List[str] = None
    ):
        self.lines_per_page = lines_per_page
        self.max_line_width = max_line_width
        self.char_widths = char_widths or self.default_char_widths()
        self.chinese_punctuation = chinese_punctuation or self.default_chinese_punctuation()

    @staticmethod
    def default_char_widths() -> Dict[str, float]:
        return {
            '`': 1.5,
            '[': 2, ']': 2, '(': 2, ')': 2, '"': 2, '{': 2, '}': 2, '*': 2, ' ': 2,
            '.': 1, ',': 1, ';': 1, ':': 1, "'": 1, '!': 1, '|': 1,
            '<': 2.5, '>': 2.5,
            '→': 4, '~': 4,
            '\n': -1
        }

    @staticmethod
    def default_chinese_punctuation() -> List[str]:
        return [
            '，', '。', '、', '？', '！', '】', '【', '（', '）',
            '·', '；', '：', '“', '‘', '《', '》', '…'
        ]


class TextFormatter:
    """文本格式化处理类"""

    def __init__(self, config: BookConfig):
        self.config = config

    def is_chinese(self, char: str) -> bool:
        """判断字符是否为中文或中文标点"""
        if char in self.config.chinese_punctuation:
            return True
        return re.match(r'[\u4e00-\u9fff]', char) is not None

    def get_char_width(self, char: str) -> float:
        """获取字符宽度"""
        if char in self.config.char_widths:
            return self.config.char_widths[char]
        if self.is_chinese(char):
            return 4.5
        return 3.0  # 默认英文字符宽度

    def split_into_lines(self, text: str) -> List[str]:
        """将文本分割为符合宽度限制的行"""
        current_line = []
        current_width = 0.0
        lines = []

        for char in text:
            char_width = self.get_char_width(char)

            if char == '\n':
                lines.append(''.join(current_line))
                current_line = []
                current_width = 0.0
                continue

            if current_width + char_width > self.config.max_line_width:
                lines.append(''.join(current_line))
                current_line = [char]
                current_width = char_width
            else:
                current_line.append(char)
                current_width += char_width

        if current_line:
            lines.append(''.join(current_line))

        return self._process_trailing_newlines(text, lines)

    def _process_trailing_newlines(self, original: str, lines: List[str]) -> List[str]:
        """处理原始文本末尾的换行符"""
        if original.endswith('\n'):
            while lines and lines[-1] == '':
                lines.pop()
            if lines:
                lines[-1] = lines[-1].rstrip('\n')
        return lines

    def format_pages(self, lines: List[str]) -> List[str]:
        """将行列表分页处理"""
        pages = []
        current_page = []

        for line in lines:
            current_page.append(line)
            if len(current_page) >= self.config.lines_per_page:
                pages.append('\n'.join(current_page))
                current_page = []

        if current_page:
            pages.append('\n'.join(current_page))

        return pages


class InputHandler:
    """输入处理类"""

    def __init__(self, delay: float = 0.1):
        self.delay = delay
        self.abort_key = 0x1B  # ESC键虚拟键码

    def wait_for_trigger(self, trigger_key: int = win32con.VK_CONTROL):
        """等待指定触发键按下"""
        logger.info("等待Ctrl键按下（按ESC取消）...")
        while True:
            if win32api.GetAsyncKeyState(self.abort_key) & 0x8000:
                logger.warning("检测到ESC键，程序终止")
                sys.exit(0)
            if win32api.GetAsyncKeyState(trigger_key) & 0x8000:
                logger.info("检测到Ctrl键，开始输入")
                return
            time.sleep(self.delay)

    def simulate_input(self, pages: List[str]):
        """模拟键盘输入"""
        original_pos = pyautogui.position()
        try:
            for idx, page in enumerate(pages, 1):
                pyperclip.copy(page)
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(self.delay)
                pyautogui.click(original_pos)
                logger.debug(f"已输入第{idx}/{len(pages)}页")
                time.sleep(self.delay)
        except Exception as e:
            logger.error(f"输入过程中发生错误: {str(e)}")
            raise


def main(path='input.txt'):
    # 命令行参数解析
    parser = argparse.ArgumentParser(description="自动格式化文本为Minecraft书本格式")
    parser.add_argument('input', nargs='?', default=path,
                        help="输入文件路径（默认为input.txt）")
    parser.add_argument('--lines', type=int, default=14,
                        help="每页行数（默认为14）")
    parser.add_argument('--preview', action='store_true',
                        help="仅预览分页结果不执行输入")
    parser.add_argument('--verbose', action='store_true',
                        help="显示详细调试信息")
    args = parser.parse_args()

    if args.verbose:
        logger.setLevel(logging.DEBUG)

    # 初始化配置
    config = BookConfig(lines_per_page=args.lines)
    formatter = TextFormatter(config)
    input_handler = InputHandler()

    try:
        # 读取并处理文本
        with open(args.input, 'r', encoding='utf-8') as f:
            text = f.read()

        lines = formatter.split_into_lines(text)
        pages = formatter.format_pages(lines)

        # 预览模式处理
        if args.preview:
            logger.info("预览模式（共%d页）:", len(pages))
            for i, page in enumerate(pages, 1):
                print(f"\n=== 第{i}页 ===")
                print(page)
                print("=" * 20)
            return

        # 显示执行信息
        logger.info(f"共处理{len(pages)}页文本（每页{args.lines}行）")
        logger.info("切换到游戏窗口后，按住Ctrl键开始自动输入...")

        # 执行自动输入
        input_handler.wait_for_trigger()
        input_handler.simulate_input(pages)
        logger.info("所有内容输入完成")

    except FileNotFoundError:
        logger.error(f"输入文件不存在: {args.input}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"发生未预期错误: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main("inputs/input2.txt")
