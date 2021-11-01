## 配置文件
setting = {
    # 存档文件目录
    "save_dir" : "save_dir",
    # 能被删除的文件
    "can_remove" : [".txt", ".beam"]
}

common = {
    "cehua":{
        # 配置名            必须和上面保持一致
        "name" : "cehua",
        # 替换文件目录
        "sou_dir" : "new", 
        # 替换文件
        "file_list" : [
            "1.txt",
            "2.txt"
        ], 
        # 被替换目录
        "tar_dir" : "old",
        # 是否热更
        "reload" : True,
        # 是否保存被替换的文件，保存后可用 recovery 指令恢复
        "recovery" : True
    }
}