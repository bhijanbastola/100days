import re
string="A sentence is a group of words that gives a complete thought. It usually has a subject and a verb, starts with a big letter, and ends with a mark Like a dot or a question mark. In law, A sentence also means the punishment a judge gives to a guilty person"

pattern=r"[A-Z]"

match=re.findall(pattern,string)
repl="replced"
replace=re.sub(pattern,repl,string,count=0)

if match:
    res=match.count
    print(res)

if replace:
    print(replace)


#split