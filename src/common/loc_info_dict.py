def get_loc_info_dict(col_list):
       
    loc_info_dict_6666 = {
        'A1': {
            '1_1': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_7': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}},

        'A2': {
            '1_1': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_7': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}},

        'A3': {
            '1_1': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_7': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}},

        'A4': {
            '1_1': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_7': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}},

        'B1': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}},

        'B2': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}},

        'B3': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}},

        'B4': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}},

        'C1': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': False, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_7': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}},

        'C2': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_7': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': False, 'min_col_flag': True}},

        'C3': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': False, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_7': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}},

        'C4': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_7': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': False}}}

    loc_info_dict_4664 = {
        'A1': {
            '1_1': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}},

        'A2': {
            '1_1': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_7': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}},

        'A3': {
            '1_1': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_7': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}},

        'A4': {
            '1_1': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}},

        'B1': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}},

        'B2': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}},

        'B3': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}},

        'B4': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}},

        'C1': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': False, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}},

        'C2': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_7': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': False, 'min_col_flag': True}},

        'C3': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': False, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_7': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}},

        'C4': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': False}}}

    loc_info_dict_7667 = {
        'A1': {
            '1_1': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_7': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_8': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_8': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_8': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}},

        'A2': {
            '1_1': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_7': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
    
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}},

        'A3': {
            '1_1': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_7': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}},

        'A4': {
            '1_1': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_7': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_8': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_8': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_8': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}},

        'B1': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_8': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_8': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_8': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}},

        'B2': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}},

        'B3': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}},

        'B4': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_8': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_8': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_8': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}},

        'C1': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_8': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_8': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': False, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_7': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_8': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}},

        'C2': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_7': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': False, 'min_col_flag': True}},

        'C3': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': False, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_7': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}},

        'C4': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_8': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_7': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_8': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_7': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_8': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': False}}}

    loc_info_dict_4554 = {
        'A1': {
            '1_1': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}},

        'A2': {
            '1_1': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}},

        'A3': {
            '1_1': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}},

        'A4': {
            '1_1': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': False, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}},

        'B1': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}},

        'B2': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}},

        'B3': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}},

        'B4': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}},

        'C1': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': False, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}},

        'C2': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': False, 'min_col_flag': True}},

        'C3': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_6': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': False, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_6': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}},

        'C4': {
            '1_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '1_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}, \
     
            '2_1': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': False, 'min_col_flag': True}, \
            '2_2': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_3': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_4': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': True}, \
            '2_5': {'max_row_flag': True, 'min_row_flag': True, 'max_col_flag': True, 'min_col_flag': False}, \
     
            '3_1': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_2': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_3': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_4': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': True}, \
            '3_5': {'max_row_flag': True, 'min_row_flag': False, 'max_col_flag': True, 'min_col_flag': False}}}
    
    if col_list == [6, 6, 6, 6]:
        return loc_info_dict_6666
    elif col_list == [4, 6, 6, 4]:
        return loc_info_dict_4664
    elif col_list == [7, 6, 6, 7]:
        return loc_info_dict_7667
    elif col_list == [4, 5, 5, 4]:
        return loc_info_dict_4554
    else:
        print('unsupport col list')
