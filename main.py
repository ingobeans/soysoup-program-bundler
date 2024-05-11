import os, json, pyperclip

base = {"type":"directory","content":{"soysoup":{"type":"directory","content":{}},"home":{"type":"directory","content":{"downloads":{"type":"directory","content":{}},"documents":{"type":"directory","content":{}},"programs":{"type":"directory","content":{}}}}}}

programs = os.listdir("programs")

for program in programs:
    with open(f"programs/{program}","r",encoding="utf-8") as f:
        data = f.read()

    base["content"]["soysoup"]["content"][program.removesuffix(".js") + ".soup"] = {"type":"file","content":data}

print(repr(json.dumps(base)))
pyperclip.copy(repr(json.dumps(base)))