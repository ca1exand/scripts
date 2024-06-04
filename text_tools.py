import re

# insert file name here
fn='filename.txt'

# insert stop word file name here
stopwords='stopwords.txt'

def sentences_from_text(text):
    s1=re.split('(\. |\! |\?)',text)
    if (len(s1)%2!=0):
        s1.append("")
    r=[]
    for i in range(0,len(s1),2):
        if (s1[i+1].strip()=='!'):
            continue
        r.append(s1[i]+s1[i+1])
    return r

def parse_text(filename):
    with open(filename) as f:
        contents=f.read()
        prepped_text=prepare_text(contents)
        sentences=sentences_from_text(prepped_text)
        print('parsed text with ',len(sentences),' sentences')
        return sentences

def load_stopwords(filename):
    stopwords=[]
    with open(filename, encoding='utf8') as f:
        for line in f:
            sw=line.strip().lower()
            stopwords.append(sw)
    return stopwords

def sentences_matching():
    sws=load_stopwords(stopwords)
    candidates=[]
    sentences=parse_text(fn)
    for s in sentences:
        t=False
        for sw in sws:
            if sw in s:
                t=True
                break
        if not t:
            candidates.append(s)
    print(len(candidates)+"unsuscpicious sentences")
    return(candidates)

