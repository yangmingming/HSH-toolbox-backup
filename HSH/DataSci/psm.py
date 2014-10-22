##encoding=utf8
##version =py27, py33
##author  =sanhe
##date    =2014-10-15

"""
============================================
Propensity score matching (PSM) 倾向评分匹配
============================================
PSM主要用于生物统计中。在生物统计中，很多实验都要设置
"对照组/控制组（control group）"和"实验组（treatment group）"。
在一个精心设计的实验中，对照组和实验组通常在除了实验所导致的结果
部分，都要保证其他情况尽量一致，这样实验结果才有说服力。例如我们
研究X药品对A疾病的治疗效果：

    如果我们选择100个病人，他们的身体状况都比较相似，给其中50个人
    吃药，另外50个人不吃药。如果过了一个月对照组中的病人有30%身体
    恶化，10%的状态不变，10%的稍许好转。而实验组中的病人有30%都有
    好转，那么我们大体上可以说明这个药是有效的。

    
而在实际的实验中我们通常做不到这一点。因为我们很难找到大量的状态
相似的实验对象。同样是X药品和A疾病的例子：

    我们在测试A药对B病的治疗效果，于是我们对1000名病病人做实验，
    其中50人吃了药，另外950人什么其他药也没吃。而在选择实验对象时，
    并没有对病人的其他身体情况做预先的调查。
    
    所以为了研究X药的有效性，我们必须从950个病人的对照组中选取
    合适的子集用来验证
    === 下面是sanhe自己的理解 ===
    选择子集的方式：
        方法1. 对于实验组中的每一个，分层或者不分层找寻k个knn近邻。
        然后最终我们得到k*50个样本集。
        所谓分层是：
            比如我们按年龄分层，那么我们在找k近邻时

参考文献
--------
    http://en.wikipedia.org/wiki/Propensity_score_matching
    R版本的实现，和测试数据
    http://cran.r-project.org/web/packages/MatchIt/MatchIt.pdf

=========================
PSM python implementation
=========================

Test Data Format
----------------
path = HSH\DataSci\demo_data\re78.csv
A data frame with 313 observations (185 treated, 429 control). There are 10 variables measured for
each individual. "treat" is the treatment assignment (1=treated, 0=control). "age" is age in years.
"educ" is education in number of years of schooling. "black" is an indicator for African-American
(1=African-American, 0=not). "hispan" is an indicator for being of Hispanic origin (1=Hispanic,
0=not). "married" is an indicator for married (1=married, 0=not married). "nodegree" is an indicator
for whether the individual has a high school degree (1=no degree, 0=degree). "re74" is income in
1974, in U.S. dollars. "re75" is income in 1975, in U.S. dollars. "re78" is income in 1978, in U.S.
dollars.

Import:
    from HSH.DataSci.psm import psm
"""

from __future__ import print_function
from ..LinearSpider.logger import Log
from ..Data.iterable import flatten_all
import pandas as pd
import knn_classifier

def psm(control, treatment, usecol = None, stratified_col = None, k = 1, enable_log = False):
    """
    [Args]
    ------
    control: [sample_1, sample_2, ..., sample_n]
        sample = [feature1, feature2, ..., feature_k]
    
    treatment: [sample_1, sample_2, ..., sample_n]
        sample = [feature1, feature2, ..., feature_k]
        
    k: number of matching sample
        how many samples been matching from control group
        for each sample in treatment
    """
    if usecol: # select the columns we gonna use
        control, treatment = (control.transpose()[usecol].transpose(),
                              treatment.transpose()[usecol].transpose() )
        
    std_control, std_treatment = knn_classifier.prep_standardize(control, treatment) # pre-processing standardization
    
    _, indices = knn_classifier.knn_find(std_control, 
                                         std_treatment, 
                                         k = len(std_control) ) # 更大的k值能保证确保匹配到足够的control sample
    
    if enable_log:
        log = Log()
        ## 处理index
        subcontrol_indice = set()
        for indice, t_sample in zip(indices, treatment): # indice = each sample
            matched_i = list() # 每一个treatment sample 所匹配到的list of control samples
            
            for ind in indice:
                if ind not in subcontrol_indice: # 如果不重复
                    subcontrol_indice.add(ind) 
                    matched_i.append(ind)
                    if len(matched_i) == k: # 对该treatment已经匹配到了足够的control samples
                        log.write("%s --matching-- %s" % (t_sample, control[matched_i]), enable_verbose=False)
                        break
                
        return control[list(subcontrol_indice)]
    