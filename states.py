class StateMachine():
    commands = [
        ["INICIO"],
        ["LOCATION"],
        ["LOCATION_CONFIRMATION"],
        ["SIZE_X"],
        ["SIZE_X_CONFIRMATION"],
        ["CHOOSE_IF_SIZE_Y"],
        ["SIZE_Y"],
        ["SIZE_Y_CONFIRMATION"],
        ["CHOOSE_IS_MORE_PARAMS"],
        ["CHOOSE_PARAM_TO_ADD_MODIFY"],
        ["NICE"],
        ["JNET"],
        ["LESION"],
        ["PARIS"],
        ["RECOVER"],
        ["CHOOSE_RECOVERY_PARAMS_TO_ADD_MODIFY"],
        ["NUM_FRAGMENTS"],
        ["NUM_FRAGMENTS_CONFIRMATION"],
        ["RESECTION_METHOD"],
        ["SEND_DATA"],
    ]

    ui_actions = {
        "INICIO": ["BRANCH"],
        "LOCATION": ["SET_LOCATION", "NEXT_STATE"],
        "LOCATION_CONFIRMATION": ["BRANCH"],
        "SIZE_X": ["SET_SIZE_X", "NEXT_STATE"],
        "SIZE_X_CONFIRMATION": ["BRANCH"],
        "CHOOSE_IF_SIZE_Y": ["BRANCH"],
        "SIZE_Y": ["SET_SIZE_Y", "NEXT_STATE"],
        "SIZE_Y_CONFIRMATION": ["BRANCH"],
        "CHOOSE_IS_MORE_PARAMS": ["BRANCH"],
        "CHOOSE_PARAM_TO_ADD_MODIFY": ["BRANCH"],
        "NICE": ["SET_NICE", "BRANCH"],
        "JNET": ["SET_JNET", "BRANCH"],
        "LESION": ["SET_LESION", "BRANCH"],
        "PARIS": ["SET_PARIS", "BRANCH"],
        "RECOVER": ["BRANCH"],
        "CHOOSE_RECOVERY_PARAMS_TO_ADD_MODIFY": ["BRANCH"],
        "NUM_FRAGMENTS": ["SET_NUM_FRAGMENTS", "NEXT_STATE"],
        "NUM_FRAGMENTS_CONFIRMATION": ["BRANCH"],
        "RESECTION_METHOD": ["SET_RESECTION_METHOD", "BRANCH"],
        "SEND_DATA": ["SEND_DATA"],
    }

    next_states = {
        "INICIO": 1,
        "LOCATION": 2,
        "LOCATION_CONFIRMATION": 3,
        "SIZE_X": 4,
        "SIZE_X_CONFIRMATION": 5,
        "CHOOSE_IF_SIZE_Y": 6,
        "SIZE_Y": 7,
        "SIZE_Y_CONFIRMATION": 8,
        "CHOOSE_IS_MORE_PARAMS": 9,
        "CHOOSE_PARAM_TO_ADD_MODIFY": 10,
        "NICE": 11,
        "JNET": 12,
        "LESION": 13,
        "PARIS": 14,
        "RECOVER": 15,
        "CHOOSE_RECOVERY_PARAMS_TO_ADD_MODIFY": 16,
        "NUM_FRAGMENTS": 17,
        "NUM_FRAGMENTS_CONFIRMATION": 18,
        "RESECTION_METHOD": 19,
        "SEND_DATA": 0,
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
        if command == "SEND_DATA":
            return True

        if command == "LOCATION":
            digits = ''.join(c for c in transcription if c.isdigit())
            has_number = bool(digits)
            self.set_location_argument(digits)
            return has_number
        
        if command == "SIZE_X":
            digits = ''.join(c for c in transcription if c.isdigit())
            has_number = bool(digits)
            self.set_size_x_argument(digits)
            return has_number
        
        if command == "SIZE_Y":
            digits = ''.join(c for c in transcription if c.isdigit())
            has_number = bool(digits)
            self.set_size_y_argument(digits)
            return has_number
        
        if command == "NUM_FRAGMENTS":
            digits = ''.join(c for c in transcription if c.isdigit())
            has_number = bool(digits)
            self.set_num_fragments_argument(digits)
            return has_number

        if command == "LOCATION_CONFIRMATION":
            confirm = True if " SÍ " in transcription or " SI " in transcription else False if " NO " in transcription else None
            if confirm is not None:
                self.set_branch(confirm, "LOCATION_CONFIRMATION", 0, self.curr_state + 1, self.curr_state - 1)
                return True
            
        if command == "INICIO":
            confirm = True if " SÍ " in transcription or " SI " in transcription else None
            if confirm is not None:
                self.set_branch(True, "INICIO", 0, self.curr_state + 1, self.curr_state + 1)
                return True
            
        if command == "SIZE_X_CONFIRMATION":
            confirm = True if " SÍ " in transcription or " SI " in transcription else False if " NO " in transcription else None
            if confirm is not None:
                self.set_branch(confirm, "SIZE_X_CONFIRMATION", 0, self.curr_state + 1, self.curr_state - 1)
                return True
            
        if command == "SIZE_Y_CONFIRMATION":
            confirm = True if " SÍ " in transcription or " SI " in transcription else False if " NO " in transcription else None
            if confirm is not None:
                self.set_branch(confirm, "SIZE_Y_CONFIRMATION", 0, self.curr_state + 1, self.curr_state - 1)
                return True
            
        if command == "NUM_FRAGMENTS_CONFIRMATION":
            confirm = True if " SÍ " in transcription or " SI " in transcription else False if " NO " in transcription else None
            if confirm is not None:
                self.set_branch(confirm, "NUM_FRAGMENTS_CONFIRMATION", 0, self.curr_state - 2, self.curr_state - 1)
                return True
            
        if command == "CHOOSE_IF_SIZE_Y":
            confirm = True if " SÍ " in transcription or " SI " in transcription else False if " NO " in transcription else None
            if confirm is not None:
                self.set_branch(confirm, "CHOOSE_IF_SIZE_Y", 0, self.curr_state + 1, self.curr_state + 3)
                return True 
            
        if command == "CHOOSE_IS_MORE_PARAMS":
            confirm = True if " SÍ " in transcription or " SI " in transcription else False if " NO " in transcription else None
            if confirm is not None:
                self.set_branch(confirm, "CHOOSE_IS_MORE_PARAMS", 0, 9, 14)
                return True

        if command == "RECOVER":
            confirm = True if " SÍ " in transcription or " SI " in transcription else False if " NO " in transcription else None
            if confirm is not None:
                self.set_branch(confirm, "RECOVER", 0, 15, 19)
                return True

        if command == "CHOOSE_PARAM_TO_ADD_MODIFY":
            digits = ''.join(c for c in transcription if c.isdigit())
            if digits == "1":
                self.set_branch(True, "CHOOSE_PARAM_TO_ADD_MODIFY", 0, 10, 10)
                return True
            elif digits == "2":
                self.set_branch(True, "CHOOSE_PARAM_TO_ADD_MODIFY", 0, 11, 11)
                return True
            elif digits == "3":
                self.set_branch(True, "CHOOSE_PARAM_TO_ADD_MODIFY", 0, 12, 12)
                return True
            elif digits == "4":
                self.set_branch(True, "CHOOSE_PARAM_TO_ADD_MODIFY", 0, 13, 13)
                return True
            elif digits == "5":
                self.set_branch(True, "CHOOSE_PARAM_TO_ADD_MODIFY", 0, 14, 14)
                return True
            else:
                return False            

        if command == "CHOOSE_RECOVERY_PARAMS_TO_ADD_MODIFY":
            digits = ''.join(c for c in transcription if c.isdigit())
            if digits == "1":
                self.set_branch(True, "CHOOSE_RECOVERY_PARAMS_TO_ADD_MODIFY", 0, 16, 16)
                return True
            elif digits == "2":
                self.set_branch(True, "CHOOSE_RECOVERY_PARAMS_TO_ADD_MODIFY", 0, 18, 18)
                return True
            elif digits == "3":
                self.set_branch(True, "CHOOSE_RECOVERY_PARAMS_TO_ADD_MODIFY", 0, 19, 19)
                return True
            else:
                return False

        if command == "NICE":
            digits = ''.join(c for c in transcription if c.isdigit())
            if digits == "1" or digits == "2" or digits == "3":
                self.set_nice_argument(digits)
                self.set_branch(True, "NICE", 1, 9, 9)
                return True
            else:
                return False
            
        if command == "JNET":
            digits = ''.join(c for c in transcription if c.isdigit())
            if digits == "1" or digits == "2" or digits == "3" or digits == "4":
                self.set_jnet_argument(digits)
                self.set_branch(True, "JNET", 1, 9, 9)
                return True
            else:
                return False
                
        if command == "LESION":
            digits = ''.join(c for c in transcription if c.isdigit())
            if digits == "1" or digits == "2":
                self.set_lesion_argument(digits)
                self.set_branch(True, "LESION", 1, 9, 9)
                return True
            else:
                return False
            
        if command == "PARIS":
            digits = ''.join(c for c in transcription if c.isdigit())
            if digits == "1" or digits == "2" or digits == "3" or digits == "4" or digits == "5" or digits == "6" or digits == "7" or digits == "8" or digits == "9" or digits == "10" or digits == "11":
                self.set_paris_argument(digits)
                self.set_branch(True, "PARIS", 1, 9, 9)
                return True
            else:
                return False
            
        if command == "RESECTION_METHOD":
            digits = ''.join(c for c in transcription if c.isdigit())
            if digits == "1" or digits == "2" or digits == "3" or digits == "4":
                self.set_resection_method_argument(digits)
                self.set_branch(True, "RESECTION_METHOD", 1, 15, 15)
                return True
            else:
                return False
            
        return False
    
    def set_location_argument(self, number):
        self.ui_actions["LOCATION"][0] = self.ui_actions["LOCATION"][0] + " " + number

    def set_size_x_argument(self, number):
        self.ui_actions["SIZE_X"][0] = self.ui_actions["SIZE_X"][0] + " " + number

    def set_size_y_argument(self, number):
        self.ui_actions["SIZE_Y"][0] = self.ui_actions["SIZE_Y"][0] + " " + number

    def set_num_fragments_argument(self, number):
        self.ui_actions["NUM_FRAGMENTS"][0] = self.ui_actions["NUM_FRAGMENTS"][0] + " " + number
    
    def set_nice_argument(self, number):
        self.ui_actions["NICE"][0] = self.ui_actions["NICE"][0] + " " + number

    def set_jnet_argument(self, number):
        self.ui_actions["JNET"][0] = self.ui_actions["JNET"][0] + " " + number

    def set_resection_method_argument(self, number):
        self.ui_actions["RESECTION_METHOD"][0] = self.ui_actions["RESECTION_METHOD"][0] + " " + number

    def set_lesion_argument(self, number):
        self.ui_actions["LESION"][0] = self.ui_actions["LESION"][0] + " " + number

    def set_paris_argument(self, number):
        self.ui_actions["PARIS"][0] = self.ui_actions["PARIS"][0] + " " + number

    def set_branch(self, confirm, command, index, state_yes, state_no):
        self.next_states[command] = state_yes if confirm else state_no
        self.ui_actions[command][index] = f"""{self.ui_actions[command][index]} {state_yes if confirm else state_no}"""
