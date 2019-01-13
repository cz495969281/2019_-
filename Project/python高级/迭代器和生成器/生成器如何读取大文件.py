# 一个文件有500G,需要一行一行的读取出来
#这个文件比较特殊只有一行，这个文件是以追加的方式写进去的
#文件中的分割符是{|}

def myreadlines(f,newline):
    buf = ""   #相当于内存
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline):]

        chunk = f.read(4096)

        if not chunk:
            #说明已经读到了文件结尾
            yield buf
            break
        buf += chunk

with open("input.txt") as f:
    for line in myreadlines(f,"{|}"):
        print(line)