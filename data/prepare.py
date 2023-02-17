import json


with open('qadata.json', 'r') as f, open('qadata1.txt', 'w') as g:
    for line in f:
        jr = json.loads(line.strip())
        q = jr['question'].strip()
        a = jr['answer'].replace("\n", '').strip()
        if len(a) > 10:
            g.write(q + '\n')
        elif len(a) > 0:
            g.write(q)
        g.write(a + '\n')
        g.write('\n')