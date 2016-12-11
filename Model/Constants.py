class Constants:
    keys_map = [
        # 1st controller
        {'-1': 4, '+1': 17, '-0': 27, '+0': 22,
         '2': 15, '4': 14, '5': 23, '1': 24, '6': 9, '7': 10, '0': 25, '3': 18},

        # 2nd controller
        {'-1': 11, '+1': 5, '-0': 6, '+0': 13,
         '1': 20, '0': 21, '3': 12, '4': 8, '2': 7, '5': 16, '7': 19}
    ]

    directions = ["up", "down", "left", "right"]
    buttons_keys = ["a", "b", "x", "y", "l", "r", "start", "select"]

    config_gpio_base_path = '/opt/retropie/configs/all/retroarch-joypads/GPIOController'

    default_conf_section = 'root'

    default_mouse_move=10
