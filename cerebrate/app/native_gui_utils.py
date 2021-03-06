import asyncio
import contextlib
import os
import sys
import tkinter
import tkinter.filedialog

from typing import Optional, Generator, Tuple, List


def _cross_platform_file_types() -> List[Tuple[str, str]]:
    if sys.platform == "win32":
        return [
            ("Scelight", "*.exe"),
        ]
    elif sys.platform == "darwin":
        return [
            ("Scelight", "*.command"),
        ]
    else:
        return [
            ("Scelight", "*.sh"),
        ]


@contextlib.contextmanager
def _make_root_window_for_dialog(
    title: str,
) -> Generator[tkinter.Tk, None, None]:
    root = tkinter.Tk()
    root.withdraw()
    root.title(title)
    root.iconbitmap("static/app-icon.ico")
    root.overrideredirect(True)
    root.geometry("0x0+0+0")
    root.attributes("-alpha", 0)
    root.lift()
    root.focus_force()
    root.deiconify()

    yield root

    root.destroy()


async def open_directory_picker(title: str = None) -> Optional[str]:
    if title is None:
        title = "Select directory"

    def ask_directory():
        with _make_root_window_for_dialog(title) as root:
            directory = tkinter.filedialog.askdirectory(
                parent=root, title=title, mustexist=True
            )
        return os.path.normpath(directory) if directory else None

    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, ask_directory)


async def open_file_picker(title: str = None) -> Optional[str]:
    if title is None:
        title = "Select file"

    def ask_file():
        with _make_root_window_for_dialog(title) as root:
            filename = tkinter.filedialog.askopenfilename(
                parent=root,
                title=title,
                filetypes=_cross_platform_file_types(),
            )
        return os.path.normpath(filename) if filename else None

    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, ask_file)
