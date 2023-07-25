with open('paragraph.txt','w')as f:
    f.write('Artificial Intelligence (AI) has revolutionized numerous industries and has become an integral '
            'part of our daily lives. AI refers to the development of computer systems that can perform tasks'
            ' that would typically require human intelligence. It encompasses a wide range of technologies,'
            ' including machine learning, natural language processing, and computer vision. AI has transformed '
            'sectors such as healthcare, finance, transportation, and entertainment. In healthcare, AI algorithms'
            ' can analyze medical data and assist in diagnosing diseases, predicting outcomes, and recommending'
            ' treatment plans. In finance, AI-powered algorithms can analyze vast amounts of data to detect fraudulent '
            'transactions and make accurate predictions for investment strategies. Self-driving cars are a prime example '
            'of AI in transportation, where sophisticated algorithms enable vehicles to navigate roads and make real-time '
            'decisions. AI has also enhanced our entertainment experiences through personalized recommendations '
            'on streaming platforms and virtual assistants like Siri and Alexa'
            '. The possibilities for AI are vast and continue to expand as technology advances.')

f.close()
f2=open('new.txt','w')
with open('paragraph.txt','r') as f1:
        s=f1.readline()
        for i in range(len(s)):
                if 65<=ord(s[i])<=90 or 97<=ord(s[i])<=122:
                        f2.write(f'{s[i]}')
f2.close()
countA=0
countB=0
countC=0
countD=0
countE=0
countF=0
countG=0
countH=0
countI=0
countJ=0
countK=0
countL=0
countM=0
countN=0
countO=0
countP=0
countQ=0
countR=0
countS=0
countT=0
countU=0
countV=0
countW=0
countX=0
countY=0
countZ=0
f2=open('new.txt','r')
s=f2.readline()
for i in range(len(s)):
        n=s[i]
        if n == 'a' or n == 'A': countA = countA + 1
        if n == 'b' or n == 'B': countB += 1
        if n == 'c' or n == 'C': countC += 1
        if n == 'd' or n == 'D': countD += 1
        if n == 'e' or n == 'E': countE += 1
        if n == 'f' or n == 'F': countF += 1
        if n == 'g' or n == 'G': countG += 1
        if n == 'h' or n == 'H': countH += 1
        if n == 'i' or n == 'I': countI += 1
        if n == 'j' or n == 'J': countJ += 1
        if n == 'k' or n == 'K': countK += 1
        if n == 'l' or n == 'L': countL += 1
        if n == 'm' or n == 'M': countM += 1
        if n == 'n' or n == 'N': countN += 1
        if n == 'o' or n == 'O': countO += 1
        if n == 'p' or n == 'P': countP += 1
        if n == 'q' or n == 'Q': countQ += 1
        if n == 'r' or n == 'R': countR += 1
        if n == 's' or n == 'S': countS += 1
        if n == 't' or n == 'T': countT += 1
        if n == 'u' or n == 'U': countU += 1
        if n == 'v' or n == 'V': countV += 1
        if n == 'w' or n == 'W': countW += 1
        if n == 'x' or n == 'X': countX += 1
        if n == 'y' or n == 'Y': countY += 1
        if n == 'z' or n == 'Z': countZ += 1
print(f'count A is {countA}')
print(f'count B is {countB}')
print(f'count C is {countC}')
print(f'count D is {countD}')
print(f'count E is {countE}')
print(f'count F is {countF}')
print(f'count G is {countG}')
print(f'count H is {countH}')
print(f'count I is {countI}')
print(f'count J is {countJ}')
print(f'count K is {countK}')
print(f'count L is {countL}')
print(f'count M is {countM}')
print(f'count N is {countN}')
print(f'count O is {countO}')
print(f'count P is {countP}')
print(f'count Q is {countQ}')
print(f'count R is {countR}')
print(f'count S is {countS}')
print(f'count T is {countT}')
print(f'count U is {countU}')
print(f'count V is {countV}')
print(f'count W is {countW}')
print(f'count X is {countX}')
print(f'count Y is {countY}')
print(f'count Z is {countZ}')

