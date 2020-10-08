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
        if re.search(r'经营范围', txt) != None:
            temp = re.search(r'经营范围', txt).group()
            temp = temp.split('：')
            if len(temp)>1:
                for tp in temp[1]:
                    A[i][5] = A[i][5] + tp
            else:
                for tp in temp[0]:
                    A[i][5] = A[i][5] + tp
        elif re.search(r'主要经营', txt) != None:
            temp = re.search(r'主要经营', txt).group()
            temp = temp.split('：')
            if len(temp) > 1:
                for tp in temp[1]:
                    A[i][5] = A[i][5] + tp
            else:
                for tp in temp[0]:
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
            while k < b:
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


txt = '湖北恒通荣昌建设工程有限公司，成立于2000年2月2日，经营范围包括：室内外装饰工程设计与施工；消防工程设计、施工；楼宇智能化监控系统、电气自动化控制系统的设计、施工；给排水工程设计、施工；市政工程设计与施工；暖通设备、通风设备、空调设备维修；机电设备销售；幕墙工程、园林绿化工程、钢结构工程施工；电梯设备的安装与维修；通风设备的生产、加工（生产加工仅限分支机构）。公司地址：黄陂区盘龙城卓尔总部m2。#武汉缘来文化传播有限责任公司（缘来文化），成立于2001年，总资产过亿，是一家为高等院校、公共图书馆、科技馆等提供专业的多媒体资源数据服务、数字图书馆解决方案以及其它教育相关资源产品的综合性文化传播公司。国内较大规模的科教节目供应商——缘来文化携手英国、德国、美国、匈牙利等不同国家专业科教制作机构，BBC、DW、DISCOVERY、Schlessinger、Mozaik……成功打造行业知名品牌“知识视界”。目前科教类资源总库存量有60万分钟海量视频素材、1万多个不同主题内容、50万个视频条目、100万幅图片，除了自制外，每年仍不断从国内外著名科教节目制作中心引进优秀的科教节目。优秀的制作团队及技术运营团队——缘来文化拥有国际水准的专业多媒体资源制作队伍，擅长视频资源、高技术互动产品、平面图文等富媒体资源的设计及制作，拥有进行数字内容加工、数字出版技术解决方案和数字内容平台运营的能力；拥有国际领先的网络和远程教育技术及专业的网络技术人员。成熟完善口碑卓越的产品体系——缘来文化打造的各类产品运用于教育、公共文化建设、新媒体、电视等领域，获得了广泛关注和良好市场反响。用户群体已覆盖全国高等院校、公共图书馆1000多所，中小学20000多所；缘来文化参与到了文化部、财政部共同推出“数字图书馆推广工程”当中，资源产品覆盖全国地市级以上公共图书馆，直接受益图书馆达300所。同时缘来文化与中国科学技术出版社、广东教育出版社、上海科学技术出版社、山东科学技术出版社等众多出版社成为战略合作伙伴。公司制作的“科学的航程”系列图书（全12册）入围国家“十二五”重点出版物出版规划项目、“我们周围的秘密”系列图书（全6册）入围国家“十三五”重点出版物出版规划项目。“知识视界”以专业的产品优势，成熟的技术，良好的客户群体，已成为文化教育出版等行业最具发展潜力的品牌。我们拥有朝气蓬勃的团队---年轻人，在一起，就是有话题；全面系统的培训及提升机制---拥有“知识，视界”无限，在这里，你可以学到更多；极具竞争力的薪酬体系---有能力，你就上；公司将搬迁至武汉客厅，1000多平的全新的办公环境，期待你的加入！地址：江岸区黄浦大街258号天梨阁北苑A1栋7楼。联系电话：027-82880801。公司网址：http://www.yuanlai.cn。#武汉市博源纸塑彩印制品有限公司，成立于1997年，公司是省内最早一批从事于食品包装加工制造的民营企业，在国内有广泛的知名度。公司坐落于武汉市东西湖区银柏路60号，有良好的工业环境以及较为便利的交通，产品远销国内外，设备先进，拥有专业的技术人员以及管理人员。公司主要客户包括食品饮料公司，进出口贸易公司，各大商超，日用批发市场，销售前景广阔。欢迎您的加入。公司地址：武汉市东西湖区泾河银柏路60号。邮政编码：430040。#武汉星斐斯文化传媒有限公司，武汉星斐斯文化传媒有限公司成立于2020年，武汉星斐斯是着力于打造属于星斐斯的线下网红艺人，着力于培养，孵化，发展线下艺人的企业。武汉总部设立于风景秀丽，空气清新的武汉江夏区别墅。是由安徽总部分支出来的新公司。公司运营，技术，短视频运营等实力雄厚，孵化线下艺人能力强大。公司拥有专业的直播设备，资深运营团队及培训人员。只为打造星斐斯线下艺人团队做好充分准备。公司地址：武汉市江夏区藏龙岛阳光100。邮政编码：430200。#武汉春晖园林股份有限公司，初始创办于2009年，是一家以市政园林、地产景观、湿地公园、喷泉水景、水处理、仿古建筑、景观规划设计施工以及绿化养护园林环境整合一体化的综合性园林企业运营商。公司先后参与武汉市政府重点工程：省博物馆、汉口江滩以及省、市重点工程辛亥革命百周年庆典献礼工程——首义文化公园、黄梅小池滨江新区的清江烟雨公园、太子公园、江汉路商业步行街、万松园国际品牌街、省委茶港小区的工程建设以及武汉项目C1地块、中梁九号院示范区、绿城·龙苑澜岸三期A块、金银湖一号三期别墅、美联·石桥K7地块、锦绣长江C2-2地块、湖湘文化城B地块二期展示区、盘龙理想城南区一期二期、美加湖滨新城四期示范区、宝江南春、银海华庭、山水华庭、碧海花园、北大鸿城、天舜金港明珠、葛洲坝国际广场、清江泓景、晋合金桥世家、翰林雅居、南德国际城、香域华府、锦绣香江、奥林匹克花园、河南昌建誉峰、南昌世茂C-15、湖南御华园、石首市山底湖公园、中国地质大学（武汉）新校区、天河机场T3航站楼、湖北师范文理学院搬迁项目一期室外、华中科技大文化学院、中南财经政法大学、东西湖人民医院、汇丰企业总部、市公安局交警大队、武汉大学科技园、华科大武昌分校、黄陂广场、生物城、武汉市中医医院汉阳分院、新长江·王家墩广场、木兰广场、美联石桥K9室外、销品茂等园林景观工程，共计两百多个项目的施工，业务分布湖北、湖南、江西、河南、安徽等地。同时为首义文化公园十八星旗喷泉核心景观，罗田城东广场、南漳县水镜公园二期、山水华庭、销品茂、武广专客咸宁火车站喷泉广场、明珠豪生大酒店等一大批名优项目提供了优秀的园林景观设计。公司是湖北省风景园林学会副会长单位、湖北国际合作协会执行会长单位、楚商联合会副会长单位、武汉市城市园林绿化企业协会常任理事单位、中国水景喷泉分会常任理事单位、武汉大冶商会常务副会长单位。本着高起点，严要求，科学管理的原则，严禁组织，精心设计，精心施工，以科学决策为依靠，以充足的资金为后盾，以先进的技术设备为保障，以严谨的管理手段立足于武汉，辐射全国，崇尚信誉，树立春晖品牌。公司地址：武汉市武昌区徐东大街群星城汇金中心K3-2。邮政编码：430062。公司网站：http://www.whchyl.com/。'
Data = extract(txt)
