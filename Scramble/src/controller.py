import random
class Controller:
    def __init__(self,repo):
        self.__repo=repo

    def choose_prop(self):
        return self.__repo.get_random_prop()


    def scramble(self,sentence):
        result=""
        words=sentence.split(" ")
        middle_letters=[]
        for word in words:
            if len(word) > 2:
                letters=list(word)
                mids=letters[1:-1]
                for m in mids:
                    middle_letters.append(m)
        #shuffle
        random.shuffle(middle_letters)
        #now rewbuild
        index=0
        for i in range(len(words)):
            if len(words[i])<=2:
                result+=words[i]+" "
                continue

            letters=list(words[i])
            needed=len(letters)-2
            result +=letters[0]
            for l in range(needed):
                result+=middle_letters[index]
                index+=1
            result+=letters[-1]
            result+=" "
        return result.strip()


    def swap(self,sentence,w1,l1,w2,l2):
        words=sentence.split()
        if not(0<=w1<len(words) and 0<=w2<len(words)):
            raise ValueError("Words out of bound")

        word1=words[w1]
        word2=words[w2]
        if not(0<=l1<len(word1) and 0<=l2<len(word2)):
            raise ValueError("Letters out of bound")

        if l1==0 or l1==len(word1)-1:
            raise ValueError("You can not swap first or last letter")

        if l2==0 or l2==len(word2)-1:
            raise ValueError("You can not swap first or last letter")


        if w1==w2:
            if l1==l2:
                raise ValueError("You don't have to swap same letters")
            letters=list(word1)
            letters[l1],letters[l2]=letters[l2],letters[l1]
            words[w1]="".join(letters)
            sentence=" ".join(words)

        else:
            letters1=list(word1)
            letters2=list(word2)
            letters1[l1],letters2[l2]=letters2[l2],letters1[l1]

            words[w1]="".join(letters1)
            words[w2]="".join(letters2)


            sentence = " ".join(words)

        return sentence


