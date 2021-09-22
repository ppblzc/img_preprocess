import os, glob, shutil, re, cv2
import pickle
from src.common.loc_info_dict import get_loc_info_dict
from src.common import function
import numpy as np

def get_mark(img_name):
    if int(img_name.split('_')[-1]) // 4 == 0:
        s = 'A'
        d = 0
    elif int(img_name.split('_')[-1]) // 4 == 1:
        s = 'B'
        d = 1
    else:
        s = 'C'
        d = 2
    camera_num = int(img_name.split('_')[-1]) % 4 + 1
    return s + str(camera_num),  [d, camera_num - 1]


def undistort(undistort_path, img, col):
    distort_matrix = pickle.load(open(undistort_path, "rb"))                                                                
    mtx, dist = distort_matrix["camera" + str(col)]["mtx"], distort_matrix["camera" + str(col)]["dist"]
    dst = cv2.undistort(img, mtx, dist, None, mtx)
    return dst
        
        
def pre_process(file_path, undistort_path, concat_path, col_list):                                       
    rows = 2  #分段图电池片行数
    h = rows * 750 #透视参数 ，宽度
    v_alpha = 70 #拼图竖直pad大小
    h_alpha = 70 #拼图水平 pad 大小
    
    img_name = os.path.splitext(os.path.basename(file_path))[0]
    mark, section_idx = get_mark(img_name)
    
     # wg图序mark ——> zj图序mark,由于正畸的逻辑不同，需进行映射
    mark_dict={'A1': 'D3','A2':'C3' ,'A3':'B3' ,'A4':'A3' ,'B1':'D2' ,'B2':'C2' ,'B3':'B2' ,'B4':'A2' ,'C1':'D1' ,'C2':'C1' ,'C3':'B1' ,'C4':'A1' }
    camera_number = int(mark_dict[mark][1]) - 1

    img = cv2.imread(file_path)
    img_resize = cv2.resize(img, (2754, 1836), interpolation=cv2.INTER_CUBIC)
    # img_dst = undistort(undistort_path, img_resize, str(section_idx[1]))
    img_dst = undistort(undistort_path, img_resize, str(camera_number))
    
    print("name: ", img_name)
    cols = col_list[section_idx[1]]
    part_row = rows + 1
    part_col = cols + 1
    distort_matrix = pickle.load(open(concat_path, "rb" ))
    center_coordinates = distort_matrix[mark]['Perspective_parameters'][0].astype('uint64')
    try:
        loc_info_dict = get_loc_info_dict(col_list)                                                        

        point_dict = function.get_points(img_dst, center_coordinates, v_alpha, h_alpha, part_row, part_col, loc_info_dict, mark)
        point_dict = function.check_points(part_row, part_col, point_dict)
        row_line_dict, col_line_dict = function.fit_lines_by_points(point_dict, part_row, part_col)

        corners_ = function.modify_corners_by_points(point_dict, row_line_dict, col_line_dict, center_coordinates, h_alpha, v_alpha, part_row, part_col)
    except:
        corners_ = center_coordinates
        print("find corncerns error")

    w = 375 * cols
    pers_transed_img, pad_row_lines, pad_col_lines = function.padded_perspective_transform_one_image(img_dst, corners_, h, w, False , 0.3)
    img_cut, left_alfa, top_alfa = function.cut_edge(pers_transed_img)
    dots = np.zeros((4,2))
    dots[0][0] = pad_col_lines[0]
    dots[0][1] = pad_row_lines[0]
    dots[1][0] = pad_col_lines[1]
    dots[1][1] = pad_row_lines[0]
    dots[2][0] = pad_col_lines[0]
    dots[2][1] = pad_row_lines[1]
    dots[3][0] = pad_col_lines[1]
    dots[3][1] = pad_row_lines[1]

    row_bias_0 = int(dots[0][1]) - top_alfa
    row_bias_1 = int(dots[3][1]) - top_alfa
    col_bias_0 = int(dots[0][0]) - left_alfa
    col_bias_1 = int(dots[1][0]) - left_alfa

    row_lines, col_lines = function.cell_lines_process(img_cut, rows, cols, row_bias_0, row_bias_1, col_bias_0, col_bias_1, section_idx[1])
    print("-------------------------row_lines-------------------------------------------------------")
    print(row_lines)
    print("-------------------------col_lines-------------------------------------------------------")
    print(col_lines)
    print("-------------------------go on------------------------------")
    
    el_data = {}
    el_data['img_info'] = {}
    el_data['img_info']['rows'] = rows
    el_data['img_info']['cols'] = cols
    el_data['img_info']['row_lines'] = row_lines
    el_data['img_info']['col_lines'] = col_lines
    el_data['img_info']['img_cv2'] = img_cut
    el_data['img_info']['section_idx'] = section_idx
    
    return el_data
