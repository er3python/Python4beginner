import re
import os

h1 = "# "
h2 = "## "
h3 = "### "
p = re.compile("\[(.*)\]")

start_count_keyword = False
keyword_cnt = 0
keywords = []

with open("./README.md", encoding='utf-8') as f:
    new_lines = []
    for line in f:
        if line.startswith(h2):
            content = line.strip()[len(h2):]
            if content == "知识点":
                start_count_keyword = True

        if start_count_keyword:
            if line.startswith(h3):
                content = line.strip()[len(h3):]
                val = p.findall(line)
                keyword_cnt += 1
                keywords.append(content)
                if not content.startswith('['):
                    path = f"./keywords/{content}.md"
                    if not os.path.exists(path):
                        with open(path, 'w', encoding='utf-8') as _:
                            line = f"{h3}[{content}]({path})\n"
                            print(line)
                            pass
        new_lines.append(line)

    with open("README.tmp", 'w', encoding='utf-8') as output:
        output.writelines(new_lines)

print("Total keywords count: ", keyword_cnt)

os.remove("./README.md")
os.rename("./README.tmp", "./README.md")