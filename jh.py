# A number indicates a confirmed depth
uniques = [["Exosuit",6],
           ["Shadowcloak",4],
           ["Cybersuit",5],
           ["Fiend crown",4],
           ["Overlord"],
           ["Thompson",4],
           ["Hammerhead",5],
           ["Avalanche",6],
           ["Vengeance",4],
           ["Scrapgun",4],
           ["Apocalypse",6],
           ["BFT 10k"],
           ["Shadowhunter"],
           ["Firestorm",4],
           ["Calamity",5],
           ["Hate",4],
           ["Death",5],
           ["Love",4],
           ["Bloodletter",5],
           ["Executioner",4],
           ["Wavesplitter"],
           ["Soulstealer"],
           ["Monster",4],
           ["Denial",5],
           ["Carnage",4],
           ["Twin viper"],
           ["Void",4],
           ["Firecrown"],
           ["Vulcan"],
           ["Wavedancer"]]

# You can manually add new paths here
additional_paths = [["URR","Europa portal"],
                    ["RRUU","Io portal"]]

codes = ["U","R","D","L"]
default_length=7

# generate the prefix tree (recursive function)
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

# transform the name into URDL sequence
def name2seq(u,length):
    u=u.lower().strip().replace(" ", "")[:length]
    prev=(ord(u.lower().strip()[0])-ord('a'))//7
    out=[codes[prev]]
    for letter in u.lower().strip()[1:]:
        prev=(prev+(ord(letter)-ord('a'))//9+3)%4
        out.append(codes[prev])
    return out

# export to graphviz format
def export(dic):
    if dic.get("here") is None:
        print(str(id(dic))+" [shape=point, label=\"\"]")
    for k,v in dic.items():
        if k=="here":
            if len(v)==1:
                v=v[0]
            if str(v).endswith("portal"):
                print(str(id(dic))+" [shape=box, label=\""+str(v)+"\"]")
            else:
                print(str(id(dic))+" [label=\""+str(v)+"\"]")
        else:
            print(str(id(dic))+" -> "+str(id(v))+" [label=\""+k+"\"]")
            export(v)

dic = {}
for u in uniques:
    name = u[0] if len(u)>1 else u[0]+"\nUNCONFIRMED"
    length = u[1] if len(u)>1 else default_length
    add(dic, name2seq(name,length), name)

for p in additional_paths:
    add(dic,list(p[0]),p[1])

print("digraph {")
print("label=\"Jupiter Hell Purgatory Map\"")
export(dic)
print(str(id(dic))+" [shape=pentagon label=\"START\"]")
print("}")
