import random
class Repo:
    def __init__(self,filename):
        self.filename=filename
        self.sentence=self.load_file()


    def load_file(self):
        sentence=[]
        with open(self.filename,"r") as file:
            for line in file:
                line=line.strip()
                if line:
                    sentence.append(line)


        return sentence

    def get_random_prop(self):
        return random.choice(self.sentence)


