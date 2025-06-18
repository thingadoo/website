import sys

cipher_dict = {
  "e": 2,
  "a": 3,
  "r": 5,
  "i": 7,
  "o": 11,
  "t": 13,
  "n": 17,
  "s": 19,
  "l": 23,
  "c": 29,
  "u": 31,
  "d": 37,
  "p": 41,
  "m": 43,
  "h": 47,
  "g": 53,
  "b": 59,
  "f": 61,
  "y": 67,
  "w": 71,
  "k": 73,
  "v": 79,
  "x": 83,
  "z": 89,
  "j": 97,
  "q": 101
}
special_characters = "!@#$%^&*()_+{}|:<>?-=[];',./"
out: int = 1
out_special_character: str = ""

x: str = input("input message: ")
x = x.lower()
li = list(x.split(" "))
for i in li:
    for j in i:
        if any(c in special_characters for c in j):
            out_special_character = j
        else:
            out = out * int(cipher_dict[j])
    sys.stdout.write(str(out))
    sys.stdout.write(out_special_character)
    sys.stdout.write(" ")
    out = 1
    out_special_character = ""
