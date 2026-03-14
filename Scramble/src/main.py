from repo import Repo
from controller import Controller
from ui import Ui
def main():
    repo=Repo("s.txt")
    controller=Controller(repo)
    ui=Ui(controller)
    ui.start()


main()