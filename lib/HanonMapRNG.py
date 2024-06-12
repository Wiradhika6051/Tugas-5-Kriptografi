class HanonMapRNG:
  def __init__(self,x:float,a:float=1.4,b:float=0.3) -> None:
    self.x:float = x
    self.a:float = a
    self.b:float = b

  def get_salt(self,n:int):
    value = self._get_hanon_map_value(n)
    return value

  def _get_hanon_map_value(self,n:int):
    for _ in range(n):
      self.x = 1-1.4*(self.x*self.x)+0.3*self.x
    return self.x
