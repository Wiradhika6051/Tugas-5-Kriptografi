import argparse
from lib.HanonMapRNG import HanonMapRNG


if __name__=="__main__":
  parser = argparse.ArgumentParser(prog="HaonMapRNG",description="Pembangkit Bilangan Acak Berbasis Hanon Map")
  parser.add_argument("--x0",type=float,help="Nilai Awal x0",default='0.000020496') # Just a random number buat nilai defaulr
  parser.add_argument("--a",type=float,help="Nilai konstanta a untuk Hanon Map",default='1.4') # Just a random number buat nilai defaulr
  parser.add_argument("--b",type=float,help="Nilai konstanta b untuk Hanon Map",default='0.3') # Just a random number buat nilai defaulr

  args = parser.parse_args()
  hanon_rng = HanonMapRNG(args.x0,args.a,args.b)
  print(hanon_rng.get_salt(50))