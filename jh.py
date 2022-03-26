# A number indicates a confirmed depth
uniques = [["Exosuit",6],
           ["Shadowcloak",4],
           ["Cybersuit",5],
           ["Fiend crown",4],
           ["Overlord",5],
           ["Thompson",4],
           ["Hammerhead",5],
           ["Avalanche",6],
           ["Vengeance",4],
           ["Scrapgun",4],
           ["Apocalypse",6],
           ["BFG Ten",6],
           ["Shadowhunter",9],
           ["Firestorm",4],
           ["Calamity",5],
           ["Hate",4],
           ["Death",5],
           ["Love",4],
           ["Bloodletter",5],
           ["Executioner",4],
           ["Wavesplitter",5],
           ["Soulstealer [Bug?]",6],
           ["Monster",4],
           ["Denial",5],
           ["Carnage",4],
           ["Viper",5],
           ["Void",4],
           ["Firecrown",6],
           ["Vulcan [Bug?]",5],
           ["Wavedancer",6]]

# You can manually add new paths here
additional_paths = [["URR","Europa portal"],
                    ["RRUU","Io portal"],
                    ["ULLDRURRUUULDLLU","Final boss portal"],
                    ["ULLUL","Dante portal [Bug?]"]]

codes = ["U","R","D","L"]
# default_length=10
condensed=True

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
def export(prefix,previous_dic,dic):
    if condensed and len(dic)==1 and dic.get("here") is None:
        for k,v in dic.items():
            export(prefix+k,previous_dic,v)
    else:
        if dic.get("here") is None:
            print(str(id(dic))+" [shape=point, label=\"\"]")
        if prefix!="":
            print(str(id(previous_dic))+" -> "+str(id(dic))+" [label=\""+prefix+"\"]")
        for k,v in dic.items():
            if k=="here":
                if len(v)==1:
                    v=v[0]
                if "portal" in str(v):
                    print(str(id(dic))+" [shape=box, label=\""+str(v)+"\"]")
                else:
                    print(str(id(dic))+" [label=\""+str(v)+"\"]")
            else:
                export(k,dic,v)

dic = {}
for u in uniques:
    name = u[0] # if len(u)>1 else u[0]+"\nUNCONFIRMED"
    length = u[1] # if len(u)>1 else default_length
    add(dic, name2seq(u[0],length), name)

for p in additional_paths:
    add(dic,list(p[0]),p[1])

print("digraph {")
print("label=\"Jupiter Hell Purgatory Map\"")
export("",dic,dic)
print(str(id(dic))+" [shape=pentagon label=\"Purgatory\"]")
print("}")
