

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

txt = '湖北恒通荣昌建设工程有限公司，成立于2000年2月2日，经营范围包括：室内外装饰工程设计与施工；消防工程设计、施工；楼宇智能化监控系统、电气自动化控制系统的设计、施工；给排水工程设计、施工；市政工程设计与施工；暖通设备、通风设备、空调设备维修；机电设备销售；幕墙工程、园林绿化工程、钢结构工程施工；电梯设备的安装与维修；通风设备的生产、加工（生产加工仅限分支机构）。公司地址：黄陂区盘龙城卓尔总部m2。#武汉缘来文化传播有限责任公司（缘来文化），成立于2001年，总资产过亿，是一家为高等院校、公共图书馆、科技馆等提供专业的多媒体资源数据服务、数字图书馆解决方案以及其它教育相关资源产品的综合性文化传播公司。国内较大规模的科教节目供应商——缘来文化携手英国、德国、美国、匈牙利等不同国家专业科教制作机构，BBC、DW、DISCOVERY、Schlessinger、Mozaik……成功打造行业知名品牌“知识视界”。目前科教类资源总库存量有60万分钟海量视频素材、1万多个不同主题内容、50万个视频条目、100万幅图片，除了自制外，每年仍不断从国内外著名科教节目制作中心引进优秀的科教节目。优秀的制作团队及技术运营团队——缘来文化拥有国际水准的专业多媒体资源制作队伍，擅长视频资源、高技术互动产品、平面图文等富媒体资源的设计及制作，拥有进行数字内容加工、数字出版技术解决方案和数字内容平台运营的能力；拥有国际领先的网络和远程教育技术及专业的网络技术人员。成熟完善口碑卓越的产品体系——缘来文化打造的各类产品运用于教育、公共文化建设、新媒体、电视等领域，获得了广泛关注和良好市场反响。用户群体已覆盖全国高等院校、公共图书馆1000多所，中小学20000多所；缘来文化参与到了文化部、财政部共同推出“数字图书馆推广工程”当中，资源产品覆盖全国地市级以上公共图书馆，直接受益图书馆达300所。同时缘来文化与中国科学技术出版社、广东教育出版社、上海科学技术出版社、山东科学技术出版社等众多出版社成为战略合作伙伴。公司制作的“科学的航程”系列图书（全12册）入围国家“十二五”重点出版物出版规划项目、“我们周围的秘密”系列图书（全6册）入围国家“十三五”重点出版物出版规划项目。“知识视界”以专业的产品优势，成熟的技术，良好的客户群体，已成为文化教育出版等行业最具发展潜力的品牌。我们拥有朝气蓬勃的团队---年轻人，在一起，就是有话题；全面系统的培训及提升机制---拥有“知识，视界”无限，在这里，你可以学到更多；极具竞争力的薪酬体系---有能力，你就上；公司将搬迁至武汉客厅，1000多平的全新的办公环境，期待你的加入！地址：江岸区黄浦大街258号天梨阁北苑A1栋7楼。联系电话：027-82880801。公司网址：http://www.yuanlai.cn。'
Data = extract(txt)
