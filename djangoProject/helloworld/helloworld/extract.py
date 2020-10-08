#coding:utf-8
import re


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
        temp = re.search(r'(\s?)(.{1,30})公司|(\s?)(.{1,30})企业|，(.{1,30})企业|。(.{1,30})企业|，(.{1,30})公司|。(.{1,30})公司', txt)
        if temp != None:
            for tp in temp.group():
                A[i][0] = A[i][0] + tp
        print(A[i][0])

        # 公司的主要经营范围
        temp_scope = ''
        if re.search(r'经营范围', txt) != None:
            a, b = re.search(r'经营范围', txt).span()
            while b < last:
                if txt[b+1] != '。':
                    temp_scope = temp_scope + txt[b]
                    b = b + 1
                else:
                    break
            temp_scope = temp_scope + txt[b+1]
            temp_scope = temp_scope.split('：')
            if len(temp_scope)>1:
                for tp in temp_scope[1]:
                    A[i][5] = A[i][5] + tp
            else:
                for tp in temp_scope[0]:
                    A[i][5] = A[i][5] + tp
        elif re.search(r'主要经营', txt) != None:
            a, b = re.search(r'主要经营', txt).span()
            while b < last:
                if txt[b + 1] != '。':
                    temp_scope = temp_scope + txt[b]
                    b = b + 1
                else:
                    break
            temp_scope = temp_scope + txt[b + 1]
            temp_scope = temp_scope.split('：')
            if len(temp_scope) > 1:
                for tp in temp_scope[1]:
                    A[i][5] = A[i][5] + tp
            else:
                for tp in temp_scope[0]:
                    A[i][5] = A[i][5] + tp
        elif re.search(r'授权经营', txt) != None:
            a, b = re.search(r'授权经营', txt).span()
            while b < last:
                if txt[b + 1] != '。':
                    temp_scope = temp_scope + txt[b]
                    b = b + 1
                else:
                    break
            temp_scope = temp_scope + txt[b + 1]
            temp_scope = temp_scope.split('：')
            if len(temp_scope) > 1:
                for tp in temp_scope[1]:
                    A[i][5] = A[i][5] + tp
            else:
                for tp in temp_scope[0]:
                    A[i][5] = A[i][5] + tp
        print(A[i][5])

        # 公司的成立时间
        temp = re.search(r'(\d+)年(\d+)月(\d+)日|(\d+)年(\d+)月|(\d+)年', txt)
        if temp != None:
            for tp in temp.group():
                A[i][2] = A[i][2] + tp
        print(A[i][2])

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
            A[i][4] = A[i][4] + txt[b+1]
        print(A[i][4])

        # 邮政编码
        temp = re.search(r'\D\d{6}\D', txt)
        if temp != None:
            a, b = temp.span()
            k = a + 1
            while k < b-1:
                A[i][12] = A[i][12] + txt[k]
                k = k + 1
        print(A[i][12])

        # 公司网址
        if re.search(r'http(.+)[a-zA-Z0-9]/?', txt) != None:
            for tp in re.search(r'http(.+)[a-zA-Z0-9]/?', txt).group():
                A[i][13] = A[i][13] + tp
        print(A[i][13])
        print(A[i])
        i = i + 1
    return A