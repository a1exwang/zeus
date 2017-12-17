# zeus
Third-party Thunder 9 Client Manager API on Windows.


## Getting started
- Install Python3.6 on Windows
- Install pywin32 https://sourceforge.net/projects/pywin32/
- Install win32gui with PyPI
- Install Thunder on Windows, change Thunder install directory in thunder.py
- Start a new task with thunder and try to get the coordinates of the "Start Task" button
- Start with python3 api.py
- Use `requests.post("http://xxx/tasks", json={"url": url})` to start a task


## TODOs
- Parse Thunder sqlite3 file to get downloading status
