from Core.MappingManager import MappingManager
from Core.ButtonManager import ButtonManager


def main():
    print("Starting joystick2mouse...")
    buttons = MappingManager.map()
    buttons_manager = ButtonManager(buttons)
    buttons_manager.process()

if __name__ == "__main__":
    main()
