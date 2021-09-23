import os
import sys
import yaml
import json
import cv2
import time
import glob
import shutil
import numpy as np
# sys.path.append('/home/detectron2_repo/projects/PointRend')
from detectron2.config import get_cfg
# from point_rend import add_pointrend_config

from src.common.pre_process import pre_process
from src.utils import GridCutSafe, get_logger
from src.predictor import VisualizationDemo
# from src.detect_safedistance import detect_mini, plot_mini, detector

logger = get_logger()


class Config:
    def __init__(self, config_path):
        self.config_path = config_path

        self.yml_str = None

        self.INFO = None
        self.PRE_PROCESS = None
        self.IMG_CUT_FOLDER = None
        self.OUTPUT_FOLDER = None
        self.MODEL = None
        self.IMG_TYPE = None
        self.is_valid = self.check_if_valid()

    def check_if_valid(self):
        '''
        确认配置文件的正确性
        :param yml_str:
        :return:
        '''
        if not os.path.exists(self.config_path):
            logger.info('the configuration file: {} is not exists!'.format(self.config_path))
            return 1

        # 读取配置文件
        self.yml_str = open(self.config_path).read()
        try:
            cfg_info = yaml.load(self.yml_str, Loader=yaml.FullLoader)

            self.INFO = cfg_info['info']

            self.PRE_PROCESS = cfg_info['pre_process']

            self.IMG_CUT_FOLDER = cfg_info['img_folder']
            self.OUTPUT_FOLDER = cfg_info['output_folder']

            self.MODEL = cfg_info['model']
            
            self.IMG_TYPE = cfg_info['img_type']
        except:
            logger.info('failed to read configuration file')
            return 1

        # 有前处理时：
        if self.PRE_PROCESS['switch'] is True:
            # 判断前处理文件夹是否存在
            if not os.path.exists(self.PRE_PROCESS['origin_folder']):
                logger.info('path: {} not exists!'.format(self.PRE_PROCESS['origin_folder']))
                return 1
        else:
            if not os.path.exists(self.IMG_CUT_FOLDER):
                # 判断图片输入路径是否存在
                logger.info('path: {} not exists!'.format(self.IMG_CUT_FOLDER))
                return 1

        # 判断模型路径是否存在
        # for i in self.MODEL.values():
        #     if not os.path.exists(i['model_dir']):
        #         logger.info('path: {} not exists!'.format(i['model_dir']))
        #         return 1

        # 创建输出文件夹
        if os.path.exists(self.OUTPUT_FOLDER):
            shutil.rmtree(self.OUTPUT_FOLDER)
        os.mkdir(self.OUTPUT_FOLDER)
        os.mkdir(os.path.join(self.OUTPUT_FOLDER, 'masks'))
        os.mkdir(os.path.join(self.OUTPUT_FOLDER, 'dists'))
        os.mkdir(os.path.join(self.OUTPUT_FOLDER, 'preprocessed'))

        # 再次查看配置信息正确性
        logger.info('\n\n>>>>>>>>----------------------------------------------------------------<<<<<<<<\n')
        logger.info(self.yml_str)
        logger.info('\n>>>>>>>>----------------------------------------------------------------<<<<<<<<\n\n')

        answer = input('Is the configuration file correct? [yes/no]:')
        while answer.upper() not in ['YES', 'Y', 'NO', 'N']:
            logger.info('Please input yes or no!')
            answer = input()

        if answer.upper() in ['YES', 'Y']:
            return 0
        else:
            return 1


# def model_init(model_dir):
#     config_file = os.path.join(model_dir, 'configs/pointrend_rcnn_R_50_FPN_1x_coco.yaml')
#     weights = os.path.join(model_dir, 'output/model_final.pth')
#     cfg = get_cfg()
#     add_pointrend_config(cfg)
#     cfg.merge_from_file(config_file)
#     # manual override some options
#     cfg.merge_from_list(["MODEL.DEVICE", "cuda"])
#     cfg.merge_from_list(["MODEL.WEIGHTS", weights])
#     cfg.freeze()
#     demo = VisualizationDemo(cfg)

#     with open(os.path.join(model_dir, 'output/labels.json'), 'r') as f:
#         labels_datasets = json.load(f)
        
#     return demo, labels_datasets


def plot_dists(img, defects):
    defects1 = {'busbar_miss': [255, 0, 0], 'glass_cell_ud_max': [0, 255, 0]}
    defects2 = {'busbar_edge_dist': [0, 0, 255], 'busbar_mid_dist': [255, 255, 0]}
    defects3 = {'mid_cell_max': [0, 255, 255], 'glass_edge_max': [170, 170, 0], 'edge_cell_max': [170, 0, 170]}
    defects4 = {'glass_cell_lr_max': [0, 170, 170]}
    img1 = img.copy()
    img2 = img.copy()
    img3 = img.copy()
    img4 = img.copy()
    for d in defects:
        if d['class'] in list(defects1.keys()):
            img1 = cv2.rectangle(img1, (d['coord'][0], d['coord'][1]), (d['coord'][2], d['coord'][3]), tuple(defects1[d['class']]), 2)
            img1 = cv2.putText(img1, d['class'], (d['coord'][0], d['coord'][1]), cv2.FONT_HERSHEY_SIMPLEX, 1, tuple(defects1[d['class']]), 2)
        elif d['class'] in list(defects2.keys()):
            img2 = cv2.rectangle(img2, (d['coord'][0], d['coord'][1]), (d['coord'][2], d['coord'][3]), tuple(defects2[d['class']]), 2)
            img2 = cv2.putText(img2, d['class'], (d['coord'][0], d['coord'][1]), cv2.FONT_HERSHEY_SIMPLEX, 1, tuple(defects2[d['class']]), 2)
        elif d['class'] in list(defects3.keys()):
            img3 = cv2.rectangle(img3, (d['coord'][0], d['coord'][1]), (d['coord'][2], d['coord'][3]), tuple(defects3[d['class']]), 2)
            img3 = cv2.putText(img3, d['class'], (d['coord'][0], d['coord'][1]), cv2.FONT_HERSHEY_SIMPLEX, 1, tuple(defects3[d['class']]), 2)
        elif d['class'] in list(defects4.keys()):
            img4 = cv2.rectangle(img4, (d['coord'][0], d['coord'][1]), (d['coord'][2], d['coord'][3]), tuple(defects4[d['class']]), 2)
            img4 = cv2.putText(img4, d['class'], (d['coord'][0], d['coord'][1]), cv2.FONT_HERSHEY_SIMPLEX, 1, tuple(defects4[d['class']]), 2)
    return img1, img2, img3, img4


def main():
    '''
    main function
    :return:
    '''
    # --------------------------------------------------------
    # 一、读取配置文件
    # 1.1 检查配置文件是否准确
    # 1.2 正确则读取配置文件
    # 1.3 从配置文件中获取模型相关信息，主要是：缺陷类型，置信度，模型路径
    config_path = r'config/config.yml'
    cfgs = Config(config_path)
    if cfgs.is_valid:
        logger.info('Please modify the configuration file!')
        exit(0)
    
    # --------------------------------------------------------
    # 二、模型初始化
    # MODEL = cfgs.MODEL['safe']
    # glass_threshold = MODEL['threshold']['glass']
    # cell_threshold = MODEL['threshold']['cell']
    # edge_threshold = MODEL['threshold']['edge']
    # mid_threshold = MODEL['threshold']['mid']
    # demo, labels_datasets = model_init(MODEL['model_dir'])
    # logger.info('[PART2]!!!start model init with {}'.format(str(labels_datasets)))
    
    # --------------------------------------------------------
    # 三、模型检测
    PRE_PROCESS = cfgs.PRE_PROCESS
    if PRE_PROCESS['switch']:
        # 如果存在小图文件夹，先删除再新建
        if os.path.exists(cfgs.IMG_CUT_FOLDER):
            shutil.rmtree(cfgs.IMG_CUT_FOLDER)
        os.mkdir(cfgs.IMG_CUT_FOLDER)
        img_list = glob.glob(os.path.join(PRE_PROCESS['origin_folder'], '*.{}'.format(cfgs.IMG_TYPE)))
        img_len = len(img_list)
        for i, img in enumerate(img_list):
            img_name = os.path.splitext(os.path.basename(img))[0]
            logger.info('[{}/{}] --------------> start predictor ------------->'.format(i+1, img_len))
            try:
                undistort_path = PRE_PROCESS['size']['undistort']
                concat_path = PRE_PROCESS['size']['concat']
                print('---------hi 2------------- ')
                col_list = PRE_PROCESS['size']['col_list']
                print('---------hi 3------------- ')
                el_data = pre_process(img, undistort_path, concat_path, col_list)         # error
                print('---------hi 4------------- ')
                img_data = el_data['img_info']['img_cv2']
                cv2.imwrite(os.path.join(cfgs.OUTPUT_FOLDER, 'preprocessed', '{}.jpg'.format(img_name)), img_data)  # + 保存正畸、透视、切黑边、resize的图
                print('img_data:',img_data.shape)
                grid_cuttor = GridCutSafe(el_data)
                print('---------hi 5------------- ')
                cut_lr_images, cut_ud_images = grid_cuttor.grid_cut_safe(110, 110)
                #cut_lr_images = grid_cuttor.grid_cut_safe(110)
                for key, lr_image in cut_lr_images.items():
                    cv2.imwrite(os.path.join(cfgs.IMG_CUT_FOLDER, '{}-{}.jpg'.format(img_name, str(key))), lr_image)
                for key, ud_image in cut_ud_images.items():
                    cv2.imwrite(os.path.join(cfgs.IMG_CUT_FOLDER, '{}-{}.jpg'.format(img_name, str(key))), ud_image)

                # defects = detector(demo, img_name, cfgs.IMG_CUT_FOLDER, os.path.join(cfgs.OUTPUT_FOLDER, 'masks'), cut_ud_images, cut_lr_images, labels_datasets, \
                #                    grid_cuttor.section_idx, glass_threshold, cell_threshold, edge_threshold, mid_threshold, 15)
                # img1, img2, img3, img4 = plot_dists(img_data, defects)
                # cv2.imwrite(os.path.join(cfgs.OUTPUT_FOLDER, 'dists', '{}-1.jpg'.format(img_name)), img1)
                # cv2.imwrite(os.path.join(cfgs.OUTPUT_FOLDER, 'dists', '{}-2.jpg'.format(img_name)), img2)
                # cv2.imwrite(os.path.join(cfgs.OUTPUT_FOLDER, 'dists', '{}-3.jpg'.format(img_name)), img3)
                # cv2.imwrite(os.path.join(cfgs.OUTPUT_FOLDER, 'dists', '{}-4.jpg'.format(img_name)), img4)
                # logger.info('defects {}'.format(defects))
            except:
                print('---------pre-process error------------- ')                                                       #+
            logger.info('[{}/{}] --------------> finish predictor ------------->'.format(i+1, img_len))
            
    else:
        # img_list = glob.glob(os.path.join(cfgs.IMG_CUT_FOLDER, '*.{}'.format(cfgs.IMG_TYPE)))
        # img_len = len(img_list)
        # for i, img in enumerate(img_list):
        #     img_name = os.path.splitext(os.path.basename(img))[0]
        #     logger.info('[{}/{}] --------------> start predictor ------------->'.format(i+1, img_len))
        #     try:
        #         img_data = cv2.imread(img)
        #         masks, scores, labels, bboxes = detect_mini(demo, img_data)
        #         cv2.imwrite(os.path.join(cfgs.OUTPUT_FOLDER, 'masks', '{}.jpg'.format(img_name)), plot_min(ud_image, masks, scores, labels, bboxes))
        #     except:
        #         pass
        #     logger.info('[{}/{}] --------------> finish predictor ------------->'.format(i+1, img_len))
        pass    
if __name__ == "__main__":
    main()