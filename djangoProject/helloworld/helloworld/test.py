#coding:utf-8
import re
import csv


def create_csv(A):
    path = "../../data/"
    with open(path+"enterprise_node.csv", 'w', encoding='utf-8', newline='') as file:
        csv_write = csv.writer(file)
        csv_head = ["name_id", "name"]
        csv_write.writerow(csv_head)
        i = 1
        for data in A:
            data_row = [i, data[0]]
            csv_write.writerow(data_row)
            i = i + 1
    with open(path+"codeof.csv", 'w', encoding='utf-8', newline='') as file:
        csv_write = csv.writer(file)
        csv_head = ["name_id", "name", "code_id", "code", "relation"]
        csv_write.writerow(csv_head)
        i = 1
        j = 1
        for data in A:
            if data[12] != '*':
                data_row = [j, data[0], i, data[12], "codeof"]
                csv_write.writerow(data_row)
                i = i + 1
            j = j + 1
    with open(path+"establishtimeof.csv", 'w', encoding='utf-8', newline='') as file:
        csv_write = csv.writer(file)
        csv_head = ["name_id", "name", "time_id", "time", "relation"]
        csv_write.writerow(csv_head)
        i = 1
        j = 1
        for data in A:
            if data[2] != '*':
                data_row = [j, data[0], i, data[2], "establishtimeof"]
                csv_write.writerow(data_row)
                i = i + 1
            j = j + 1
    with open(path+"locationof.csv", 'w', encoding='utf-8', newline='') as file:
        csv_write = csv.writer(file)
        csv_head = ["name_id", "name", "location_id", "location", "relation"]
        csv_write.writerow(csv_head)
        i = 1
        j = 1
        for data in A:
            if data[4] != '*':
                data_row = [j, data[0], i, data[4], "locationof"]
                csv_write.writerow(data_row)
                i = i + 1
            j = j + 1
    with open(path+"scopeof.csv", 'w', encoding='utf-8', newline='') as file:
        csv_write = csv.writer(file)
        csv_head = ["name_id", "name", "scope_id", "scope", "relation"]
        csv_write.writerow(csv_head)
        i = 1
        j = 1
        for data in A:
            if data[5] != '*':
                data_row = [j, data[0], i, data[5], "scopeof"]
                csv_write.writerow(data_row)
                i = i + 1
            j = j + 1
    with open(path+"webof.csv", 'w', encoding='utf-8', newline='') as file:
        csv_write = csv.writer(file)
        csv_head = ["name_id", "name", "web_id", "web", "relation"]
        csv_write.writerow(csv_head)
        i = 1
        j = 1
        for data in A:
            if data[13] != '*':
                data_row = [j, data[0], i, data[13], "webof"]
                csv_write.writerow(data_row)
                i = i + 1
            j = j + 1


def extract(txt):
    txt_split = txt.split('#')
    A = []
    i = 0
    for text in txt_split:
        A.append([])
        for j in range(0, 14):
            A[i].append('')
        i = i + 1
    i = 0
    print(txt)
    for txt in txt_split:
        # 公司名称
        name_num = 0
        # 法定代表人
        legal_representative_num = 0
        # 成立时间
        establish_num = 0
        # 注册资本
        registered_capital_num = 0
        # 公司地址
        location_num = 0
        # 经营范围
        business_scope_num = 0
        # 经营期限
        operating_period_num = 0
        # 登记机关
        registered_authority_num = 0
        # 股东信息
        shareholder_information_num = 0
        # 高管信息
        executive_information_num = 0
        # 登记状态
        registered_statement_num = 0
        # 实收资本
        get_capital_num = 0
        # 邮政编码
        postal_code_num = 0
        # 公司网址
        web_num = 0
        last = len(txt)
        # 获取企业名称
        name = ''
        temp = re.search(r'(\s?)(.{1,30})公司|(\s?)(.{1,30})企业|，(.{1,30})企业|。(.{1,30})企业|，(.{1,30})公司|。(.{1,30})公司', txt)
        if temp != None:
            for tp in temp.group():
                name = name + tp
        name = name.split('，')
        A[i][0] = name[0]
        if A[i][0] == '':
            A[i][0] = '*'
        print(A[i][0])

        # 法人代表
        if re.search(r'法定代表人(为?)', txt) != None:
            a, b = re.search(r'法定代表人(为?)', txt).span()
            while txt[b] != '，' and txt[b] != '。':
                A[i][1] = A[i][1] + txt[b]
                b = b + 1
        elif re.search(r'法人代表(为?)', txt) != None:
            a, b = re.search(r'法人代表(为?)', txt).span()
            while txt[b] != '，' and txt[b] != '。':
                A[i][1] = A[i][1] + txt[b]
                b = b + 1
        print(A[i][1])
        if A[i][1] == '':
            A[i][1] = '*'

        # 公司的成立时间
        temp = re.search(r'(\d+)年(\d+)月(\d+)日|(\d+)年(\d+)月|(\d{4})年', txt)
        if temp != None:
            for tp in temp.group():
                A[i][2] = A[i][2] + tp
        print(A[i][2])
        if A[i][2] == '':
            A[i][2] = '*'

        # 注册资本
        temp = ''
        if re.search(r'注册资本', txt) != None:
            a, b = re.search(r'注册资本', txt).span()
            while txt[b] != '。' and txt[b] != '，':
                temp = temp + txt[b]
                b = b + 1
            if re.search(r'\d(.+)[(人民币)(美元)]', temp) != None:
                A[i][3] = A[i][3] + temp
            elif re.search(r'[(一)(二)(三)(四)(五)(六)(七)(八)(九)(十)](.+)[(人民币)(美元)]', temp) != None:
                A[i][3] = A[i][3] + temp
        print(A[i][3])
        if A[i][3] == '':
            A[i][3] = '*'

        # 公司地址
        temp = re.search(r'(公司)?地址', txt)
        if temp != None:
            a, b = re.search(r'(公司)?地址', txt).span()
            b = b + 2
            while b < last:
                if txt[b+1] != '。' and txt[b+1] != '，' and txt[b+1] != '！':
                    A[i][4] = A[i][4] + txt[b]
                    b = b + 1
                else:
                    break
            A[i][4] = A[i][4] + txt[b]
        print(A[i][4])
        if A[i][4] == '':
            A[i][4] = '*'

        # 公司的主要经营范围
        if re.search(r'经营范围', txt) != None:
            a, b = re.search(r'经营范围', txt).span()
            #b = b + 1
            temp = ''
            while txt[b] != '。':
                temp = temp + txt[b]
                b = b + 1
            temp1 = temp.split('：')
            if len(temp1) > 1 and len(temp1)<3:
                for tp in temp1[1]:
                    A[i][5] = A[i][5] + tp
            else:
                for tp in temp:
                    A[i][5] = A[i][5] + tp
        elif re.search(r'主要经营', txt) != None:
            a, b = re.search(r'主要经营', txt).span()
            #b = b + 1
            temp = ''
            while txt[b] != '。':
                temp = temp + txt[b]
                b = b + 1
            temp1 = temp.split('：')
            if len(temp1) > 1 and len(temp1)<3:
                for tp in temp1[1]:
                    A[i][5] = A[i][5] + tp
            else:
                for tp in temp:
                    A[i][5] = A[i][5] + tp
        elif re.search(r'经营范围', txt) != None:
            a, b = re.search(r'经营范围', txt).span()
            # b = b + 1
            temp = ''
            while txt[b] != '。':
                temp = temp + txt[b]
                b = b + 1
            temp1 = temp.split('：')
            if len(temp1) > 1 and len(temp1)<3:
                for tp in temp[1]:
                    A[i][5] = A[i][5] + tp
            else:
                for tp in temp:
                    A[i][5] = A[i][5] + tp
        elif re.search(r'主要运营', txt) != None:
            a, b = re.search(r'主要运营', txt).span()
            # b = b + 1
            temp = ''
            while txt[b] != '。':
                temp = temp + txt[b]
                b = b + 1
            temp1 = temp.split('：')
            if len(temp1) > 1 and len(temp1)<3:
                for tp in temp[1]:
                    A[i][5] = A[i][5] + tp
            else:
                for tp in temp:
                    A[i][5] = A[i][5] + tp
        print(A[i][5])
        if A[i][5] == '':
            A[i][5] = '*'

        # 邮政编码
        temp = re.search(r'\D\d{6}\D', txt)
        if temp != None:
            a, b = temp.span()
            k = a + 1
            while k < b-1:
                A[i][12] = A[i][12] + txt[k]
                k = k + 1
        print(A[i][12])
        if A[i][12] == '':
            A[i][12] = '*'

        # 公司网址
        if re.search(r'http(.+)[a-zA-Z0-9](\/?)', txt) != None:
            for tp in re.search(r'http(.+)[a-zA-Z0-9]/?', txt).group():
                A[i][13] = A[i][13] + tp
        elif re.search(r'www(.+)[a-zA-Z0-9](\/?)', txt) != None:
            for tp in re.search(r'www(.+)[a-zA-Z0-9](\/?)', txt).group():
                A[i][13] = A[i][13] + tp
        print(A[i][13])
        if A[i][13] == '':
            A[i][13] = '*'
        print(A[i])
        i = i + 1
    return A


txt = '武汉昱达昌实业有限公司是一家专注于“产旅城”大健康全域发展公司。公司最早发展于2005年9月，是集房地产开发、药食同源养生健康产品销售、主题公园运营、特色小镇开发运营、建筑工程、商品房销售和设计、制作、发布为一体的多元化综合性公司。在武汉先后开发了世纪庭苑/福欣园/银都雅园/果乐小镇等项目。其中“果乐小镇”项目是与蓝城集团合作，占地8000亩，投资150亿元，旨在打造以文化旅游、观光休闲、养生度假等为一体的特色小镇项目。公司地址：武汉市江夏区北华街世纪庭苑北门4-5栋一楼。邮编：432000。'
Data = extract(txt)
print(Data)
#create_csv(Data)
