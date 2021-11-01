import sys
import lib.util as UtilLib
import lib.file as FileLib
import lib.sh as ShLib
import config as Config


# args 
## 必选
# 操作
# cmd=replace  替换文件
# cmd=recovery 恢复文件

# cfg=cfgname  使用config common常用配置, cfgname是配置名

## 可选
# file_list=[file.beam] 文件列表，对应 cfg 的 file_list
def main(argv):
    # 提取配置
    param = UtilLib.argv_to_dict(argv)
    print(param)
    # 检查必须参数
    requisite_list = ["cmd", "cfg"]
    for item in requisite_list:
        if item not in param:
            print("缺少必须参数 :" + item)
            return 
    # 配置是否存在
    cfg_name = param["cfg"]
    if cfg_name not in Config.common:
        print("配置不存在 :" + cfg_name)
        return 
    cfg = Config.common[cfg_name]
    
    # 是否有替换 file_list
    if "file_list" in param:
        cfg["file_list"] = UtilLib.get_param_file_list(param)
    
    cmd = param["cmd"]
    if cmd == "replace":
        # 替换文件
        if not FileLib.replace_file(cfg):
            # 失败退出
            print("err replace_file return")
            return 
        
        # 是否热更
        if cfg["reload"]:
            # 热更代码
            ShLib.reload(cfg["tar_dir"], cfg["file_list"])
    elif cmd == "recovery":
        # 恢复原代码
        FileLib.recovery_file(cfg)
        # 是否热更
        if cfg["reload"]:
            # 热更代码
            ShLib.reload(cfg["tar_dir"], cfg["file_list"])
    

main(sys.argv)