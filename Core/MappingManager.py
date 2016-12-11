from backports import configparser

from Model.Button import Button
from Model.Constants import Constants


class MappingManager:
    @staticmethod
    def map():
        print("detecting mapping...")

        buttons = []

        for player_idx in range(1, 3):
            config = configparser.RawConfigParser()
            print("\nMapping player ["+str(player_idx)+"]")
            ini_str =\
                '[' + Constants.default_conf_section + ']\n' \
                + open(Constants.config_gpio_base_path+str(player_idx)+".cfg", 'r').read()

            config.read_string(ini_str.decode('utf8'))

            for direction in Constants.directions:
                btn = MappingManager.__map_input("input_" + direction + "_axis", config, player_idx)
                buttons.append(btn)
            for button_key in Constants.buttons_keys:
                btn = MappingManager.__map_input("input_" + button_key + "_btn", config, player_idx)
                if btn is not None:
                    buttons.append(btn)

        return buttons

    @staticmethod
    def __map_input(conf_key, config, player_idx):
        if config.has_option(Constants.default_conf_section, conf_key):
            key = config.get(Constants.default_conf_section, conf_key)[1:-1]
            bcm_code = Constants.keys_map[player_idx - 1][key]
            print("[" + conf_key + "] [" + key + "] -> [" + str(bcm_code) + "]")
            return Button(conf_key, bcm_code, player_idx)
        else:
            print("[" + conf_key + "] -> [ NOT MAPPED ]")
            return None
