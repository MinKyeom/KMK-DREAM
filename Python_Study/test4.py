def solution(numbers):
    from itertools import permutations
    #num=[("zero",0),("one",1),("two",2),("three",3),("four",4),("five",5),("six",6),("seven",7),("eight",8),("nine",9)]
    num=["zero","one","two","three","four","five","six","seven","eight","nine"]
    for a in range(1,50):
        b=list(permutations(num,a))
        if not b[0]=="zero":
            c="".join(map(str,b))
            if c==numbers:
                for d in range(len(b)):
                    if b[d]=="zero":
                        b[d]="0"
                    elif b[d]=="one":
                        b[d]="1"
                    elif b[d]=="two":
                        b[d]="2"
                    elif b[d]=="three":
                        b[d]="3"
                    elif b[d]=="four":
                        b[d]="4"
                    elif b[d]=="five":
                        b[d]="5"
                    elif b[d]=="six":
                        b[d]="6"
                    elif b[d]=="seven":
                        b[d]="7"
                    elif b[d]=="eight":
                        b[d]="8"
                    elif b[d]=="nine":
                        b[d]="9"
                answer="".join(b)
                break
    return answer

numbers="onetwothreefourfivesixseveneightnine"

f=solution(numbers)

print(f)