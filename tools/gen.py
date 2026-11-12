import random, json, math
R = random.Random(20261112)

def nz(x, pct=False):
    """show a clean number as a noisy decimal"""
    if pct:
        d = R.choice([-0.03,-0.02,-0.01,0.01,0.02,0.03])
    elif x < 100:
        d = R.choice([-0.04,-0.03,-0.02,-0.01,0.01,0.02,0.03,0.04])
    elif x < 1000:
        d = R.choice([-0.11,-0.08,-0.03,-0.02,0.02,0.03,0.07,0.12])
    else:
        d = R.choice([-0.3,-0.2,-0.1,0.1,0.2,0.3])
    v = x + d
    return v, ("%.2f" % v)

def opts_num(ans, step):
    for _ in range(50):
        pos = R.randrange(5)
        o = [ans + (i-pos)*step for i in range(5)]
        if min(o) > 0: break
    return [str(x) for x in o], pos

def step_for(ans):
    return 10 if ans < 200 else (20 if ans < 1000 else 50)

PCT = [15,20,25,30,35,40,45,60,65,75,80,12,18,24,36]
SQ = [n*n for n in range(11,31)]
CU = [n**3 for n in range(4,13)]

def t1():
    p=R.choice(PCT); N=R.choice([200,300,400,500,600,800,900,1200,1500,1800]); a=R.randint(12,28); b=R.randint(11,19)
    ans=p*N//100 + a*b
    pv,ps=nz(p,True); Nv,Ns=nz(N); av,as_=nz(a); bv,bs=nz(b)
    return f"{ps}% of {Ns} + {as_} × {bs} = ?", pv*Nv/100+av*bv, ans, f"{p}% of {N} = {p*N//100}. {a} × {b} = {a*b}. Sum = {ans}."
def t2():
    S=R.choice(SQ); r=int(math.isqrt(S)); a=R.randint(6,15); d=R.choice([4,5,8,12,15]); q=R.randint(12,45); N=d*q
    ans=r*a+q
    Sv,Ss=nz(S); av,as_=nz(a); Nv,Ns=nz(N); dv,ds=nz(d)
    return f"√{Ss} × {as_} + {Ns} ÷ {ds} = ?", math.sqrt(Sv)*av+Nv/dv, ans, f"√{S} = {r}. {r} × {a} = {r*a}. {N} ÷ {d} = {q}. Sum = {ans}."
def t3():
    a=R.randint(16,29); p=R.choice([15,20,25,30,40]); N=R.choice([400,600,800,1000,1200])
    while a*a - p*N//100 < 40: a+=3
    ans=a*a-p*N//100
    av,as_=nz(a); pv,ps=nz(p,True); Nv,Ns=nz(N)
    return f"({as_})² − {ps}% of {Ns} = ?", av*av-pv*Nv/100, ans, f"{a}² = {a*a}. {p}% of {N} = {p*N//100}. Difference = {ans}."
def t4():
    C=R.choice(CU); r=round(C**(1/3)); a=R.randint(12,25); b=R.randint(11,18); c=R.randint(6,14); d=R.randint(40,160)
    ans=r*a+b*c-d
    Cv,Cs=nz(C); av,as_=nz(a); bv,bs=nz(b); cv,cs=nz(c); dv,ds=nz(d)
    return f"∛{Cs} × {as_} + {bs} × {cs} − {ds} = ?", Cv**(1/3)*av+bv*cv-dv, ans, f"∛{C} = {r}. {r} × {a} = {r*a}. {b} × {c} = {b*c}. {r*a} + {b*c} − {d} = {ans}."
def t5():
    p=R.choice([20,25,40,60,75]); a=R.choice([4,5,6,8]); k=R.randint(6,20); N=a*k*100//p
    while N*p % 100 or (N*p//100) % a: k+=1; N=a*k*100//p
    b=R.randint(12,24)
    ans=(N*p//100)//a + b*b
    pv,ps=nz(p,True); Nv,Ns=nz(N); av,as_=nz(a); bv,bs=nz(b)
    return f"{ps}% of {Ns} ÷ {as_} + ({bs})² = ?", pv*Nv/100/av+bv*bv, ans, f"{p}% of {N} = {N*p//100}. ÷ {a} = {(N*p//100)//a}. {b}² = {b*b}. Sum = {ans}."
def t6():
    c=R.choice([4,6,8,12]); a=c*R.randint(3,9); b=R.randint(12,25); p=R.choice(PCT[:10]); N=R.choice([400,600,800,1200,1600])
    ans=a*b//c + p*N//100
    av,as_=nz(a); bv,bs=nz(b); cv,cs=nz(c); pv,ps=nz(p,True); Nv,Ns=nz(N)
    return f"({as_} × {bs}) ÷ {cs} + {ps}% of {Ns} = ?", av*bv/cv+pv*Nv/100, ans, f"{a} × {b} ÷ {c} = {a*b//c}. {p}% of {N} = {p*N//100}. Sum = {ans}."
def t7():
    p=R.choice([20,25,40,50,75]); x=R.choice([240,320,400,480,560,640,800,960]); a=R.randint(60,240)
    while x*p%100: x+=20
    b=x*p//100+a
    _,ps=nz(p,True); _,as_=nz(a); _,bs=nz(b)
    return f"{ps}% of ? + {as_} = {bs}", None, x, f"{p}% of ? = {b} − {a} = {b-a}. So ? = {b-a} × 100 ÷ {p} = {x}."
def t8():
    x=R.randint(12,26); a=R.randint(14,28); b=R.randint(15,26)
    k=a*b-x*x
    while k<=20: a+=2; k=a*b-x*x
    _,ks=nz(k); _,as_=nz(a); _,bs=nz(b)
    return f"(?)² + {ks} = {as_} × {bs}", None, x, f"{a} × {b} = {a*b}. {a*b} − {k} = {x*x}. So ? = √{x*x} = {x}."
def t9():
    d=R.choice([6,8,12,15,16]); q=R.randint(15,40); N=d*q; a=R.randint(7,14); S=R.choice(SQ); r=math.isqrt(S); b=R.randint(4,9)
    while q*a-r*b<30: a+=2
    ans=q*a-r*b
    Nv,Ns=nz(N); dv,ds=nz(d); av,as_=nz(a); Sv,Ss=nz(S); bv,bs=nz(b)
    return f"{Ns} ÷ {ds} × {as_} − √{Ss} × {bs} = ?", Nv/dv*av-math.sqrt(Sv)*bv, ans, f"{N} ÷ {d} = {q}. {q} × {a} = {q*a}. √{S} × {b} = {r*b}. Difference = {ans}."
def t10():
    num,den=R.choice([(3,8),(5,8),(2,5),(3,5),(5,6),(4,9),(7,12)]); N=den*R.randint(40,110); p=R.choice([20,25,40,60]); M=R.choice([350,450,550,650,750,850]) if p%20==0 else R.choice([400,600,800])
    while M*p%100: M+=50
    ans=N*num//den + M*p//100
    Nv,Ns=nz(N); pv,ps=nz(p,True); Mv,Ms=nz(M)
    return f"{num}/{den} of {Ns} + {ps}% of {Ms} = ?", Nv*num/den+pv*Mv/100, ans, f"{num}/{den} of {N} = {N*num//den}. {p}% of {M} = {M*p//100}. Sum = {ans}."

quant=[]
T=[t1,t2,t3,t4,t5,t6,t7,t8,t9,t10]
seen=set()
while len(quant)<50:
    f=T[len(quant)%10]
    text,exact,ans,ex=f()
    if text in seen: continue
    step = (2 if f is t8 else (40 if f is t7 else step_for(ans)))
    if exact is not None and abs(exact-ans) >= step*0.3: continue
    o,pos=opts_num(ans,step)
    seen.add(text)
    quant.append(dict(t="Approximation", q="What approximate value should come in place of the question mark (?)\n"+text, o=o, a=pos, e=ex))

# ---------- Reasoning ----------
V={'North':(0,1),'East':(1,0),'South':(0,-1),'West':(-1,0)}
CW=['North','East','South','West']
D8=['North','North-East','East','South-East','South','South-West','West','North-West']
def dname(dx,dy):
    if dx==0 and dy==0: return None
    ns='North' if dy>0 else ('South' if dy<0 else '')
    ew='East' if dx>0 else ('West' if dx<0 else '')
    return ns+('-' if ns and ew else '')+ew
def opp(d): return D8[(D8.index(d)+4)%8]
NAMES=['Ravi','Meena','Arjun','Kavita','Suresh','Pooja','Imran','Neha','Vikram','Anita','Rohan','Divya','Farhan','Sneha','Manoj','Tanvi','Gaurav','Ritu']

def path_q(i):
    while True:
        name=NAMES[i%len(NAMES)]; he='he' if i%2==0 else 'she'
        f=R.choice(CW); n=R.choice([3,4,4,5]); x=y=0; parts=[]; cur=f
        start=R.choice(['his house','the office','point A','a bus stop','the bank','a temple']) if he=='he' else R.choice(['her house','the office','point A','a bus stop','the bank','a school'])
        for k in range(n):
            L=R.choice([3,4,5,6,7,8,9,10,12,14,15,16,18,20,24])
            if k==0: parts.append(f"{name} starts from {start} and walks {L} m towards the {cur.lower()}")
            else:
                tr=R.choice(['left','right'])
                cur=CW[(CW.index(cur)+(1 if tr=='right' else -1))%4]
                parts.append(f"turns {tr} and walks {L} m")
            x+=V[cur][0]*L; y+=V[cur][1]*L
        d2=x*x+y*y; d=math.isqrt(d2)
        if d*d!=d2 or d==0: continue
        if x!=0 and y!=0 and R.random()<0.0: continue
        dr=dname(x,y)
        text=parts[0]+". Then "+he+" "+", ".join(parts[1:-1]+["and finally "+parts[-1]] if n>2 else parts[1:])+"."
        text=text.replace("Then "+he+" and finally","Then "+he)
        rev = (i%4==3)
        if rev:
            qn=f"{text} In which direction is the starting point with respect to {name}'s final position, and how far?"
            cd=opp(dr); ex=f"Net movement: {abs(x)} m {'east' if x>0 else 'west'} and {abs(y)} m {'north' if y>0 else 'south'}. Final position is {d} m {dr} of start, so the start is {d} m to the {cd} of the final position."
        else:
            qn=f"{text} How far and in which direction is {name} now from the starting point?"
            cd=dr; ex=f"Net movement: {abs(x)} m {'east' if x>0 else 'west'} and {abs(y)} m {'north' if y>0 else 'south'}. Distance = √({x*x} + {y*y}) = {d} m, direction {dr}."
        ex=ex.replace("0 m east and ","").replace("0 m west and ","").replace(" and 0 m north","").replace(" and 0 m south","")
        cands=[(d,opp(cd)),(d+R.choice([2,3,5]),cd),(abs(x)+abs(y),cd),(d,D8[(D8.index(cd)+2)%8]),(max(1,d-R.choice([1,2,4])),opp(cd)),(d+7,D8[(D8.index(cd)+6)%8])]
        o=[f"{d} m, {cd}"]
        for dd,dn in cands:
            s=f"{dd} m, {dn}"
            if s not in o and len(o)<5: o.append(s)
        if len(o)<5: continue
        return dict(t="Direction: distance and path", q=qn, o=o, a=0, e=ex)

def turn_q(i):
    f=R.choice(D8); idx=D8.index(f); parts=[]; steps=[]
    for k in range(R.choice([3,4])):
        deg=R.choice([45,90,90,135,180,225,270]); cw=R.random()<0.5
        idx=(idx+(deg//45)*(1 if cw else -1))%8
        parts.append(f"{deg}° {'clockwise' if cw else 'anticlockwise'}"); steps.append(D8[idx])
    who=R.choice(['A man','A woman','A clock tower guard','A cyclist','A traffic policeman'])
    qn=f"{who} is facing {f}. The person turns {', then '.join(parts)}. Which direction is the person facing now?"
    ex=f"Start {f} → "+" → ".join(steps)+"."
    ans=D8[idx]; others=[d for d in D8 if d!=ans]; R.shuffle(others)
    return dict(t="Direction: turns", q=qn, o=[ans]+others[:4], a=0, e=ex)

def shadow_q(i):
    morning = i%2==0; left = (i//2)%2==0; other = i%4 in (1,2)
    S='West' if morning else 'East'
    facing=CW[(CW.index(S)+(1 if left else -1))%4]
    a,b=[('Amit','Bhanu'),('Rekha','Sunil'),('Kiran','Lata'),('Deepak','Farah')][i%4]
    when='One morning just after sunrise' if morning else 'One evening just before sunset'
    qn=f"{when}, {a} and {b} were standing face to face. {a}'s shadow fell exactly to {a}'s {'left' if left else 'right'}. Which direction was {b if other else a} facing?"
    ans=opp(facing) if other else facing
    ex=f"{'Morning: sun in the east, shadow falls west.' if morning else 'Evening: sun in the west, shadow falls east.'} {a}'s {'left' if left else 'right'} is {S.lower()}, so {a} faces {facing.lower()}."+(f" {b} is opposite, so {b} faces {ans.lower()}." if other else "")
    others=[d for d in ['North','South','East','West','North-East','South-West'] if d!=ans]
    return dict(t="Direction: shadow", q=qn, o=[ans]+others[:4], a=0, e=ex)

def para_set(si):
    labels=[list('PQRSTU'),list('ABCDEF'),list('JKLMNO'),list('GHWXYZ'),list('DEFGHK')][si]
    while True:
        pts={labels[0]:(0,0)}; st=[]
        prev=labels[0]; lastdir=None
        for L in labels[1:]:
            while True:
                dr=R.choice(CW)
                if lastdir and dr==CW[(CW.index(lastdir)+2)%4]: continue
                break
            k=R.choice([3,4,5,6,8,9,10,12,15,16,7,24,20])
            px,py=pts[prev]; pts[L]=(px+V[dr][0]*k,py+V[dr][1]*k)
            st.append((L,k,dr,prev)); prev=L; lastdir=dr
        if len(set(pts.values()))<6 or len(set(x[2] for x in st))<3: continue
        pairs=[(a,b) for ia,a in enumerate(labels) for ib,b in enumerate(labels) if ib>ia+1]
        trip=[]
        for a,b in pairs:
            dx=pts[a][0]-pts[b][0]; dy=pts[a][1]-pts[b][1]; d2=dx*dx+dy*dy; d=math.isqrt(d2)
            if d*d==d2 and dx and dy: trip.append((a,b,d,dx,dy))
        if not trip: continue
        break
    forms=["Point {L} is {k} m to the {d} of point {p}.","Point {L} is {k} m {d} of point {p}."]
    ctx=" ".join(forms[j%2].format(L=L,k=k,d=dr.lower(),p=p) for j,(L,k,dr,p) in enumerate(st))
    R.shuffle(st)  # not used further
    qs=[]
    def diro(ans):
        others=[d for d in D8 if d!=ans]; R.shuffle(others); return [ans]+others[:4]
    a,b,d,dx,dy=R.choice(trip)
    cs=[d+1,d+3,abs(dx)+abs(dy),max(2,d-2),d+5,d+8]
    o=[f"{d} m"]
    for c in cs:
        if f"{c} m" not in o and len(o)<5: o.append(f"{c} m")
    qs.append(dict(q=f"What is the shortest distance between point {a} and point {b}?", o=o, a=0, e=f"{a} is {abs(dx)} m {'east' if dx>0 else 'west'} and {abs(dy)} m {'north' if dy>0 else 'south'} of {b}. Distance = √({dx*dx} + {dy*dy}) = {d} m."))
    used={(a,b)}
    cand=[p for p in pairs if p not in used]; R.shuffle(cand)
    for (a,b) in cand[:2]:
        if R.random()<0.5: a,b=b,a
        dx=pts[a][0]-pts[b][0]; dy=pts[a][1]-pts[b][1]; ans=dname(dx,dy)
        desc=", ".join(x for x in [f"{abs(dx)} m {'east' if dx>0 else 'west'}" if dx else "", f"{abs(dy)} m {'north' if dy>0 else 'south'}" if dy else ""] if x)
        qs.append(dict(q=f"In which direction is point {a} with respect to point {b}?", o=diro(ans), a=0, e=f"{a} is {desc} of {b}, so {a} is to the {ans} of {b}."))
    while True:
        last=labels[-1]; dr=R.choice(CW); k=R.choice([5,6,8,10,12])
        vx=pts[last][0]+V[dr][0]*k; vy=pts[last][1]+V[dr][1]*k; tgt=R.choice(labels[:4])
        dx=vx-pts[tgt][0]; dy=vy-pts[tgt][1]
        if (vx,vy) in pts.values() or (dx==0 and dy==0): continue
        break
    ans=dname(dx,dy)
    desc=", ".join(x for x in [f"{abs(dx)} m {'east' if dx>0 else 'west'}" if dx else "", f"{abs(dy)} m {'north' if dy>0 else 'south'}" if dy else ""] if x)
    qs.append(dict(q=f"If point V is {k} m to the {dr.lower()} of point {last}, then in which direction is point V with respect to point {tgt}?", o=diro(ans), a=0, e=f"V is {desc} of {tgt}, so V is to the {ans} of {tgt}."))
    for q in qs:
        q['t']="Direction: paragraph based"; q['ctx']="Study the information carefully and answer the questions.\n"+ctx
    return qs

reason=[]
for s in range(5): reason+=para_set(s)
for i in range(18): reason.append(path_q(i))
for i in range(8): reason.append(turn_q(i))
for i in range(4): reason.append(shadow_q(i))

def shuffle_opts(q):
    correct=q['o'][q['a']]; o=q['o'][:]; R.shuffle(o); q['o']=o; q['a']=o.index(correct)
for q in reason: shuffle_opts(q)
assert len(quant)==50 and len(reason)==50
for q in quant+reason: assert len(set(q['o']))==5, q
json.dump(quant,open('quant.json','w'),ensure_ascii=False)
json.dump(reason,open('reasoning.json','w'),ensure_ascii=False)
for q in quant[:10]+reason[:4]+reason[20:23]+reason[38:40]+reason[46:48]:
    print(q.get('ctx','')); print(q['q']); print(q['o'], '->', q['o'][q['a']]); print(q['e']); print()
