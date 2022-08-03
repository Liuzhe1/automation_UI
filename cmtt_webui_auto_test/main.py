import os
from excel.excel_read import excel_read

if __name__ == '__main__':
    cases = list()
    #读取路径下测试用例
    for path,dir,files in os.walk('./data/'):
        for file in files:
            #获取文件后缀名
            file_type = os.path.splitext(file)[1]
            file_name = os.path.splitext(file)[0]
            if file_type == '.xlsx':
                if 'old' not in file_name:
                    case_path = path+file
                    cases.append(case_path)
            else:
                print('***文件类型错误:{}***'.format(file))

    for case in cases:
        print('^^^^^^^^^^^^正在执行:{}^^^^^^^^^^^^'.format(case))
        excel_read(case)