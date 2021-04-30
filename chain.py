def gch(n,ex='infinity',lim=50):
    nms=[]
    x=int(n)
    tmr=0
    inf=False
    while x!=0:
        x=x-((abs(x)/x)*(int(str(x)[::-1].strip('-').strip('.0'))))
        tmr+=1
        nms.append(x)
        if len(nms) >= 3:
            if str(abs(nms[tmr-1])).strip('.0') == str(abs(nms[tmr-3]))[::-1].strip('.0'):
                inf=True
                break
        if tmr==lim:
            inf=True
            break
    if inf==False:
        return tmr
    else:
        return ex

def fspt(n,lim=13):
    x=int(n)
    tmr=0
    inf=False
    while x!=0:
        x=x-((abs(x)/x)*(int(str(x)[::-1].strip('-').strip('.0'))))
        print(x,end=' ')
        tmr+=1
        if tmr==lim:
            break
    print(' ')
    
def allgch(a,b):
    for i in range(a,b+1):
        t=gch(i)
        if t!='infinity':
            print(i,t,'-'*t+'#')
        else:
            print(i,t)
