import os
import cv2
import pdb
import time
import numpy as np

def select_label(labels_datasets, feature_name, masks, scores, labels, bboxes):
    '''
    根据类别名称筛选检出
    '''
    label_idx = int(list(labels_datasets.keys())[list(labels_datasets.values()).index(feature_name)]) - 1
    feature_idx = np.where(labels == label_idx)[0]
    
    return masks[feature_idx], scores[feature_idx], bboxes[feature_idx]


def select_predictions(masks, scores, labels, bboxes, class_name, labels_datasets, keep_num, threshold):
    '''
    输出符合条件的cell mask
    条件:
    1. 类别
    2. 置信度
    '''
    try:
        s_masks, s_scores, s_bboxes = select_label(labels_datasets, class_name, masks, scores, labels, bboxes)
        keep_th = np.where(s_scores > threshold)[0]
        areas = np.squeeze(s_masks[keep_th].sum(axis=(1, 2)))
        keep_idx = np.argsort(areas)[-keep_num:]
        f_masks = s_masks[keep_th][keep_idx].astype(np.uint8)
        f_scores = s_scores[keep_th][keep_idx]
        f_bboxes = s_bboxes[keep_th][keep_idx]
    except:
        print('select {} masks failed'.format(class_name))
        return None, None, None
    if len(f_masks) != keep_num:
        print('select {} masks failed'.format(class_name))
        return None, None, None

    return f_masks, f_scores, f_bboxes


def micro_detector(masks, detect_step, rc_direction):
    '''
    按照方向计算最小最大值
    '''
    if rc_direction == 'r':
        detect_locs = np.linspace(0, masks.shape[0] - 1, detect_step).astype(np.int)
        dist = masks.shape[1] - np.sum(masks[detect_locs, :], axis = 1)
    else:
        detect_locs = np.linspace(0, masks.shape[1] - 1, detect_step).astype(np.int)
        dist = np.sum(masks[:, detect_locs], axis = 0)
        
    return int(np.quantile(dist, 0.25)), int(np.quantile(dist, 0.75))



def caculate_glass_cell(masks, scores, labels, bboxes, labels_datasets, direction, detect_step, glass_threshold, cell_threshold):
    '''
    计算电池片到边距离
    '''
    cell_masks, cell_scores, cell_bboxes = select_predictions(masks, scores, labels, bboxes, 'cell', labels_datasets, 1, cell_threshold)
    glass_masks, glass_scores, glass_bboxes = select_predictions(masks, scores, labels, bboxes, 'glass', labels_datasets, 1, glass_threshold)
    if cell_masks is None or glass_masks is None:
        return None, None, None
    sub_mask = cv2.subtract(glass_masks[0], cell_masks[0])
    
    if direction == 'd':
        glass_cell_min, glass_cell_max = micro_detector(sub_mask[10:, 80:-80], detect_step, 'c')
    else:
        glass_cell_min, glass_cell_max = micro_detector(sub_mask[:-10, 80:-80], detect_step, 'c')

    return sub_mask, glass_cell_min, glass_cell_max


def get_mid_masks(masks, scores, labels, bboxes, labels_datasets, cell_threshold):
    '''
    获得中间汇流条背景
    '''
    cell_masks, cell_scores, cell_bboxes = select_predictions(masks, scores, labels, bboxes, 'cell', labels_datasets, 2, cell_threshold)
    if cell_masks is None:
        return None
    sub_mask = 1 - cv2.add(cell_masks[0], cell_masks[1])
    
    return sub_mask


def caculate_busbar(masks, scores, labels, bboxes, busbar_name, labels_datasets, busbar_threshold, section_idx, row):
    '''
    计算汇流条是否缺失及距离
    1. 缺失后续距离不计算
    2. 不缺失但未通过筛选不计算
    '''
    # busbar miss
    busbar_miss = False
    try:
        obusbar_masks, obusbar_scores, obusbar_bboxes = select_label(labels_datasets, busbar_name, masks, scores, labels, bboxes)
    except:
        return True, None, None, None, None
    if len(obusbar_masks) == 0:
        busbar_miss = True
    busbar_masks, busbar_scores, busbar_bboxes = select_predictions(masks, scores, labels, bboxes, busbar_name, labels_datasets, 1, busbar_threshold)
    # busbar dist
    busbar_dist = None
    if busbar_masks is not None:
        if busbar_name == 'edge':
            if (section_idx[1] == 0 and row == 1) or (section_idx[1] == 3 and row == 2):
                busbar_dist = busbar_masks[0].shape[1] - busbar_bboxes[0][2]
            else:
                busbar_dist = busbar_bboxes[0][0]
        else:
            if section_idx[0] == 0 and row == 1:
                busbar_dist = busbar_masks[0].shape[1] - busbar_bboxes[0][2]
            elif section_idx[0] == 2 and row == 2:
                busbar_dist = busbar_bboxes[0][0]

    return busbar_miss, busbar_dist, busbar_masks, busbar_scores, busbar_bboxes


def caculate_edge_busbar(sub_mask, busbar_masks, busbar_bboxes, busbar_name, detect_step):
    '''
    若存在mask计算汇流条到边缘距离
    '''
    roi_masks = cv2.subtract(sub_mask, busbar_masks[0])
    mid_line = (busbar_bboxes[0][1] + busbar_bboxes[0][3]) // 2
    
    left_point = max(70, busbar_bboxes[0][0])
    right_point = min(busbar_masks[0].shape[1] - 70, busbar_bboxes[0][2])
    
    y_pad = 10 if busbar_name == 'mid' else 0
    up_roi_masks = roi_masks[y_pad:mid_line, left_point + 10:right_point - 10]
    down_roi_masks = roi_masks[mid_line:-10, left_point + 10:right_point - 10]
    
    up_busbar_min, up_busbar_max = micro_detector(up_roi_masks, detect_step, 'c')
    down_busbar_min, down_busbar_max = micro_detector(down_roi_masks, detect_step, 'c')
    
    return up_busbar_min, up_busbar_max, down_busbar_min, down_busbar_max


def detect_glass_cell(glass_cell_min, glass_cell_max, loc_key, w):
    '''
    返回电池片到边缘距离
    '''
    defects = []
    if loc_key[0] == 'u':
        class_name = 'glass_cell_ud_'
        coord = [loc_key[-1], loc_key[-2], loc_key[-1] + w, loc_key[-2] + 100]
    elif loc_key[0] == 'd':
        class_name = 'glass_cell_ud_'
        coord = [loc_key[-1], loc_key[-2] + 110, loc_key[-1] + w, loc_key[-2] + 210]
    elif loc_key[0] == 'l':
        class_name = 'glass_cell_lr_'
        coord = [loc_key[-1], loc_key[-2], loc_key[-1] + 100, loc_key[-2] + w]
    else:
        class_name = 'glass_cell_lr_'
        coord = [loc_key[-1] + 110, loc_key[-2], loc_key[-1] + 210, loc_key[-2] + w]
        
    defects.append({'class': class_name + 'min', 'loc': (loc_key[1], loc_key[2]), 'prob': 1, 'coord': coord, 'ext_features': {'dist': glass_cell_min}})
    defects.append({'class': class_name + 'max', 'loc': (loc_key[1], loc_key[2]), 'prob': 1, 'coord': coord, 'ext_features': {'dist': glass_cell_max}})
    
    return defects


def detect_busbar_miss(loc_key, w):
    '''
    返回汇流条缺失
    '''
    defects = []
    if loc_key[0] == 'l':
        coord = [loc_key[-1] + 80, loc_key[-2], loc_key[-1] + 110, loc_key[-2] + w]
    else:
        coord = [loc_key[-1] + 110, loc_key[-2], loc_key[-1] + 140, loc_key[-2] + w]
    
    defects.append({'class': 'busbar_miss', 'loc': (loc_key[1], loc_key[2]), 'prob': 1, 'coord': coord, 'ext_features': {}})
    
    return defects

    
def detect_busbar_dist(busbar_dist, class_name, loc_key, w):
    '''
    返回汇流条短-到顶端距离
    '''
    defects = []
    if loc_key[0] == 'l':
        coord = [loc_key[-1] + 80, loc_key[-2], loc_key[-1] + 110, loc_key[-2] + w]
    else:
        coord = [loc_key[-1] + 110, loc_key[-2], loc_key[-1] + 140, loc_key[-2] + w]  
    
    defects.append({'class': 'busbar_{}_dist'.format(class_name), 'loc': (loc_key[1], loc_key[2]), 'prob': 1, 'coord': coord, 'ext_features': {'dist': busbar_dist}})
    
    return defects


def detect_glass_cell_busbar(up_busbar_min, up_busbar_max, down_busbar_min, down_busbar_max, section_idx, loc_key, w, busbar_bbox):
    '''
    返回汇流条到边到电池片距离
    '''
    defects = []
    if section_idx[1] == 0:
        left_class_name = 'glass_edge_'
        right_class_name = 'edge_cell_'
    elif section_idx[1] == 3:
        left_class_name = 'edge_cell_'
        right_class_name = 'glass_edge_'
    else:
        left_class_name = 'mid_cell_'
        right_class_name = 'mid_cell_'
        
    if loc_key[0] == 'l':
        left_dist_min = up_busbar_min
        left_dist_max = up_busbar_max
        right_dist_min = down_busbar_min
        right_dist_max = down_busbar_max
        left_boundary = [loc_key[-1], loc_key[-1] + busbar_bbox[1]]
        right_boundary = [loc_key[-1] + busbar_bbox[3], loc_key[-1] + 220]
    else:
        left_dist_min = down_busbar_min
        left_dist_max = down_busbar_max
        right_dist_min = up_busbar_min
        right_dist_max = up_busbar_max
        left_boundary = [loc_key[-1], loc_key[-1] + 220 - busbar_bbox[3]]
        right_boundary = [loc_key[-1] + 220 - busbar_bbox[1], loc_key[-1] + 220]
        
    defects.append({'class': left_class_name + 'min', 'loc': (loc_key[1], loc_key[2]), 'prob': 1, 'coord': [left_boundary[0], loc_key[-2], left_boundary[1], loc_key[-2] + w], 'ext_features': {'dist': left_dist_min}})
    defects.append({'class': left_class_name + 'max', 'loc': (loc_key[1], loc_key[2]), 'prob': 1, 'coord': [left_boundary[0], loc_key[-2], left_boundary[1], loc_key[-2] + w], 'ext_features': {'dist': left_dist_max}})
    
    defects.append({'class': right_class_name + 'min', 'loc': (loc_key[1], loc_key[2]), 'prob': 1, 'coord': [right_boundary[0], loc_key[-2], right_boundary[1], loc_key[-2] + w], 'ext_features': {'dist': right_dist_min}})
    defects.append({'class': right_class_name + 'max', 'loc': (loc_key[1], loc_key[2]), 'prob': 1, 'coord': [right_boundary[0], loc_key[-2], right_boundary[1], loc_key[-2] + w], 'ext_features': {'dist': right_dist_max}})
    
    return defects


def detect_mini(demo, im):
    '''
    处理检测结果
    '''
    predictions = demo.run_on_image(im)
    labels = predictions.pred_classes.numpy()
    scores = predictions.scores.numpy()
    masks = predictions.pred_masks.numpy()
    bboxes = predictions.pred_boxes.tensor.numpy().astype('int')
    
    return masks, scores, labels, bboxes


def plot_mini(img, masks, scores, labels, bboxes):
    '''
    绘制mask结果
    '''
    color_list = [[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 0], [255, 0, 255], [0, 255, 255]]
    painter = np.zeros_like(img).astype(np.uint8)
    for i in range(len(scores)):
        mask = masks[i]
        score = scores[i]
        label = labels[i]
        bbox = bboxes[i]
        temp = np.zeros_like(img)
        temp[mask] = color_list[label]
        painter = cv2.add(painter, temp)
        img = cv2.rectangle(img, (bbox[0], bbox[1]), (bbox[2], bbox[3]), tuple(color_list[label]), 1)
        cv2.putText(img, str(score), (bbox[0], bbox[1]), cv2.FONT_HERSHEY_COMPLEX, 1, tuple(color_list[label]), 2)
        
    return cv2.addWeighted(img, 0.5, painter, 0.5, 0)
        
    
    
def detector(demo, img_name, img_cut_folder, save_folder, cut_ud_images, cut_lr_images, labels_datasets, section_idx, glass_threshold, cell_threshold, edge_threshold, mid_threshold, detect_step):
    '''
    最终检测
    '''
    defects = []
    
    # 检测上下电池片到边缘距离
    for key, ud_image in cut_ud_images.items():
        #
        cv2.imwrite(os.path.join(img_cut_folder, '{}-{}.jpg'.format(img_name, str(key))), ud_image)
        #
        print('start up and down {} image detect'.format(key))
        w = ud_image.shape[1]
        masks, scores, labels, bboxes = detect_mini(demo, ud_image)
        if isinstance(bboxes, type(None)):
            continue
        if len(bboxes) == 0:
            continue   
        #
        cv2.imwrite(os.path.join(save_folder, '{}-{}.jpg'.format(img_name, str(key))), plot_mini(ud_image, masks, scores, labels, bboxes))
        #
        
        sub_mask, glass_cell_min, glass_cell_max = caculate_glass_cell(masks, scores, labels, bboxes, labels_datasets, key[0], detect_step, glass_threshold, cell_threshold)
        if sub_mask is not None:
            mini_ud_defects = detect_glass_cell(glass_cell_min, glass_cell_max, key, w)
            defects.extend(mini_ud_defects)
            print('finish up and down {} image detect with defects {}'.format(key, mini_ud_defects))
        else:
            continue

    # 检测含汇流条部分距离
    for key, lr_image in cut_lr_images.items():
        #
        cv2.imwrite(os.path.join(img_cut_folder, '{}-{}.jpg'.format(img_name, str(key))), lr_image)
        #
        print('start left and right {} image detect'.format(key))
        w = lr_image.shape[1]
        masks, scores, labels, bboxes = detect_mini(demo, lr_image)
        if isinstance(bboxes, type(None)):
            continue
        if len(bboxes) == 0:
            continue
        #
        cv2.imwrite(os.path.join(save_folder, '{}-{}.jpg'.format(img_name, str(key))), plot_mini(lr_image, masks, scores, labels, bboxes))
        #
        
        if section_idx[1] != 2:
            sub_mask, glass_cell_min, glass_cell_max = caculate_glass_cell(masks, scores, labels, bboxes, labels_datasets, key[0], detect_step, glass_threshold, cell_threshold)
            if sub_mask is not None:
                mini_lr_gc_defects = detect_glass_cell(glass_cell_min, glass_cell_max, key, w)
                defects.extend(mini_lr_gc_defects)
                print('finish left and right {} image edge detect with defects {}'.format(key, mini_lr_gc_defects))
            busbar_name = 'edge'
            busbar_threshold = edge_threshold
        else:
            sub_mask = get_mid_masks(masks, scores, labels, bboxes, labels_datasets, cell_threshold)
            busbar_name = 'mid'
            busbar_threshold = mid_threshold
        
        busbar_miss, busbar_dist, busbar_masks, busbar_scores, busbar_bboxes = caculate_busbar(masks, scores, labels, bboxes, busbar_name, labels_datasets, busbar_threshold, section_idx, key[1])

        if busbar_miss:
            mini_lr_miss_defects = detect_busbar_miss(key, w)
            defects.extend(mini_lr_miss_defects)
            print('finish left and right {} image busbar miss detect with defects {}'.format(key, mini_lr_miss_defects))

        if busbar_dist is not None:
            mini_lr_dist_defects = detect_busbar_dist(busbar_dist, busbar_name, key, w)
            defects.extend(mini_lr_dist_defects)
            print('finish left and right {} image busbar dist detect with defects {}'.format(key, mini_lr_dist_defects))
            
        if (sub_mask is not None) and (busbar_masks is not None):
            up_busbar_min, up_busbar_max, down_busbar_min, down_busbar_max = caculate_edge_busbar(sub_mask, busbar_masks, busbar_bboxes, busbar_name, detect_step)
            mini_lr_busbar_defects = detect_glass_cell_busbar(up_busbar_min, up_busbar_max, down_busbar_min, down_busbar_max, section_idx, key, w, busbar_bboxes[0])
            defects.extend(mini_lr_busbar_defects)
            print('finish left and right {} image busbar edge cell detect with defects {}'.format(key, mini_lr_busbar_defects))
                
    return defects
