from controller import Controller
class Ui:
    def __init__(self,controller):
        self.__controller=controller

    def get_sentence(self):
        sentence=self.__controller.choose_prop()
        scrambled=self.__controller.scramble(sentence)
        letters=list(scrambled)
        score=len(letters)
        for l in letters:
            if l==" ":
                score=score-1

        return sentence,scrambled,score

    def menu(self):
        print("\nYou can swap using: swap <word1> <letter1> - <word2> <letter2> ")
        print("exit")




    def start(self):
        sentence,scrambled,score=self.get_sentence()
        print(f"Scrambled sentence: {scrambled}     -> Score:{score}")
        while True:
            self.menu()
            cmd=input(">> ").strip()
            parts=cmd.split()
            if not parts:
                continue
            if parts[0]=="exit":
                return
            elif parts[0]=="swap":
                if len(parts)!=6 or parts[3]!="-":
                    print("Invalid command")
                    continue

                try:
                    w1=int(parts[1])
                    l1=int(parts[2])
                    w2=int(parts[4])
                    l2=int(parts[5])
                except ValueError:
                    print("All values must be type int")
                    continue

                try:
                    new_sentence=self.__controller.swap(scrambled, w1, l1, w2, l2)
                except ValueError as e:
                    print(e)
                    continue



                print(f"Updated sentence: {new_sentence}")
                score-=1
                print(f"New score: {score}")


                if new_sentence==sentence:
                    print("You won!")
                    return

                scrambled = new_sentence

                if score == 0:
                    print("You lost")
                    return


            else:
                print("Invalid command")

