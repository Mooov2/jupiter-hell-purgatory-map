uniques = [["exosuit",6],
           ["shadowcloak",4],
           ["cybersuit",5],
           ["fiend crown",4],
           ["overlord"],
           ["thompson",4],
           ["hammerhead",5],
           ["avalanche"],
           ["vengeance",4],
           ["scrapgun",4],
           ["apocalypse",6],
           ["bft10k"],
           ["shadowhunter"],
           ["firestorm",4],
           ["calamity",5],
           ["hate",4],
           ["death",5],
           ["love",4],
           ["bloodletter",5],
           ["executioner",4],
           ["wavesplitter"],
           ["soulstealer"],
           ["monster",4],
           ["denial",5],
           ["carnage",4],
           ["twin viper"],
           ["void",4],
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
    if dic.get("here") is None:
        print(str(id(dic))+" [label=\"\"]")
    for k,v in dic.items():
        if k=="here":
            print(str(id(dic))+" [label=\""+str(v)+"\"]")
        else:
            print(str(id(dic))+" -> "+str(id(v))+" [label=\""+k+"\"]")
            export(v)

dic = {}
for u in uniques:
    name = u[0] if len(u)>1 else u[0]+" UNCONFIRMED"
    length = u[1] if len(u)>1 else default_length
    add(dic, name2seq(name[:length]), name)
add(dic,["U","R","R"],"EUROPA")
add(dic,["R","R","U","U"],"IO")

print("digraph {")
export(dic)
print("}")
