import os, glob, shutil,re,cv2
import numpy as np
import pickle
import time
import math
import scipy.signal as ss
from PIL import Image
from PIL import ImageFilter
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from collections import Counter


def argrelmax(x, order):
    rand = np.random.randn(len(x)) * 1e-3
    x1 = x + rand
    return ss.argrelmax(x1, order = order)


def argrelmin(x, order):
    rand = np.random.randn(len(x)) * 1e-3
    x1 = x + rand
    return ss.argrelmin(x1, order = order)

def get_point_by_lines(row_lines,col_lines):
    point_list = list()
    for row in row_lines:
        for col in col_lines:
            point_list.append([col,row ])
    return point_list

def get_intersection_by_lines(line_1,line_2):
    #print("line_1: " ,line_1)
    line_1_k = line_1[1][0] / line_1[0][0]
    line_1_b = line_1[3][0] - line_1_k * line_1[2][0]

    line_2_k = line_2[1][0] / line_2[0][0]
    line_2_b = line_2[3][0] - line_2_k * line_2[2][0]

    point_x = (line_2_b-line_1_b)/(line_1_k - line_2_k )
    point_y = line_1_k*point_x + line_1_b
    return point_x ,point_y


def padded_perspective_transform_one_image(img, dots, h, w, black_edge, pad=0.2):
    """
    根据选中四点与矩形高宽进行仿射变换
    :param img: 原图
    :param dots: 四点坐标（左上，右上，左下，右下）
    :param h, w: 仿射后矩形（高， 宽）
    :param black_edge: 串检切黑边True
    :returns: img_trans, pad_row_lines, pad_col_lines
    """
    pad_h, pad_w = int(h * pad), int(w * pad)
    dst = np.float32([
        [pad_w, pad_h],
        [pad_w + w, pad_h],
        [pad_w, pad_h + h],
        [pad_w + w, pad_h + h]])
    m = cv2.getPerspectiveTransform(dots.astype(np.float32), dst)
    size = (w + 2 * pad_w, h + 2 * pad_h)
    img_trans = cv2.warpPerspective(img, m, size)
    if black_edge:
        cut_xmin, cut_ymin, cut_xmax, cut_ymax = find_transform_edge(img_trans, pad_h, pad_w, h, w)
        pad_row_lines = [pad_h - cut_ymin, pad_h + h - cut_ymin]
        pad_col_lines = [pad_w - cut_xmin, pad_w + w - cut_xmin]

        return img_trans[cut_ymin:cut_ymax, cut_xmin:cut_xmax, :], pad_row_lines, pad_col_lines
    else:
        pad_row_lines = [pad_h, pad_h + h]
        pad_col_lines = [pad_w, pad_w + w]

        return img_trans, pad_row_lines, pad_col_lines

    
def calculate_points_distance(point_1,point_2):
    return math.pow(point_1[0]-point_2[0],2) +  math.pow(point_1[1]-point_2[1],2)


def get_points_distance(points_1,points_2):
    point_dict=dict()
    for i in range(4):
        point_dict[i]=calculate_points_distance(points_1[i],points_2[i])
    return point_dict


def normal_distribution(x, mean, sigma):
    return np.exp(-1*((x-mean)**2)/(2*(sigma**2)))/(math.sqrt(2*np.pi) * sigma)
      
    
def get_points(img,corners,v_alpha,h_alpha,part_row,part_col,loc_info_dict,mark):
    tem_points_list=list()
    point_dict = dict()
    
    img_roi = img[int(min(corners[0][1],corners[1][1]) -v_alpha):int(max(corners[2][1],corners[3][1]) + v_alpha) , \
                      int(min(corners[0][0],corners[2][0]) -h_alpha):int(max(corners[1][0],corners[3][0]) + h_alpha),:] 
    img_part_width  = int(img_roi.shape[0]/part_row)
    img_part_length = int(img_roi.shape[1]/part_col)

    for row in range(1,part_row+1):
        
        if (row-1)*img_part_width < 0:
            top_point=0
        else:
            top_point=(row-1)*img_part_width

        if row*img_part_width > img.shape[0]:
            bottom_point = img.shape[0]
        else:
            bottom_point = row*img_part_width 
        for col in range(1,part_col+1):
            tem_points_list=list()
            if (col - 1)*(img_part_length) < 0:
                left_point=0
            else:
                left_point=(col - 1)*img_part_length


            if col*img_part_length > img.shape[1]:
                right_point = img.shape[1]
            else:
                right_point = col*img_part_length

            img_cut = img_roi[top_point:bottom_point,left_point:right_point,:].copy()

            img_cut_gray = cv2.cvtColor(img_cut,cv2.COLOR_BGR2GRAY) 
            row_order = int(0.9*img_cut_gray.shape[0])
            col_order = int(0.9*img_cut_gray.shape[1])
            ret, th = cv2.threshold(img_cut_gray, 0, 255,cv2.THRESH_OTSU)
            img_cut_gray_erode = cv2.erode(img_cut_gray,None,iterations=4)

            _,contours,hierarchy = cv2.findContours(th,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
            draw = np.zeros((th.shape), np.uint8)
            area = []
            for i in range(len(contours)):
                area.append(cv2.contourArea(contours[i]))
            max_idx = np.argmax(area)

            cv2.fillConvexPoly(draw, contours[max_idx], 255)

            row_edge = normal_distribution(np.linspace(-3, 3, int(len(draw.mean(1))*0.08)), 0, 1)
            mean_fil_row_edge = np.convolve(draw.mean(1), row_edge, 'same')  
            
            max_row_flag = loc_info_dict[mark][str(row)+"_"+str(col)]['max_row_flag']
            min_row_flag = loc_info_dict[mark][str(row)+"_"+str(col)]['min_row_flag']
            max_col_flag = loc_info_dict[mark][str(row)+"_"+str(col)]['max_col_flag']
            min_col_flag = loc_info_dict[mark][str(row)+"_"+str(col)]['min_col_flag']                      

            if max_row_flag:
                row_lines_max_con = argrelmax(np.diff(mean_fil_row_edge), order = int(row_order))[0]
                row_lines_max_gray = argrelmax(np.diff(img_cut_gray_erode.mean(1)), order = int(row_order))[0]

            else:
                row_lines_max_con  = []
                row_lines_max_gray = []
            if min_row_flag:
                row_lines_min_con  = argrelmin(np.diff(mean_fil_row_edge), order = int(row_order))[0]  
                row_lines_min_gray = argrelmin(np.diff(img_cut_gray_erode.mean(1)), order = int(row_order))[0] 

            else:
                row_lines_min_con  = []
                row_lines_min_gray = []

            col_edge = normal_distribution(np.linspace(-3, 3, int(len(draw.mean(0))*0.08)), 0, 1)
            mean_fil_col_edge = np.convolve(draw.mean(0), col_edge, 'same')   
            if max_col_flag:
                col_lines_max_con  = argrelmax(np.diff(draw.mean(0)), order = int(col_order))[0]
                col_lines_max_gray = argrelmax(np.diff(img_cut_gray_erode.mean(0)), order = int(col_order))[0]

            else:
                col_lines_max_con  = []
                col_lines_max_gray = []
            if min_col_flag:
                col_lines_min_gray = argrelmin(np.diff(img_cut_gray_erode.mean(0)), order = int(col_order))[0]
                col_lines_min_con  = argrelmin(np.diff(draw.mean(0)), order = int(col_order))[0]

            else:
                col_lines_min_con  = []
                col_lines_min_gray = []
                                               
            row_lines_min_con[:] = [x+top_point for x in row_lines_min_con]  
            row_lines_max_con[:] = [x+top_point for x in row_lines_max_con]
            col_lines_min_con[:] = [x+left_point for x in col_lines_min_con]  
            col_lines_max_con[:] = [x+left_point for x in col_lines_max_con] 

            row_lines_min_gray[:] = [x+top_point for x in row_lines_min_gray]  
            row_lines_max_gray[:] = [x+top_point for x in row_lines_max_gray]
            col_lines_min_gray[:] = [x+left_point for x in col_lines_min_gray]  
            col_lines_max_gray[:] = [x+left_point for x in col_lines_max_gray] 

            tem_points_list.extend(get_point_by_lines(row_lines_max_con,col_lines_max_con))  
            tem_points_list.extend(get_point_by_lines(row_lines_max_con,col_lines_min_con))
            tem_points_list.extend(get_point_by_lines(row_lines_min_con,col_lines_max_con))
            tem_points_list.extend(get_point_by_lines(row_lines_min_con,col_lines_min_con))

            tem_points_list.extend(get_point_by_lines(row_lines_max_gray,col_lines_max_gray))  
            tem_points_list.extend(get_point_by_lines(row_lines_max_gray,col_lines_min_gray))
            tem_points_list.extend(get_point_by_lines(row_lines_min_gray,col_lines_max_gray))
            tem_points_list.extend(get_point_by_lines(row_lines_min_gray,col_lines_min_gray))
            point_dict[str(row) + '_' + str(col)] = tem_points_list
    return point_dict


def check_points(part_row,part_col,point_dict):
    for row in range(1,part_row+1):
        for col in range(1,part_col+1):
            tem_points_list=point_dict[str(row) + '_' + str(col)] 
            if len(np.array(tem_points_list))>1:

                clustering = DBSCAN(eps=30, min_samples=1).fit(np.array(tem_points_list))

                point_count = Counter(clustering.labels_)

                top_four_point = point_count.most_common(4)

                max_number = 0
                max_list=list()
                for i in range(len(point_count)):
                    if point_count[i] > max_number:
                        max_number = point_count[i]
                        max_list=list()
                        max_list.append(i)
                    if max_number == point_count[i]:
                        if i not in max_list:
                            max_list.append(i)

                if len(max_list)>1:
                    list_=list(clustering.labels_)
                    index_dict = dict()
                    max_list_len = 0
                    max_clustering_index = 8
                    for i in max_list:
                        index_list=list()
                        for j in range(len(list_)):
                            if list_[j] == i:
                                index_list.append(j)
                        index_dict[str(i)] = index_list
                    max_len = 0 
                    for i in range(len(index_dict)):
                        if len(index_dict[str(i)]) >max_len:
                            max_len = len(index_dict[str(i)])
                    count_flag = 0
                    for i in range(len(index_dict)):
                        if len(index_dict[str(i)]) ==max_len:
                            count_flag +=1 
                    if count_flag >1:

                        cluster_info_dict=dict()
                        for i in range(len(index_dict)):
                            tem_list=[]
                            for j in index_dict[str(i)]:
                                tem_list.append(tem_points_list[j])
                            cluster_info_dict[i] = tem_list
                        stand_stand_col_value_list = list()
                        stand_stand_row_value_list = list()
                        for stand_row in range(1,part_row+1):
                            if stand_row == row :
                                pass
                            else:
                                stand_stand_col_value_list.extend(point_dict[str(stand_row)+"_"+str(col)])
                                                                                          
                        stand_col_value = int(np.average(np.array(stand_stand_col_value_list)[:,0]))
                        for stand_col in range(1,part_col+1):
                            if stand_col == col :
                                pass
                            else:
                                stand_stand_row_value_list.extend(point_dict[str(row)+"_"+str(stand_col)])  
                        stand_row_value = int(np.average(np.array(stand_stand_row_value_list)[:,1]))

                        tem_processing_list=list()

                        for i in range(len(cluster_info_dict)):
                            x_average = int(np.average(np.array(cluster_info_dict[i])[:,0]))
                            y_average = int(np.average(np.array(cluster_info_dict[i])[:,1]))
                            if abs(x_average - stand_col_value) <30 and abs(y_average - stand_row_value) <30:
                                tem_processing_list.extend(cluster_info_dict[i])
                        point_dict[str(row)+"_"+str(col)] = tem_processing_list

                else:
                    if len(top_four_point) > 1:
                        tem_processing_list=list()
                        list_=list(clustering.labels_)
                        index_dict = dict()
                        for i in max_list:
                            index_list=list()
                            for j in range(len(list_)):
                                if list_[j] == i:
                                    index_list.append(j)
                            index_dict[str(i)] = index_list
                        cluster_info_dict=dict()
                        for i in range(len(index_dict)):
                            tem_list=[]
                            for j in index_dict[str(max_list[0])]:
                                tem_list.append(tem_points_list[j])
                            cluster_info_dict[str(i)] = tem_list
                        point_dict[str(row)+"_"+str(col)] = cluster_info_dict[str(0)]
    return point_dict


def fit_lines_by_points(point_dict,part_row,part_col):
    row_line_dict = dict()
    for y in range(1,part_row+1):
        row_list=list()
        for x in range(1,part_col+1):
            point_mark = str(y) + '_' + str(x)
            row_list.extend(point_dict[point_mark])
        row_array=np.array(row_list)
        if len(row_array) >0:
            [vy,vx,point_x,point_y] = cv2.fitLine(row_array, cv2.DIST_L1, 0, 0.01, 0.01)
            row_line_dict['row'+str(y)] = [vy,vx,point_x,point_y] 
    col_line_dict = dict()
    for x in range(1,part_col+1):  
        col_list=list()
        for y in range(1,part_row+1):
            point_mark = str(y) + '_' + str(x)
            col_list.extend(point_dict[point_mark])
        col_array=np.array(col_list)
        if len(col_array) > 0:
            [vx,vy,point_x,point_y] = cv2.fitLine(col_array, cv2.DIST_L1, 0, 0.01, 0.01)
            col_line_dict['col'+str(x)] = [vx,vy,point_x,point_y]
        else:
            col_line_dict['col'+str(x)] = [0,0,0,0]
    return row_line_dict,col_line_dict


def modify_corners_by_points(point_dict,row_line_dict,col_line_dict,corners,h_alpha,v_alpha,part_row,part_col):
    row_start = row_line_dict['row1']
    col_start = col_line_dict['col1']
    row_end = row_line_dict['row'+str(part_row)]
    col_end = col_line_dict['col'+str(part_col)]


    point_left_top_x,point_left_top_y = get_intersection_by_lines(row_start,col_start)
    point_left_bottom_x,point_left_bottom_y = get_intersection_by_lines(row_end,col_start)
    point_right_top_x,point_right_top_y = get_intersection_by_lines(row_start,col_end)
    point_right_bottom_x,point_right_bottom_y = get_intersection_by_lines(row_end,col_end)

    corners_= np.zeros((4,2))                           

    candidate_left_top_x_list = list()
    candidate_left_top_y_list = list()

    candidate_left_top_x_list.append(point_left_top_x )
    candidate_left_top_y_list.append(point_left_top_y )



    for point in point_dict["1_1"]:
        candidate_left_top_x_list.append(point[0])
        candidate_left_top_y_list.append(point[1])

    candidate_left_top_x_array = np.array(candidate_left_top_x_list,dtype = 'int64')
    candidate_left_top_y_array = np.array(candidate_left_top_y_list,dtype = 'int64')
    corners_[0][0] = np.average(candidate_left_top_x_array)
    corners_[0][1] = np.average(candidate_left_top_y_array)

#                 右上
    candidate_right_top_x_list = list()
    candidate_right_top_y_list = list()

    candidate_right_top_x_list.append(point_right_top_x )
    candidate_right_top_y_list.append(point_right_top_y )

    for point in point_dict["1_"+str(part_col)]:
        candidate_right_top_x_list.append(point[0])
        candidate_right_top_y_list.append(point[1])

    candidate_right_top_x_array = np.array(candidate_right_top_x_list,dtype = 'int64')
    candidate_right_top_y_array = np.array(candidate_right_top_y_list,dtype = 'int64')
    corners_[1][0] = np.average(candidate_right_top_x_array)
    corners_[1][1] = np.average(candidate_right_top_y_array)



#                 左下
    candidate_left_bottom_x_list = list()
    candidate_left_bottom_y_list = list()

    candidate_left_bottom_x_list.append(point_left_bottom_x )
    candidate_left_bottom_y_list.append(point_left_bottom_y )
    for point in point_dict[str(part_row)+"_1"]:
        candidate_left_bottom_x_list.append(point[0])
        candidate_left_bottom_y_list.append(point[1])

    candidate_left_bottom_x_array = np.array(candidate_left_bottom_x_list,dtype = 'int64')
    candidate_left_bottom_y_array = np.array(candidate_left_bottom_y_list,dtype = 'int64')
    corners_[2][0] = np.average(candidate_left_bottom_x_array)
    corners_[2][1] = np.average(candidate_left_bottom_y_array)



#                 右下
    candidate_right_bottom_x_list = list()
    candidate_right_bottom_y_list = list()

    candidate_right_bottom_x_list.append(point_right_bottom_x )
    candidate_right_bottom_y_list.append(point_right_bottom_y )
    for point in point_dict[str(part_row)+"_"+str(part_col)]:
        candidate_right_bottom_x_list.append(point[0])
        candidate_right_bottom_y_list.append(point[1])

    candidate_right_bottom_x_array = np.array(candidate_right_bottom_x_list,dtype = 'int64')
    candidate_right_bottom_y_array = np.array(candidate_right_bottom_y_list,dtype = 'int64')
    corners_[3][0] = np.average(candidate_right_bottom_x_array)
    corners_[3][1] = np.average(candidate_right_bottom_y_array)


    corners_ [0][0] +=  int(min(corners[0][0],corners[2][0]) -h_alpha)
    corners_ [0][1] +=  int(min(corners[0][1],corners[1][1]) -v_alpha)
    corners_ [1][0] +=  int(min(corners[0][0],corners[2][0]) -h_alpha)
    corners_ [1][1] +=  int(min(corners[0][1],corners[1][1]) -v_alpha)
    corners_ [2][0] +=  int(min(corners[0][0],corners[2][0]) -h_alpha)
    corners_ [2][1] +=  int(min(corners[0][1],corners[1][1]) -v_alpha)
    corners_ [3][0] +=  int(min(corners[0][0],corners[2][0]) -h_alpha)
    corners_ [3][1] +=  int(min(corners[0][1],corners[1][1]) -v_alpha)            

    corners_   = corners_.astype('int64')
    return corners_


def cut_edge(img):
    img_height=int(img.shape[0])
    img_width=int(img.shape[1])
    img_gray=cv2.cvtColor(img ,cv2.COLOR_RGB2GRAY)
    img_gray_left=img_gray[:,:int(img_width/2)]
    img_gray_right=img_gray[:,int(img_width/2):]
    
    img_gray_top=img_gray[:int(img_height/2),:]
    img_gray_bottom=img_gray[int(img_height/2):,:]
    
    left_alfa=len(np.argwhere(img_gray_left.mean(0)==0))
    right_alfa=len(np.argwhere(img_gray_right.mean(0)==0))
    top_alfa=len(np.argwhere(img_gray_top.mean(1)==0))
    bottom_alfa=len(np.argwhere(img_gray_bottom.mean(1)==0))
    
    left=0
    top=0
    right=img_width
    bottom=img_height
    
    
    if left_alfa!=0:
        left=left_alfa  
    if right_alfa!=0:
        right=img_width-right_alfa
    if top_alfa!=0:
        top=top_alfa
    if bottom_alfa!=0:
        bottom=img_height-bottom_alfa

    img_cut=img[top:bottom,left:right]
    return img_cut,left_alfa,top_alfa


def argrelmax(x, order):
    rand = np.random.randn(len(x)) * 1e-3
    x1 = x + rand
    return ss.argrelmax(x1, order = order)


def argrelmin(x, order):
    rand = np.random.randn(len(x)) * 1e-3
    x1 = x + rand
    return ss.argrelmin(x1, order = order)


def padded_perspective_transform_one_image(img, dots, h, w, black_edge, pad=0.2):
    """
    根据选中四点与矩形高宽进行仿射变换
    :param img: 原图
    :param dots: 四点坐标（左上，右上，左下，右下）
    :param h, w: 仿射后矩形（高， 宽）
    :param black_edge: 串检切黑边True
    :returns: img_trans, pad_row_lines, pad_col_lines
    """
    pad_h, pad_w = int(h * pad), int(w * pad)
    dst = np.float32([
        [pad_w, pad_h],
        [pad_w + w, pad_h],
        [pad_w, pad_h + h],
        [pad_w + w, pad_h + h]])
    m = cv2.getPerspectiveTransform(dots.astype(np.float32), dst)
    size = (w + 2 * pad_w, h + 2 * pad_h)
    img_trans = cv2.warpPerspective(img, m, size)
    if black_edge:
        cut_xmin, cut_ymin, cut_xmax, cut_ymax = find_transform_edge(img_trans, pad_h, pad_w, h, w)
        pad_row_lines = [pad_h - cut_ymin, pad_h + h - cut_ymin]
        pad_col_lines = [pad_w - cut_xmin, pad_w + w - cut_xmin]

        return img_trans[cut_ymin:cut_ymax, cut_xmin:cut_xmax, :], pad_row_lines, pad_col_lines
    else:
        pad_row_lines = [pad_h, pad_h + h]
        pad_col_lines = [pad_w, pad_w + w]

        return img_trans, pad_row_lines, pad_col_lines
    
    
def cut_edge(img):
    img_height=int(img.shape[0])
    img_width=int(img.shape[1])
    img_gray=cv2.cvtColor(img ,cv2.COLOR_RGB2GRAY)
    img_gray_left=img_gray[:,:int(img_width/2)]
    img_gray_right=img_gray[:,int(img_width/2):]
    
    img_gray_top=img_gray[:int(img_height/2),:]
    img_gray_bottom=img_gray[int(img_height/2):,:]
    
    left_alfa=len(np.argwhere(img_gray_left.mean(0)==0))
    right_alfa=len(np.argwhere(img_gray_right.mean(0)==0))
    top_alfa=len(np.argwhere(img_gray_top.mean(1)==0))
    bottom_alfa=len(np.argwhere(img_gray_bottom.mean(1)==0))
    
    left=0
    top=0
    right=img_width
    bottom=img_height
    
    
    if left_alfa!=0:
        left=left_alfa  
    if right_alfa!=0:
        right=img_width-right_alfa
    if top_alfa!=0:
        top=top_alfa
    if bottom_alfa!=0:
        bottom=img_height-bottom_alfa

    img_cut=img[top:bottom,left:right]
    return img_cut,left_alfa,top_alfa


def get_cell_lines(img_cut, cell_height, rows, cols):
    padded_row = cell_height // 2
    padded_col = cell_height // 4
        
    row_diff = np.diff(img_cut.mean(1)[padded_row : -padded_row])
    col_diff = np.diff(img_cut.mean(0)[padded_col : -padded_col])
        
    row_max = argrelmax(row_diff, order=int(cell_height * 0.8))[0]
    row_min = argrelmin(row_diff, order=int(cell_height * 0.8))[0]

    col_max = argrelmax(col_diff, order=int(cell_height / 2 * 0.8))[0]
    col_min = argrelmin(col_diff, order=int(cell_height / 2 * 0.8))[0]


    row_lines = (row_max + row_min) / 2 + padded_row
    col_lines = (col_max + col_min) / 2 + padded_col
    
    if abs(row_lines[0]-750) > 20:
        row_lines[0] = 750
    return row_lines.astype('int'), col_lines.astype('int')


def get_avg_cell_lines(img_cut, rows, cols):
    '''todo '''
    hh, ww = img_cut.shape[:2]
    stride_row, stride_col = int(hh/rows), int(ww/cols)
    row_lines_avg = [x*stride_row for x in range(rows)]
    row_lines_avg.append(hh-1)
    col_lines_avg = [x*stride_col for x in range(cols)]
    col_lines_avg.append(ww-1)

    return row_lines_avg, col_lines_avg


def get_busbar_edge( img, cell_width):
        h, w  = img.shape[:2]
        img_busbar = img[:, w - cell_width // 2:].copy()
        busbar_edge = argrelmax(np.diff(img_busbar.mean(0)), order=cell_width // 2)[0]

        return w - cell_width // 2 + busbar_edge[0]
    
def cell_lines_process(img,rows,cols, row_bias_0,row_bias_1,col_bias_0, col_bias_1,camera_num):

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_cut = img_gray[row_bias_0:row_bias_1, col_bias_0:col_bias_1]

    
    cell_height = 750
    if camera_num == 1:
        busbar_loc = get_busbar_edge(img_cut, cell_height // 2)
        busbar_loc += col_bias_0
        img_cut = img_cut[:, :busbar_loc].copy()
    
    try:
        cell_row_lines, cell_col_lines = get_cell_lines(img_cut,cell_height, rows, cols)
    except:
        cell_row_lines, cell_col_lines = get_avg_cell_lines(img_cut, rows, cols)
    
    if len(cell_row_lines)>(rows-1) or len(cell_col_lines)>(cols-1):
        cell_row_lines, cell_col_lines = get_avg_cell_lines(img_cut, rows, cols)
    row_lines = [y + row_bias_0 for y in cell_row_lines]
    col_lines = [x + col_bias_0 for x in cell_col_lines]
    row_lines.extend([row_bias_0, row_bias_1])
    col_lines.extend([col_bias_0, col_bias_1])

    if camera_num == 1:
        col_lines.append(busbar_loc)

    row_lines = sorted(row_lines)
    col_lines = sorted(col_lines)
    return row_lines, col_lines
