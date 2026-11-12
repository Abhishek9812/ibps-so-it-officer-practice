import json, random
R=random.Random(7)
PIN=("None of","All of","Both ","No correction","No error","No dependency")
def parse(fn):
    out=[]; ctx=None
    for ln in open(fn,encoding='utf8'):
        ln=ln.rstrip('\n')
        if not ln.strip(): continue
        if ln.startswith('@@'):
            ctx=ln[2:].strip().replace('\\n','\n') or None; continue
        p=[x.strip() for x in ln.split(' | ')]
        if ln.startswith('!'):
            assert len(p)==9,(fn,ln)
            q=dict(t=p[0][1:],q=p[1],o=p[2:7],a=int(p[7])-1,e=p[8])
        else:
            assert len(p)==8,(fn,ln,len(p))
            correct=p[2]; opts=p[2:7]
            pinned=[o for o in opts if o.startswith(PIN)]
            free=[o for o in opts if o not in pinned]; R.shuffle(free)
            o=free+pinned
            q=dict(t=p[0],q=p[1],o=o,a=o.index(correct),e=p[7])
        assert len(set(q['o']))==5,(fn,ln)
        assert 0<=q['a']<5
        if ctx and q['t'] in('Sentence rearrangement','Reading comprehension','Cloze test'): q['ctx']=ctx
        out.append(q)
    assert len(out)==50,(fn,len(out))
    return out
secs=[
 dict(id='pk',name='Professional Knowledge',short='PK',marks=1,secs=2250,syllabus='DBMS keys, functional dependencies, normalization',qs=parse('pk.txt')),
 dict(id='lr',name='Reasoning',short='LR',marks=1,secs=2250,syllabus='Direction sense: paths, turns, shadows, paragraph sets',qs=json.load(open('reasoning.json'))),
 dict(id='qa',name='Quantitative Aptitude',short='QA',marks=1,secs=2250,syllabus='Approximation',qs=json.load(open('quant.json'))),
 dict(id='el',name='English Language',short='EL',marks=0.5,secs=2250,syllabus='Error detection, fill in the blanks, rearrangement, RC, cloze',qs=parse('en.txt')),
 dict(id='fa',name='Financial Awareness',short='FA',marks=1,secs=1125,syllabus='RBI and monetary policy',qs=parse('fa.txt')),
 dict(id='ck',name='Computer Knowledge',short='CK',marks=0.5,secs=1125,syllabus='Fundamentals, memory, networking, MS Office, security',qs=parse('ck.txt')),
]
test=dict(id='day1',title='Day 1 Practice Set',date='2026-11-12',negative=0.25,sections=secs)
json.dump(test,open('../tests/day1.json','w'),ensure_ascii=False)
idx=dict(exam='IBPS RRB Officer Scale II (IT)',examDate='2026-12-20',tests=[dict(id='day1',title='Day 1 Practice Set',date='2026-11-12',file='tests/day1.json',note='Approximation, direction sense, RBI and monetary policy, DBMS keys and normalization, plus English and computer basics',sections=[dict(id=s['id'],name=s['name'],short=s['short'],n=len(s['qs']),marks=s['marks'],secs=s['secs'],syllabus=s['syllabus']) for s in secs])])
json.dump(idx,open('../tests/index.json','w'),ensure_ascii=False)
from collections import Counter
for s in secs: print(s['id'],len(s['qs']),Counter(q['a'] for q in s['qs']))
