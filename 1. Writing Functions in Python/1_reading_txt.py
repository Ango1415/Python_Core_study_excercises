with open('MyFile.txt', 'r+') as f:
    print(f.read())
    print()

with open('MyFile.txt', 'r+') as f:
    print(f.read())
    f.write('\nAdditional line')
    print()

with open('MyFile.txt', 'a+') as f:
    f.write('\nAnother additional line')
    print()

with open('MyFile.txt', 'r+') as f:
    print(f.read())
    print()

with open('MyFile.txt', 'r+') as f:
    print(f.readlines())
    print()

with open('MyFile.txt', 'r+') as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline()=='')