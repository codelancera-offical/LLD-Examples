from abc import ABC, abstractmethod

# define command interface (挖一个特定规格插槽出来)
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Define Receivers
class Light:
    def on(self):
        print("Light turned ON")

    def off(self):
        print("Light turned OFF")

class Thermostat:
    def __init__(self):
        self.current_temperature = 20

    def set_temperature(self, temp):
        print(f"Thermostat set to {temp}C")
        self.current_temperature = temp

    def get_current_temperature(self):
        return self.current_temperature
    
# Implement Concrete Commands （实现可以插进这个插槽的机器）
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light # 这个机器持有light的引用

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()

class SetTemperatureCommand(Command):
    def __init__(self, thermostat, temperature):
        self.thermostat = thermostat
        self.new_temperature = temperature
        self.previous_temperature = None

    def execute(self):
        self.previous_temperature = self.thermostat.get_current_temperature()
        self.thermostat.set_temperature(self.new_temperature)
    
    def undo(self):
        self.thermostat.set_temperature(self.previous_temperature)

# Create Controlller

class RemoteControl:
    def __init__(self):
        self.history = []

    def execute_command(self, command:Command): # 这里有一个指令卡插入口，指令卡插入口插槽规格指定为Command
        command.execute()
        self.history.append(command)
    
    def undo_last(self):
        if self.history:
            last_command = self.history.pop()
            last_command.undo()
        else:
            print("Nothing to undo.")


# Client Code
def main():
    light = Light()
    thermostat = Thermostat()

    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)
    set_temp = SetTemperatureCommand(thermostat, 25)

    remote = RemoteControl()

    print("--- Executing Commands ---")
    remote.execute_command(light_on)
    remote.execute_command(set_temp)
    remote.execute_command(light_off)

    print("\n--- Undoing Commands ---")
    remote.undo_last()
    remote.undo_last()
    remote.undo_last()
    remote.undo_last()


if __name__ == "__main__":
    main()