import argparse
from lib.HanonMapRNG import HanonMapRNG


if __name__=="__main__":
  parser = argparse.ArgumentParser(prog="HaonMapRNG",description="Pembangkit Bilangan Acak Berbasis Hanon Map")
  parser.add_argument("--x0",type=float,help="Nilai Awal x0",default='0.0016408') # Just a random number buat nilai default
  parser.add_argument("--a",type=float,help="Nilai konstanta a untuk Hanon Map",default='1.4') # Just a random number buat nilai default
  parser.add_argument("--b",type=float,help="Nilai konstanta b untuk Hanon Map",default='-0.3') # Just a random number buat nilai default
  parser.add_argument("-size",type=int,help="Ukuran minimal (bytes) salt yang dihasilkan",default='16') # Just a random number buat nilai default
  parser.add_argument("-base-iteration",type=int,help="Minimal iterasi yang dilakukan untuk membangkitkan salt",default='1000') # Just a random number buat nilai default

  args = parser.parse_args()
  hanon_rng = HanonMapRNG(args.x0,args.a,args.b,args.size,args.base_iteration)
  salt = hanon_rng.get_salt()
  print("Your salt :",salt)