# 工具


# argv转字典
def argv_to_dict(argv):
    ret_dict = {}
    # 第一个是执行文件名，跳过
    for item in argv[1:]:
        idx = item.find("=")
        key = item[:idx]
        val = item[idx+1:]
        ret_dict[key] = val
    return ret_dict


# 提取param的file_list
def get_param_file_list(param):
    file_list_str = param["file_list"]
    if len(file_list_str) < 3:
        return []
    file_list_str = file_list_str[1:-1]
    file_list = file_list_str.split(",")
    return file_list




