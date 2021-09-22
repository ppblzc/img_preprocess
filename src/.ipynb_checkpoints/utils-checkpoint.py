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
        
        
    def grid_cut_safe_lr(self, direction, lr_padding):
        cut_images = {}
        if direction == 'l':
            col = 1
            left_point = max(0, self.col_lines[0] - lr_padding)
            right_point = self.col_lines[0] + lr_padding
        else:
            col = self.cols
            left_point = self.col_lines[-1] - lr_padding
            right_point = min(self.col_lines[-1] + lr_padding, self.img_data.shape[1])
            
        for r in range(self.rows):
            key = (direction, r + 1, col, self.row_lines[r], left_point)
            img_cut = self.img_data[self.row_lines[r]:self.row_lines[r + 1], left_point:right_point, :].copy()
            if direction == 'l':
                cut_images[key] = cv2.flip(cv2.transpose(img_cut), 1)
            else:
                cut_images[key] = cv2.flip(cv2.transpose(img_cut), 0)
            
        return cut_images
    
    
    def grid_cut_safe_ud(self, direction, ud_padding):
        cut_images = {}
        if direction == 'u':
            row = 1
            up_point = max(0, self.row_lines[0] - ud_padding)
            down_point = self.row_lines[0] + ud_padding
        else:
            row = self.rows
            up_point = self.row_lines[-1] - ud_padding
            down_point = min(self.row_lines[-1] + ud_padding, self.img_data.shape[0])
        
        for c in range(self.cols):
            key = (direction, row, c + 1, up_point, self.col_lines[c])
            cut_images[key] = self.img_data[up_point:down_point, self.col_lines[c]:self.col_lines[c + 1], :].copy()
         
        return cut_images
    
    
    def grid_cut_safe(self, lr_padding, ud_padding):
        cut_lr_images = {}
        cut_ud_images = {}
        
        if self.section_idx[1] == 0 or self.section_idx[1] == 2:
            cut_lr_images.update(self.grid_cut_safe_lr('l', lr_padding))
        elif self.section_idx[1] == 3:
            cut_lr_images.update(self.grid_cut_safe_lr('r', lr_padding))
            
        if self.section_idx[0] == 0:
            cut_ud_images.update(self.grid_cut_safe_ud('u', ud_padding))
        elif self.section_idx[0] == 2:
            cut_ud_images.update(self.grid_cut_safe_ud('d', ud_padding))
            
        return cut_lr_images, cut_ud_images
    