def login (inp):
  inp = str(inp)
  if len(inp) < 21:
    if 64 < ord(inp[0]) < 91 or 96 < ord(inp[0]) < 123: # первая буква символ
      if 47 < ord(inp[-1]) < 58 or 64 < ord(inp[-1]) < 91 or 96 < ord(inp[-1]) < 123: # послядняя символ или цифра
        n = 0
        for i in inp:
          m = ord(i)
          if 44 < m < 47 or 47 < m < 58 or 64 < m < 91 or 96 < m < 123:
            # [45, 46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90,97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
            n += 1
        if len(inp) == n:
            return 1 # Ok
  return 0 # Error 