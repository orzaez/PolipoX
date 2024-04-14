class StateMachine():
    commands = [
        ["REGISTRO"],
        ["LOCATION"],
        ["LOCATION_CONFIRMATION"],
        ["SIZE_X"]
    ]

    ui_actions = {
        "REGISTRO": ["NEXT_STATE"],
        "LOCATION": ["SET_LOCATION", "NEXT_STATE"],
        "LOCATION_CONFIRMATION": ["BRANCH"],
        "SIZE_X": []
    }

    next_states = {
        "REGISTRO": 1,
        "LOCATION": 2,
        "LOCATION_CONFIRMATION": 3,
        "SIZE_X": 3
    }

    def __init__(self) -> None:
        self.curr_state = 0

    def check_command(self, transcription):
        for command in self.commands[self.curr_state]:
            there_is_command = self.check_there_is_command(command, transcription)
            if there_is_command:
                self.curr_state = self.next_states[command]
                return True, self.ui_actions[command] 
        return False, ""
    
    def check_there_is_command(self, command, transcription):
        if command == "LOCATION":
            digits = ''.join(c for c in transcription if c.isdigit())
            has_number = bool(digits)
            self.set_location_argument(digits)
            return has_number
        
        if command == "LOCATION_CONFIRMATION":
            confirm = True if " SÍ " in transcription or " SI " in transcription else False if " NO " in transcription else None
            if confirm is not None:
                self.set_branch(confirm, "LOCATION_CONFIRMATION", 0, self.curr_state + 1, self.curr_state - 1)
                return True        
        return command in transcription
    
    def set_location_argument(self, number):
        self.ui_actions["LOCATION"][0] = self.ui_actions["LOCATION"][0] + " " + number

    def set_branch(self, confirm, command, index, state_yes, state_no):
        self.next_states[command] = state_yes if confirm else state_no
        self.ui_actions[command][index] = f"""{self.ui_actions[command][index]} {state_yes if confirm else state_no}"""
        
    # def check_number_in_words(self, transcription):
    #     numbers_in_words = {
    #         "one": 1,
    #         "two": 2,
    #         "three": 3,
    #         "four": 4,
    #         "five": 5,
    #         "six": 6,
    #         "seven": 7,
    #         "eight": 8,
    #         "nine": 9,
    #         "ten": 10,
    #         "hundred": 100,
    #         "thousand": 1000,
    #         "fifty": 50,
    #     }
    #     sum_of_numbers = 0
    #     for word in transcription.split():
    #         if word.lower() in numbers_in_words:
    #             sum_of_numbers += numbers_in_words[word.lower()]
    #     return sum_of_numbers > 0
