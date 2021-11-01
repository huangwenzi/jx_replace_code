import os

# 执行sh


# 热更代码
def reload(tar_dir, file_list):
    old_cwd = os.getcwd()
    # 移动到目标目录
    os.chdir(tar_dir)
    for item in file_list:
        # 去掉尾缀
        item = os.path.basename(item)
        item= item.split('.')[0]
        os.system('sh gamectl game reload -r code ' + item)
    # 回到原目录
    os.chdir(old_cwd)
    