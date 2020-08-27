#-*- encoding: utf-8 -*-


_class_name = 'CreateOrderRequest'
_class_comment = '创建订单请求'

_fields = '''
appCode	String	6	通卡编号	M
cardType	int	1	虚拟卡卡种	M
paymentMethod	int	2	扣款通道	M
orderType	int	1	订单类型	M
originAmount	int	8	标准金额（应付金额）	M
issueCardFee	int	8	开卡费	M
topupAmount	int	8	充值金额	M
transAmount	int	8	交易金额/实付金额	M
cardNumber	String	32	物理卡号	M/O
productSerialNumber	String	128	票号	M/O
refundInfo	JSON		退款信息	M/O
'''


_class_format = '''

@Data
@Builder
@EqualsAndHashCode(callSuper = true)
@ApiModel(value = "{comments}", description = "{comments}")
public class {classNames} extends BaseRequest {{
{fieldss}
}}
'''

_field_format = '''
    @ApiModelProperty(value = "{remark}")
    private {typ} {name};
'''


_type_map = {
    'string' : 'String',
    'json': 'Object',
    'long': 'Long',
    'int': 'Integer',
    'int[]': 'Integer[]',
    'string[]': 'String[]',
    'long[]': 'Long[]',
}


def trans_type(typ):
    global _type_map
    java_type = _type_map.get(typ.lower(), None)
    if java_type != None:
        return java_type
    if '[]' in typ:
        return 'Object[]'
    return 'Object'


def build_fields():
    global _fields, _field_format
    ts = _fields.split('\n')
    fields = ''
    for v in ts:
        f = v.strip()
        if f == '':
            continue
        fs = f.split('\t')
        fields += _field_format.format(name = fs[0], remark = fs[3], typ = trans_type(fs[1]))
    return fields

def exchange():
    global _class_comment, _class_name, _class_format
    fields = build_fields()

    class_content = _class_format.format(comments = _class_comment, classNames = _class_name, fieldss = fields)
    print(class_content)



if __name__ == "__main__":
    exchange()
