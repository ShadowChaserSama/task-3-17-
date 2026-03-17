name = input()

with open('students.txt','r',encoding='utf-8') as f:
  names = f.readlines()
  names = list(map(lambda x : x.strip('\n'), names))
  if name in names:
    print('Exists')
  else:
    print('Dont exists')
