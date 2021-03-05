from operator import itemgetter

def score_cal(score:dict):
    dic2 = sorted(score.items(), key = itemgetter(1), reverse=True)
    pnum = []
    psum = 0
    for i in dic2[:5]:
        pnum.append(str(i[0]))
        psum += i[1]
    pnum.sort()
    print(psum)
    print(" ".join(pnum))

if __name__ == "__main__":
    score = {}
    for i in range(8):
        score[i+1] = int(input())
    score_cal(score)