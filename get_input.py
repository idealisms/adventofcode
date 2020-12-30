import os
import sys
import urllib.request

def usage():
  print(f'''Usage:
    {sys.argv[0]} <year> <day>''')

def main(year, day):
  request = urllib.request.Request(
    f'https://adventofcode.com/{year}/day/{day}/input',
    headers={
      'cookie': f'session={open("SESSION_COOKIE").read().strip()}'
    },
  )
  inp = urllib.request.urlopen(request).read()
  with open(f'{year}/day{int(day):02d}input.txt', 'wb') as f:
    f.write(inp)

if __name__ == '__main__':
  if len(sys.argv) != 3:
    usage()
    sys.exit(-1)

  year, day = sys.argv[1:]

  main(year, day)
