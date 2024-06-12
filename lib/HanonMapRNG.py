import time
class HanonMapRNG:
  SIGNIFICANT_DIGIT = 10 ** 7
  DIGIT_MODULO = 10 ** 4
  BASE_ITERATION = 1000
  def __init__(self,x:float,a:float=1.4,b:float=-0.3) -> None:
    self.x:float = x
    self.a:float = a
    self.b:float = b

  def get_salt(self):
    # n = HanonMapRNG.BASE_ITERATION + int(time.time() * HanonMapRNG.SIGNIFICANT_DIGIT) % HanonMapRNG.DIGIT_MODULO
    n =10000
    print(n)
    value = self._get_hanon_map_value(n)
    return value

  def _get_hanon_map_value(self,n:int):
    for _ in range(n):
      self.x = 1-self.a * (self.x * self.x) +self.b * self.x
    return self.x