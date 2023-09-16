import os
contenents = ['Africa','America','Antarctica','Asia','Atlantic','Australia','Etc','Europe','Pacific']

with open (os.path.join(os.path.dirname(os.path.realpath(__file__)), "world_Api_data.txt"),'r') as f :
    # print(f.readline(slice('/')))
    # print(len(f.readlines()))
    # print(f.readlines()[0])
    content = f.readlines()
    for i in content:
        sublocation = i.split("/")
        print(sublocation[0])
        if sublocation[0] in contenents :
            with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), f"{sublocation[0]}.txt"),'+a') as g:
                g.write(f'"{sublocation[1]}",')
                g.close()
    f.close()
    # break
