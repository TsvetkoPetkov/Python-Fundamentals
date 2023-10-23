start = int(input())
end = int(input())

outp = ""

for i in range(start, end+1):
    outp += chr(i)
    outp += " "

print(f"{outp}")
