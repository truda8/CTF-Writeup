# -*- coding: UTF-8 -*-
import os
from urllib import parse

black_list = [
    ".git",
    "_book",
    "node_modules",
    "styles"
]

print("正在生成 SUMMARY.md ...")

SUMMARY = "# SUMMARY"

def get_dirs(file_dir):
    for _, dirs, _ in os.walk(file_dir):
        return dirs

for dir in  get_dirs("./"):
    if dir not in black_list:
        SUMMARY += "\n\n* [%s](/%s)\n" % (dir, dir)
        items = []
        for file_name in os.listdir(dir):
            if file_name[0] == ".":
                continue  # 跳过隐藏文件
            file_path = os.path.join(dir, file_name)
            with open(file_path, encoding="utf-8") as f:
                content = f.readlines().remove("\n")
            if content:
                title = content[0][2:]
            else:
                title = file_name[:-3]

            file_path = "/%s/%s" % (dir, file_name)
            file_path = parse.quote(file_path)

            item = "    * [%s](%s)" % (title, file_path)
            items.append(item)
        SUMMARY += "\n".join(items)

with open("./SUMMARY.md", "w+", encoding="utf-8") as f:
    f.write(SUMMARY)
print("生成 SUMMARY.md 成功！")
