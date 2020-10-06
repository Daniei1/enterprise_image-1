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
        while name_num < last:
            if txt[name_num] != '，':
                A[i][0] = A[i][0] + txt[name_num]
                name_num = name_num + 1
            else:
                break
        print(A[i][0])

        # 获取企业经营范围
        while business_scope_num + 4 < last:
            if txt[business_scope_num + 1:business_scope_num + 5] == '经营范围':
                business_scope_num = business_scope_num + 5
                while business_scope_num < last:
                    if txt[business_scope_num] != '。':
                        A[i][5] = A[i][5] + txt[business_scope_num]
                        business_scope_num = business_scope_num + 1
                    else:
                        break
                break
            else:
                business_scope_num = business_scope_num + 1
        print(A[i][5])

        # 成立时间
        while establish_num + 3 < last:
            if txt[establish_num + 1:establish_num + 4] == '成立于':
                establish_num = establish_num + 4
                while establish_num < last:
                    if (txt[establish_num] != '，') and (txt[establish_num] != '。'):
                        A[i][2] = A[i][2] + txt[establish_num]
                        establish_num = establish_num + 1
                    else:
                        break
                break
            else:
                establish_num = establish_num + 1
        print(A[i][2])

        # 公司地址
        while location_num + 4 < last:
            if txt[location_num + 1:location_num + 5] == '公司地址':
                location_num = location_num + 6
                while location_num < last:
                    if txt[location_num] != '，' and txt[location_num] != '。':
                        A[i][4] = A[i][4] + txt[location_num]
                        location_num = location_num + 1
                    else:
                        break
                break
            else:
                location_num = location_num + 1
        print(A[i][4])

        # 邮政编码
        while postal_code_num + 4 < last:
            if txt[postal_code_num + 1:postal_code_num + 5] == '邮政编码':
                postal_code_num = postal_code_num + 6
                while postal_code_num < last:
                    if txt[postal_code_num] != '，' and txt[postal_code_num] != '。':
                        A[i][12] = A[i][12] + txt[postal_code_num]
                        postal_code_num = postal_code_num + 1
                    else:
                        break
                break
            else:
                postal_code_num = postal_code_num + 1
        print(A[i][12])

        # 公司网址
        while web_num + 4 < last:
            if txt[web_num + 1:web_num + 5] == '公司网站':
                web_num = web_num + 6
                while web_num < last:
                    if txt[web_num] != ',' and txt[web_num] != '。' and txt[web_num] != '；':
                        A[i][13] = A[i][13] + txt[web_num]
                        web_num = web_num + 1
                    else:
                        break
                break
            else:
                web_num = web_num + 1
        print(A[i][13])
        print(A[i])
        i = i + 1
    return A