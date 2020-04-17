def count_substring(string, sub_string):
    m=''
    c=0
    for t in string:
        for i in string:
            s=m+i
            m=s
            #print(m)
            if m==sub_string:
                #print(m)
                c+=1
        new_string=string[1:len(string)]
        string=new_string
        m=''
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)