def parse_termsdetail(termsdetail):
    termsdetail = termsdetail.replace('SPIN-OFF TO', 'SPIN-OFF-TO')
    detail_list = termsdetail.split('AND')
    detail_list = [x.strip() for x in detail_list]
    cusip_list = []
    flag = False
    for detail in detail_list:
        items = detail.split(' ')
        if detail.startswith('SPIN-OFF-TO'):
            flag = True
            cusip_list.extend(items[1:])
            continue
        if flag and len(items) == 1:
            cusip_list.extend(items)
            continue
        flag = False
    return cusip_list

example = 'SPIN-OFF TO ABC DEF AND SPIN-OFF TO GHI AND JKL AND SPIN-OFF TO MNO AND 1 x 4 REVERSE SPLIT'
result = parse_termsdetail(example)
print result
