
text = """  """


with open("otus.txt", "w", encoding='utf-8') as f:
    a = text.replace(' , ', ',').replace(' - ','-').replace('\n\n', '')
    f.write(a)

