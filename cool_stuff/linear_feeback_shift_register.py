# prof. edmund weitz 
# weihnachtsvorlesung 2021
# https://www.youtube.com/watch?v=YIkqZsz4faA

def LFSR(n,taps):
  state = 1<<(n-1)
  while True:
    out = state&1
    yield out
    state = (state>>1)^(out*taps)
    
def check(n,taps):
  m = 2**n-1
  L = [out for out,_ in zip(LFSR(n,taps),range(m+n))]
  M = {sum(L[k+1]*(1<<i) for i in range(n)) for k in range(m)}
  return len(M)==m

check(20,Ob1001 0000 0000 0000 0000) # 16 0
