class Process:
    def __init__(self, pid, name, state ):
        self.pid = pid
        self.name = name
        self.state = state

    def show_info(self):
        return f"{self.pid} | {self.name} | {self.state}"

    def start(self):
        if self.state == "running":
            print(f"{self.pid} | {self.name} => is running")


class Systemd:
    def __init__(self):

        #systemd process collection =>
        self.processes = {}
        self.next_pid = 1

    def create(self):
        name = input("Enter process to create ❯ ")

        process = Process(
            pid= self.next_pid,
            name= name,
            state= "stopped"
            )

        self.processes[self.next_pid] = process

        self.next_pid += 1

    def show_process(self):
        for x in self.processes.values():
            print(f"{x.pid} | {x.name} | {x.state}")

    def start_process(self):

        user_input = int(input(f"Enter pid to start the process ❯ "))
        process = self.processes[user_input]
        self.processes[user_input] = process

        print(f"{user_input} | {process.name} => has started")


sys = Systemd()


def main():
    while True:
        choice = input("""Enter 1 to create a process
Enter 2 to start a process
Enter 3 to show process
Enter 4 to Exit
=> """)

        if choice == "1":
            sys.create()
            sys.show_process()
            input("press enter to continue...")

        elif choice == "2":
            sys.start_process()
            input("press enter to continue...")

        elif choice == "3":
            sys.show_process()
            input("press enter to continue...")

        elif choice == "4":
            break
        else:
            print("Invalid input")



if __name__ == "__main__":
    main()