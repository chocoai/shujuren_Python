import jieba
seg_list1 = jieba.cut("购物中心和品牌", cut_all=True)
print("Full Mode: " + "/".join(seg_list1))

seg_list2 = jieba.cut("购物中心和品牌", cut_all=False)
print("Default Mode: " + "/".join(seg_list2)) # 精确模式，适用文本分析，默认是精确模式

seg_list3 = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print(", ".join(seg_list3))




