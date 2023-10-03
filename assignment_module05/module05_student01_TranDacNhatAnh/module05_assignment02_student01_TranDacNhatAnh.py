'''
Markdown file: additionalFolder\student01_TranDacNhatAnh.md
'''
import markdown as md

with open('additionalFolder\student01_TranDacNhatAnh.md', 'r') as mdfile:
    writtenLines = mdfile.read()
htmlLines = md.markdown(writtenLines)
with open('additionalFolder\sample.html', 'w') as htmls:
    htmls.write(htmlLines)

# Learned from https://www.honeybadger.io/blog/python-markdown/