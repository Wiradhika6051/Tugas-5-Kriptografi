import time
class HanonMapRNG:
  SIGNIFICANT_DIGIT = 10 ** 7
  DIGIT_MODULO = 10 ** 4
  BASE_ITERATION = 1000
  def __init__(self,x:float,y:float,a:float=1.4,b:float=0.3) -> None:
    self.x:float = x
    self.y:float = y
    self.a:float = a
    self.b:float = b

  def get_salt(self):
    n = HanonMapRNG.BASE_ITERATION + int(time.time() * HanonMapRNG.SIGNIFICANT_DIGIT) % HanonMapRNG.DIGIT_MODULO
    print(n)
    value = self._get_hanon_map_value(n)
    return value

  def _get_hanon_map_value(self,n:int):
    # print(self.x,self.y)
    x = []
    y = []
    for _ in range(n):
      self.x = 1*10**0-self.a*10**0*(self.x*self.x) + self.y
      self.y = self.b*10**0 * self.x
      # if n % 100 == 0:
      #   self.a = self.a + 0.0001
      # print(self.x,self.y)
      x.append(self.x)
      y.append(self.y)
    return self.x,self.y,x,y