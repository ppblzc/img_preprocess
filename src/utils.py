import sys
import cv2
import logging

def get_logger():
    logger = logging.getLogger('test_and_evaluation')
    logger.setLevel(logging.INFO)

    rf_handler = logging.StreamHandler(sys.stderr)  # 默认是sys.stderr
    rf_handler.setLevel(logging.INFO)
    rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(message)s"))

    f_handler = logging.FileHandler('test.log')
    f_handler.setLevel(logging.INFO)
    f_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(message)s"))

    logger.addHandler(rf_handler)
    logger.addHandler(f_handler)

    return logger

class GridCutSafe:
    def __init__(self, el_data):
        img_info = el_data['img_info']
        self.img_data = img_info['img_cv2']
        self.row_lines, self.col_lines = img_info['row_lines'], img_info['col_lines']
        self.rows, self.cols = img_info['rows'], img_info['cols']
        self.section_idx = img_info['section_idx']
        
        
    def grid_cut_safe_lr(self, lr_padding):
        cut_images = {}
        # if direction == 'l':
        #     col = 1
        #     left_point = max(0, self.col_lines[0] - lr_padding)
        #     right_point = self.col_lines[0] + lr_padding
        # else:
        col = self.cols
        for c in range(self.cols):
            left_point = self.col_lines[c+1] - lr_padding
            right_point = min(self.col_lines[c+1] + lr_padding, self.img_data.shape[1])
            
            for r in range(self.rows):
                key = (r + 1, col, self.row_lines[r], left_point)
                img_cut = self.img_data[self.row_lines[r]:self.row_lines[r + 1], left_point:right_point, :].copy()
                # if direction == 'l':
                cut_images[key] = cv2.flip(cv2.transpose(img_cut), 1)
                # else:
                #     cut_images[key] = cv2.flip(cv2.transpose(img_cut), 0)
            
        return cut_images
    
    
    def grid_cut_safe_ud(self, ud_padding):
        cut_images = {}
        # if direction == 'u':
        #     row = 1
        #     up_point = max(0, self.row_lines[0] - ud_padding)
        #     down_point = self.row_lines[0] + ud_padding
        # else:
        row = self.rows
        for r in range(self.rows):
            up_point = self.row_lines[r] - ud_padding
            down_point = min(self.row_lines[r] + ud_padding, self.img_data.shape[0])
        
        for c in range(self.cols):
            key = (row, c + 1, up_point, self.col_lines[c])
            cut_images[key] = self.img_data[up_point:down_point, self.col_lines[c]:self.col_lines[c + 1], :].copy()
         
        return cut_images
    
    
    def grid_cut_safe(self, lr_padding, ud_padding):
    # def grid_cut_safe(self, lr_padding):
        cut_lr_images = {}
        cut_ud_images = {}

        cut_lr_images.update(self.grid_cut_safe_lr(lr_padding))

        cut_ud_images.update(self.grid_cut_safe_ud(ud_padding))



        
        # if self.section_idx[1] == 0 or self.section_idx[1] == 2:
        #     cut_lr_images.update(self.grid_cut_safe_lr('l', lr_padding))
        # elif self.section_idx[1] == 3:
        #     cut_lr_images.update(self.grid_cut_safe_lr('r', lr_padding))
            
        # if self.section_idx[0] == 0:
        #     cut_ud_images.update(self.grid_cut_safe_ud('u', ud_padding))
        # elif self.section_idx[0] == 2:
        #     cut_ud_images.update(self.grid_cut_safe_ud('d', ud_padding))
            
        return cut_lr_images,cut_ud_images
    

    def grid_cut_pian(self):
        # img_info = el_data.img_info
        img_data = self.img_data
        section_col = self.section_idx[1]
        rows, cols = self.rows, self.cols
        row_lines, col_lines = self.row_lines, self.col_lines

        # logging.warning('row_lines: %s, col_lines: %s', row_lines, col_lines)
        # cut_images = {}
        
        # cell_height =  self.row_lines[-1] - self.row_lines[-2] 
        # if  section_col== 0 or section_col== 2:
        #     col_list = list(range(1 , cols ))
        # else:
        #     col_list = list(range( cols))

        # x_pad = 135
        # for row in range(rows):
        #     for col in col_list:
        #         key = (row_lines[row], col_lines[col])
        #         left_point = max(col_lines[col] - x_pad, 0)
        #         right_point = min(col_lines[col] + x_pad, img_data.shape[1])
        #         cut_images[key] = cv2.transpose(img_data[row_lines[row]+ int(cell_height*shrink_value) :row_lines[row + 1] - int(cell_height*shrink_value), left_point:right_point, :])
        # logging.warning('cut_images_pian.keys: %s', cut_images.keys())
        logging.warning('row_lines: %s, col_lines: %s', row_lines, col_lines)
        logging.warning('rows: %s, cols: %s', rows, cols)
        cut_images = {}

        for row in range(rows):
            for col in range(0,cols,2):
                key = (row_lines[row], col_lines[col])
                img = img_data[row_lines[row]: row_lines[row+1], col_lines[col]: col_lines[col+2], :]
                cut_images[key] = img
        logging.warning('cut_images.keys: %s', cut_images.keys())

        return cut_images
        