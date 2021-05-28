#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import gettext
#_=gettext.translation('accout_scanner', '/usr/share/locale').gettext

def accout_scanner(accout,proxy):
    accout=str(accout)
    genre=[]
    if '@' in accout:
        genre.append('email')
    else:
        import re
        phone_pattern = {
                'AU': '^(\+?61|0)4\d{8}$',
                'BE': '^(\+?32|0)4?\d{8}$',
                'BR': '^(\+?55|0)\-?[1-9]{2}\-?[2-9]\d{3,4}\-?\d{4}$',
                'CN': '^(\+?0?86\-?)?1[3-9]\d{9}$',
                'CZ': '^(\+?420)? ?[1-9]\d{2} ?\d{3} ?\d{3}$',
                'DE': '^(\+?49[ \.\-])?(\(\d{1,6}\))?[\d \.\-\/]{3,20}((x|ext|extension)[ ]?\d{1,4})?$',
                'DK': '^(\+?45)?\d{8}$',
		'DZ': '^(\+?213|0)[5-7]\d{8}$',
                'ES': '^(\+?34)?(6\d{1}|7[1-4])\d{7}$',
                'FI': '^(\+?358|0)\s?(4[0-5]?|50)\s?(\d\s?){4,8}\d$',
                'FR': '^(\+?33|0)[67]\d{8}$',
                'GB': '^(\+?44|0)7\d{9}$',
                'GR': '^(\+?30)?(69\d{8})$',
                'HK': '^(\+?852\-?)?[569]\d{3}\-?\d{4}$',
                'HU': '^\+?36[237]0\d{7}$',
                'IL': '^(\+972|0)([23489]|5[0248]|77)[1-9]\d{6}',
                'IN': '^(\+?91|0)?[789]\d{9}$',
                'IT': '^(\+?39)?\s?3\d{2} ?\d{6,7}$',
                'JP': '^(\+?81|0)\d{1,4}[ \-]?\d{1,4}[ \-]?\d{4}$',
                'MY': '^\+?6?01(([145](\-|\s)?\d{7,8})|([236-9](\s|\-)?\d{7}))$',
                'NO': '^(\+?47)?[49]\d{7}$',
                'NZ': '^(\+?64|0)2\d{7,9}$',
                'PL': '^(\+?48)? ?[5-8]\d ?\d{3} ?\d{2} ?\d{2}$',
                'PT': '^(\+?351)?9[1236]\d{7}$',
                'RS': '^(\+381|0)6[- \d]{5,9}$',
                'RU': '^(\+?7|8)?9\d{9}$',
                'SA': '^(!?(\+?966)|0)?5\d{8}$',
                'SY': '^(!?(\+?963)|0)?9\d{8}$',
                'TR': '^(\+?90|0)?5\d{9}$',
                'TW': '^(\+?886\-?|0)?9\d{8}',
                'US': '^(\+?1)?[2-9]\d{2}[2-9](?!11)\d{6}$',
                'VN': '^(\+?84|0)?(1(2\d|6[2-9]|88|99)|9(?!5)\d)(\d{7})$',
                'ZA': '^(\+?27|0)\d{9}$',
                'ZM': '^(\+?26)?09[567]\d{7}$'
                }
        for k, v in phone_pattern.items():
            if bool(re.compile(v).search(accout)):
                genre.append(k)
        else:
            genre.append('text')
    return genre

if __name__ == '__main__':
    print(accout_scanner(13888888888,'sock5://127.0.0.1:9050'))
