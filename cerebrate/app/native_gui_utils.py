import asyncio
import functools
import os
import tkinter
import tkinter.filedialog

from typing import Optional


async def open_directory_picker(title: str = None) -> Optional[str]:
    if title is None:
        title = "Select directory"

    def ask_directory():
        root = tkinter.Tk()
        root.withdraw()
        root.overrideredirect(True)
        root.geometry('0x0+0+0')
        root.attributes("-alpha", 0)
        root.lift()
        root.focus_force()
        root.deiconify()

        directory = tkinter.filedialog.askdirectory(parent=root, title=title, mustexist=True)
        root.destroy()

        return os.path.normpath(directory) if directory else None

    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, ask_directory)
