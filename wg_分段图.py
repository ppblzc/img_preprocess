import cv2, os, glob, shutil, fire, random, time
from tqdm import tqdm
import numpy as np
from matplotlib import pyplot as plt

"""
根据拟合曲线的理念找到像素变化趋势。
"""

Data_parameters = {
    "data_dir": r"D:\repos\img_preprocess\data\output",  #包含img 的路径
    
}

   
class WG:
    def __init__(self):
        self.DEBUG = False
    
    def show_img(self,img,resize=[1000,500],img_name="show_img"):
        """
        根据是否开启debug,显示img
        """
        if self.DEBUG:
            img = cv2.resize(img, (resize[0], resize[1])) # col,row
            cv2.imshow(img_name, img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def show_plots(self,*args):
        """
        根据是否开启debug,显示plots
        """
        if self.DEBUG:
            for arg in args:
                plt.plot(arg)
            plt.show()
    
    def draw_lines(self,img,col_lines,row_lines,th =10):
        """
        绘制row、col 线
        """
        cols = len(col_lines)
        rows = len(row_lines)
        for i in range(0, int(cols)):
            cv2.line(img, (col_lines[i], 0),(col_lines[i], img.shape[0]), (0, 255, 0), th)
        for i in range(0, int(rows)):
            cv2.line(img, (0,row_lines[i]),(img.shape[1],row_lines[i]), (0, 255, 0), th)

        return img

    def save_cut(self,img,base,_col_lines,_row_lines):

        for i in range(len(_row_lines)-1):
            th = 2
            ts = str(time.time()).replace(".", "")
            for j in range(0,len(_col_lines)-2,2):
                # print(i,j)
                imgcut = img[_row_lines[i]-th:_row_lines[i+1]+th,_col_lines[j]-th:_col_lines[j+2]+th,:]
                # imgcut = cv2.resize(imgcut,(750,750))
                name = os.path.join(base,'save_double',ts+"^"+str(i)+str(j)+".jpg")
                cv2.imwrite(name,imgcut)
        # 片保存        
        # for i in range(0,len(_row_lines)-1,2):
        #     th = 2
        #     ts = str(time.time()).replace(".", "")
        #     for j in range(0,len(_col_lines)-2,1):
        #         # print(i,j)
        #         imgcut = img[_row_lines[i]-th:_row_lines[i+2]+th,_col_lines[j]-th:_col_lines[j+1]+th,:]
        #         # imgcut = cv2.resize(imgcut,(750,750))
        #         name = os.path.join(base,'save_double',ts+"^"+str(i)+str(j)+".jpg")
        #         cv2.imwrite(name,imgcut)

    def save_single_cut(self,img,base,lines):
        """根据分段图微调之后的lines"""
        ts = str(time.time()).replace(".", "")
        for i,v in enumerate(lines):
            # print(v,lines[v])
            _row_lines = lines[v][0]
            _col_lines = lines[v][1]
            th = 0
            # 分段图保存

            # img_cut = img[_row_lines[0]-th:_row_lines[-1]+th,_col_lines[0]-th:_col_lines[-1]+th].copy()
            # name = os.path.join(base,'save_fenduan',ts+"^"+str(i)+".jpg")
            # cv2.imwrite(name,img_cut)

            # 单片图保存

            # for i in range(len(_row_lines)-1):
            #     th = 2
            #     ts = str(time.time()).replace(".", "")
            #     for j in range(1,len(_col_lines)-1,1):
            #         imgcut = img[_row_lines[i]-th:_row_lines[i+1]+th,_col_lines[j]-th:_col_lines[j+1]+th,:]

            #         name = os.path.join(base,'save_single',ts+"^"+str(j)+".jpg")
            #         cv2.imwrite(name,imgcut)

            # 串保存        

            
        # print("1")
              
    def polyfit(self,y,fit):
        """
        修正孤立点,然后拟合直线
        """
        x = np.arange(len(y))
        y = y.copy() 
        #### 修正孤立点 ######
        counts = np.bincount((y/10).astype(np.uint8)*10+5) #统计每个值的数量
        counts[5] = 0
        counts[counts<np.sum(counts)/5] = 0
        th = np.where(counts>0)[0]
        if len(th) == 1:
            th = [th[0],th[0]]
        th[0] = th[0]-30
        y[y>th[-1]] = th[-1]
        y[y<(th[0])] = th[0]
        #### 拟合直线 ######
        f = np.polyfit(x, y, fit)
        p = np.poly1d(f)
        poly_fit = p(x)
        return poly_fit 

    def find_lines(self,plots,step=350):
        """
        plots: col or row
        step:350 or 700 
        """
        #################### 找到预选框 lines ###############################
        key = -1
        lines = []
        while True:
            th = plots[key+1] + step
            _key = key
            key = np.max(np.where(plots<th)[0])
            ########### 求范围内的均值###############
            if key == _key+1:
                mean = int(plots[key])
            else:
                mean = int((np.mean(plots[_key+1:key+1]))/1)
            lines.append(mean)
            ##### 最后一个跳出循环 ######
            if key == len(plots)-1:
                break        
        return np.array(lines)
         
    def get_col_lines(self,img):
        """
        分段拟合曲线修正坐标
        一层 col_lines, 尽量！！！保证拿到的全是精确的坐标
        二层 col_lines, 修补空洞处,插入汇流条线
        三层 col_lines, 比较精确点
        """
        img_col = (np.sum(img,axis=0)/img.shape[0])
        _img_col = img_col.copy()
        ##################### 通过分段拟合曲线修正坐标，使其更易处理 ######################
        Yvals = []
        for i in range(0,len(img_col),2760):
            yvals = self.polyfit(img_col[i:i+2760],1)   
            Yvals.extend(yvals)
        Yvals = np.array(Yvals)
        img_col = img_col-Yvals
        img_col[_img_col<5] = 0     # 去除边缘部分黑边影响
        img_col[img_col<=0]=0
        __img_col = img_col.copy()  # 精确的坐标
        self.show_plots(_img_col,Yvals,__img_col)
        ############################# 一层 col_lines #################################
        th = 30
        img_col[img_col<th] = 0
        img_col[img_col>=th] = 1
        img_col = np.where(img_col==1)[0]
        col_lines_1 = self.find_lines(img_col,step=350)
        ############################## 二层 col_lines  ##############################
        col_lines_2 = col_lines_1[0]
        for i in range(len(col_lines_1)-1):
            #### 平均值为350
            diff = col_lines_1[i+1]-col_lines_1[i]
            insert_col = np.linspace(col_lines_1[i],col_lines_1[i+1],int(diff/350)+1).astype(np.int64)[1:]
            col_lines_2 = np.hstack((col_lines_2,insert_col))
        len_col_lines_2 = int(len(col_lines_2)/2)
        # col_lines_2=np.insert(col_lines_2,len_col_lines_2,col_lines_2[len_col_lines_2])   ### 插入汇流条线
        # print("col_lines_2::",len(col_lines_2),col_lines_2)
        ################ 三层  __img_col 和 col_lines_2  坐标对比生成精确点 （待完善) ################
        col_lines_3 = col_lines_2
        for i in range(len(col_lines_3)):
            if i == 0:
                col = np.argmin(np.diff(__img_col[col_lines_3[i]:col_lines_3[i]+200])) 
                col_lines_3[i] = col_lines_3[i] + col
            elif i == len(col_lines_3)-1:
                col = np.argmax(np.diff(__img_col[col_lines_3[i]-200:col_lines_3[i]])) 
                col_lines_3[i] = col_lines_3[i]-200 + col
            # elif i == int(len(col_lines_3)/2-1):  
            #     col = np.argmax(np.diff(__img_col[col_lines_3[i]-70:col_lines_3[i]])) 
            #     col_lines_3[i] = col_lines_3[i]-70 + col
            # elif i == int(len(col_lines_3)/2):
            #     col = np.argmin(np.diff(__img_col[col_lines_3[i]:col_lines_3[i]+70])) 
            #     col_lines_3[i] = col_lines_3[i] + col    
            else:
                col = np.argmax(__img_col[col_lines_3[i]-100:col_lines_3[i]+100])
                col_lines_3[i] = col_lines_3[i]-100 + col
        ################################ 生成的点距离近,选错版型 (待完善)  ########################
        # print("get_col_lines:::done！")
        return col_lines_3

    def get_row_lines(self,img):
        """
        相比col的寻找，row受到焊线影响
        """
       
        img_row = (np.sum(img,axis=1)/img.shape[1])
        nums = 21
        kernel = np.ones((nums,nums),np.float32)/(nums*nums)
        img_row = cv2.filter2D(img_row,-1,kernel)[:,0]    
        _img_row = img_row.copy()
        ##################### 通过分段拟合曲线修正坐标，使其更易处理 ######################
        Yvals = []
        for i in range(0,len(img_row),1800):
            yvals = self.polyfit(img_row[i:i+1800],1)   
            Yvals.extend(yvals)
        Yvals = np.array(Yvals)
        img_row = img_row-Yvals
        img_row[_img_row<5] = 0     # 去除边缘部分黑边影响
        img_row[img_row<=0]=0
        __img_row = img_row.copy()  # 精确的坐标
        self.show_plots(img_row,Yvals,_img_row)
        ############################## 一层 row_lines #################################
        th = 30
        img_row[img_row<th] = 0
        img_row[img_row>=th] = 1
        img_row = np.where(img_row==1)[0]
        row_lines_1 = self.find_lines(img_row,step=700)
        ############################### 二层 row_lines  ##############################
        row_lines_2 = row_lines_1[0]
        for i in range(len(row_lines_1)-1):
            #### 平均值为700
            diff = row_lines_1[i+1]-row_lines_1[i]
            insert_row = np.linspace(row_lines_1[i],row_lines_1[i+1],int(diff/700)+1).astype(np.int64)[1:]
            row_lines_2 = np.hstack((row_lines_2,insert_row))
        ################# 三层  __img_row 和 row_lines_2  坐标对比生成精确点 （待完善)  坐标对比生成精确点 ################
        row_lines_3 = row_lines_2
        for i in range(len(row_lines_3)):
            if i == 0:
                row = np.argmin(np.diff(__img_row[row_lines_3[i]:row_lines_3[i]+200])) 
                row_lines_3[i] = row_lines_3[i] + row
            elif i == len(row_lines_3)-1:
                row = np.argmax(np.diff(__img_row[row_lines_3[i]-200:row_lines_3[i]])) 
                row_lines_3[i] = row_lines_3[i]-200 + row    
            else:
                row = np.argmax(__img_row[row_lines_3[i]-100:row_lines_3[i]+100])
                row_lines_3[i] = row_lines_3[i]-100 + row
        # ################################ 生成的点距离近，选错版型 (待完善)  ########################
        # print("最后!row_lines_3::",len(row_lines_3),row_lines_3)
        return row_lines_3

    def preprocess(self,img):
        """
        数据处理包含：
        - 从整图获得 col_lines、row_lines
        - 根据* 微调分段图的 col_lines、row_lines
        """
        ########## 从整图获得 col_lines、row_lines ##########
        col_lines = self.get_col_lines(img)
        row_lines = self.get_row_lines(img)
        draw = self.draw_lines(img.copy(),col_lines,row_lines,th=5)
        self.show_img(draw,resize=[1500,700],img_name="show_img")
        ########## 根据* 微调分段图的 col_lines、row_lines ##########
        # lines = self.adjust_by_fenduantu(img,col_lines,row_lines)

        return col_lines,row_lines

    def main(self):
        """
        main
        """
        ################################路径################################
        base= Data_parameters['data_dir']
        img_list = os.listdir(os.path.join(base,"img"))
        for i,b in enumerate(tqdm(img_list)):
            name = os.path.splitext(b)[0]
            img_path = os.path.join(base,'img',name+".jpg")
            print("图片",name)

            img = cv2.imread(img_path)
            img = cv2.resize(img,(2760,1800))
            img_for_cut = img.copy()
            img_gay = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            col_lines,row_lines = self.preprocess(img_gay)
            self.save_cut(img,base,col_lines,row_lines)


        print("done!")

if __name__ == "__main__":
    wg= WG()
    wg.main()