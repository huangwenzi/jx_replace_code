import os
import shutil
import config as Config
import copy
# 文件



# 替换 sou_dir 下文件到 tar_dir
def replace_file(cfg):
    sou_dir = cfg["sou_dir"]
    tar_dir = cfg["tar_dir"]
    # 要深拷贝，下面会对列表做修改
    file_list = copy.deepcopy(cfg["file_list"])
    recovery = cfg["recovery"]
    cfg_name = cfg["name"]
            
    file_path_list = []
    # 遍历来源目录
    for root, dirs, files in os.walk(sou_dir):
        # 遍历文件
        for f in files:
            if f in file_list:
                file_path_list.append(os.path.join(root, f))
                file_list.remove(f)
                if len(file_list) == 0:
                    break
    # 是否有文件未匹配
    if len(file_list) > 0:
        print("err 文件匹配失败")
        print(file_list)
        return False
    
    # 替换过去
    save_dir = Config.setting["save_dir"]
    save_dir = os.path.join(save_dir, cfg_name)
    for item in file_path_list:
        tar_file = item.replace(sou_dir, tar_dir, 1)
        # 目录不存在要创建
        dir_name = os.path.dirname(tar_file)
        if not os.path.isdir(dir_name):
            os.makedirs(dir_name)
        # 保存被替换文件
        if recovery and os.path.exists(tar_file):
            save_file = item.replace(sou_dir, save_dir)
            # 目录不存在要创建
            save_dir_name = os.path.dirname(save_file)
            if not os.path.isdir(save_dir_name):
                os.makedirs(save_dir_name)
            shutil.copy(tar_file, save_file)   
        # 拷贝文件
        shutil.copy(item, tar_file)
    return True

# 恢复源代码
def recovery_file(cfg):
    # 能被删除的尾缀
    can_remove = Config.setting["can_remove"]
    save_dir = Config.setting["save_dir"]
    cfg_name = cfg["name"]
    tar_dir = cfg["tar_dir"]
    # 遍历来源目录
    save_dir = os.path.join(save_dir, cfg_name)
    for root, dirs, files in os.walk(save_dir):
        # 遍历文件
        for f in files:
            save_file = os.path.join(root, f)
            # 要还原的文件路径
            tar_file = save_file.replace(save_dir, tar_dir)
            # 拷贝文件
            shutil.copy(save_file, tar_file)
            # 删除保存的文件
            for tmp_can_remove in can_remove:
                if save_file.find(tmp_can_remove):
                    os.remove(save_file)
                    break
    






