# prof. edmund weitz 
# weihnachtsvorlesung 2021
# https://www.youtube.com/watch?v=YIkqZsz4faA
# http://weitz.de/

from random import unifrom
from math import pi, cos, floor

def buffon(n):
  return sum(floor(uniform(0,1)+cos(unifrom(0,pi))) != 0
    for _ in range(n) / n
             
buffon(1 000 000)             
