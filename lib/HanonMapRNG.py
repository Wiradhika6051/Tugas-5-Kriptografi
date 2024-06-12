import time
import struct
import base64
class HanonMapRNG:
  SIGNIFICANT_DIGIT = 10 ** 7
  DIGIT_MODULO = 10 ** 4
  def __init__(self,x:float,a:float=1.4,b:float=-0.3,min_size:int=16,base_iteration:int=1000) -> None:
    self.x:float = x
    self.a:float = a
    self.b:float = b
    self.min_size = min_size
    self.base_iteration = base_iteration

  def get_salt(self)->bytes:
    salt = bytearray()
    while len(salt)<self.min_size:
      n = self.base_iteration + int(time.time() * HanonMapRNG.SIGNIFICANT_DIGIT) % HanonMapRNG.DIGIT_MODULO
      hanon_value = self._get_hanon_map_value(n)
      salt += bytearray(struct.pack("f",hanon_value))
    return base64.b64encode(salt)

  def _get_hanon_map_value(self,n:int)->float:
    for _ in range(n):
      self.x = 1-self.a * (self.x * self.x) +self.b * self.x
    return self.x