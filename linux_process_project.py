from time import sleep

class Process:
    def __init__(self, pid, name, state ):
        self.pid = pid
        self.name = name
        self.state = state

    def show_info(self):
        return f"{self.pid} | {self.name} | {self.state}"

    def start(self):
        self.state = "running"
        sleep(3)
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
        try:
            pid = int(input("Enter pid to start the process > "))
        except ValueError:
            print("Please enter a valid number.")
            return

        process = self.processes.get(pid)

        if process is None:
            print("PID not found.")
            return

        if process.state == "running":
            print(f"{process.pid} | {process.name} => is already running")
        else:
            process.start()

    def kill_process(self):
        try:
            kill_input = int(input("Enter pid to kill a process ❯ "))
        except ValueError:
            print("Please enter a valid number.")
            return

        process = self.processes.get(kill_input)

        if process is None:
            print("PID not found.")
            return
        self.processes.pop(kill_input)

        print(f"{process.pid} | {process.name} => is killed")

systemd = Systemd()


def main():
    while True:
        choice = input("""Enter 1 to create a process
Enter 2 to start a process
Enter 3 to show process
Enter 4 to kill a process
Enter 5 to Exit
=> """)

        if choice == "1":
            systemd.create()
            systemd.show_process()
            input("press enter to continue...")

        elif choice == "2":
            systemd.start_process()
            input("press enter to continue...")

        elif choice == "3":
            systemd.show_process()
            input("press enter to continue...")

        elif choice == "4":
            systemd.kill_process()
            input("press enter to continue...")

        elif choice == "5":
            break
        else:
            print("Invalid input")



if __name__ == "__main__":
    main()