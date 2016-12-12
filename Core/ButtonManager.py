import time
import RPi.GPIO as GPIO
import uinput

from Model.Constants import Constants

class ButtonManager:

    def __init__(self, buttons):
        self.buttons = buttons
        GPIO.setmode(GPIO.BCM)
        self.device = uinput.Device([
            uinput.BTN_LEFT,
            uinput.REL_X,
            uinput.REL_Y,
            uinput.KEY_UP,
            uinput.KEY_DOWN,
            uinput.KEY_RIGHT,
            uinput.KEY_LEFT,
            uinput.KEY_BACKSPACE,
            uinput.KEY_ESC,
            uinput.KEY_ENTER
        ])

        self.last_move = None

    def process(self):
        for button in self.buttons:
            GPIO.setup(button.code, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        while True:
            found = False
            for button in self.buttons:
                if GPIO.input(button.code) == 0:
                    found = True
                    self.click_button(button)
            if not found:
                self.last_move = None
            time.sleep(0.03)

    def click_button(self, button):
        print(button.name)
        if button.name.endswith("_axis"):
            if button.name == 'input_up_axis':
                print("UP")
                if button.player_idx == 2:
                    self.device.emit(uinput.REL_Y, Constants.default_mouse_move * -1)
                elif self.last_move != button.name:
                    self.device.emit_click(uinput.KEY_UP)
            elif button.name == 'input_down_axis':
                print("DOWN")
                if button.player_idx == 2:
                    self.device.emit(uinput.REL_Y, Constants.default_mouse_move)
                elif self.last_move != button.name:
                    self.device.emit_click(uinput.KEY_DOWN)
            elif button.name == 'input_left_axis':
                print("LEFT")
                if button.player_idx == 2:
                    self.device.emit(uinput.REL_X, Constants.default_mouse_move * -1)
                elif self.last_move != button.name:
                    self.device.emit_click(uinput.KEY_LEFT)
            else:
                print("RIGHT")
                if button.player_idx == 2:
                    self.device.emit(uinput.REL_X, Constants.default_mouse_move)
                elif self.last_move != button.name:
                    self.device.emit_click(uinput.KEY_RIGHT)

            if button.player_idx == 1:
                self.last_move = button.name
        elif self.last_move != button.name:
            if button.name == "input_start_btn":
                print("TAB")
                self.device.emit_click(uinput.KEY_TAB)
            if button.player_idx == 2:
                if button.name == "input_a_btn":             #Second Player
                    print("BTN_LEFT")
                    self.device.emit_click(uinput.BTN_LEFT)
            elif button.name == "input_a_btn":                 #First Player
                print("KEY_ENTER")
                self.device.emit_click(uinput.KEY_ENTER)
            elif button.name == "input_b_btn":                  #First Player
                print("KEY_BACKSPACE")
                self.device.emit_click(uinput.KEY_BACKSPACE)
            elif button.name == "input_select_btn":                 #First Player
                print("KEY_ESCAPE")
                self.device.emit_click(uinput.KEY_ESC)
            self.last_move = button.name
