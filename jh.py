uniques = [["exosuit",6],
           ["shadowcloak"],
           ["cybersuit",5],
           ["fiend crown"],
           ["overlord"],
           ["thompson"],
           ["hammerhead",5],
           ["avalanche"],
           ["vengeance"],
           ["scrapgun"],
           ["apocalypse",6],
           ["bft10k"],
           ["shadowhunter"],
           ["firestrom"],
           ["calamity",5],
           ["hate"],
           ["death",5],
           ["love"],
           ["bloodletter",5],
           ["executioner"],
           ["wavesplitter"],
           ["soulstealer"],
           ["monster"],
           ["denial",5],
           ["carnage"],
           ["twin viper"],
           ["void"],
           ["firecrown"],
           ["vulcan"],
           ["wavedancer"]]
codes = ["U","R","D","L"]

default_length=4

def add(dic, seq, name):
    if len(seq)==0:
        if dic.get("here")==None:
            dic["here"]=[]
        dic["here"].append(name)
    else:
        nextdic = dic.get(seq[0])
        if nextdic is None:
            nextdic={}
            dic[seq[0]]=nextdic
        add(nextdic, seq[1:], name)

def name2seq(u):
    prev=(ord(u.lower().strip()[0])-ord('a'))//7
    out=[codes[prev]]
    for letter in u.lower().strip()[1:]:
        prev=(prev+(ord(letter)-ord('a'))//9+3)%4
        out.append(codes[prev])
    return out

def export(dic):
    for k,v in dic.items():
        if k=="here":
            print(str(id(dic))+" [label=\""+str(v)+"\"]")
        else:
            if dic.get("here") is None:
                print(str(id(dic))+" [label=\"\"]")
            print(str(id(dic))+" -> "+str(id(v))+" [label=\""+k+"\"]")
            export(v)

dic = {}
for u in uniques:
    name = u[0]
    length = u[1] if len(u)>1 else default_length
    add(dic, name2seq(name[:length]), name)
add(dic,["U","R","R"],"europa")
add(dic,["R","R","U","U"],"io")

print("digraph {")
export(dic)
print("}")
