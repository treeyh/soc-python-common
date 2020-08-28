#-*- encoding: utf-8 -*-

from datetime import datetime
import pyperclip

# 作者
_author = '余海'
# email
_email = 'hai.yu@snowballtech.com'
# 生成类名
_class_name = 'CreateOrderRequest'
# 类描述
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

import javax.validation.constraints.NotNull;
import com.snowballtech.fp.transit.model.bean.BaseRequest;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Builder;
import lombok.Data;
import lombok.EqualsAndHashCode;

/**
 * @author {author}
 * @version 1.0
 * @description: {comment}
 * @date {time}
 * @email {email}
 */
@Data
@Builder
@EqualsAndHashCode(callSuper = true)
@ApiModel(value = "{comment}", description = "{comment}")
public class {className} extends BaseRequest {{
{fields}
}}
'''

_field_format = '''{notnull}
    @ApiModelProperty(value = "{remark}")
    private {typ} {name};
'''

_not_null = '''
@NotNull(message = "{remark}不能为空")'''


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

def build_not_null(remark, must_type):
    global _not_null
    if 'm' == must_type.lower():
        return _not_null.format(remark = remark)
    return ''

def build_fields():
    global _fields, _field_format
    ts = _fields.split('\n')
    fields = ''
    for v in ts:
        f = v.strip()
        if f == '':
            continue
        fs = f.split('\t')
        name = fs[0]
        remark = fs[3]
        typ = fs[1]
        must_type = fs[4]
        fields += _field_format.format(name = name, remark = remark, typ = trans_type(typ), 
                                        notnull = build_not_null(remark, must_type))
    return fields

def exchange():
    global _class_comment, _class_name, _class_format, _author, _email
    fields = build_fields()

    class_content = _class_format.format(comment = _class_comment, className = _class_name, 
                                        fields = fields, author = _author, email = _email, 
                                        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print(class_content)
    pyperclip.copy(class_content)
    print('生成内容已复制到剪贴板中.')



if __name__ == "__main__":
    exchange()
