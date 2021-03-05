def rprint(s):
      ls  = list(s)
      ls.reverse()
      print("".join(ls))
def reverse_str(s):
      ls = list(s)
      ls.reverse()
      return "".join(ls)
if __name__ == "__main__":
      myword = "hello"
      print(myword)
      rev = reverse_str(myword)
      print(rev)
