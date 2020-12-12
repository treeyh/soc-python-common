#-*- encoding: utf-8 -*-

from datetime import datetime
import pyperclip

# 作者
_author = ''
# email
_email = ''
# 生成类名
_class_name = ''
# 类描述
_class_comment = ''
# 是否生成请求bean, True：request，False：response
_request_type = False


_fields = '''
appCode	String	6	通卡应用编号	M
cardType	int	1	虚拟卡卡种	M
orderNumber	String	32	订单号	M
cardNumber	String	32	卡号	O
paymentMethod	String	2	支付渠道	M
paymentStatus	String	2	支付状态	M
orderType	int	1	订单类型	M
orderStatus	int	1	订单状态	M
orderStatusDesc	String	32	订单状态描述	M
orderAmount	int	8	订单金额	M
orderTime	int	11	订单创建时间的时间戳	M
orderFinishTime	int	11	订单完成时的时间戳	O
'''


_request_class_format = '''

import javax.validation.constraints.NotNull;
import com.snowballtech.fp.transit.model.bean.BaseRequest;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.*;

/**
 * @author {author}
 * @version 1.0
 * @description: {comment}
 * @date {time}
 * @email {email}
 */
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@EqualsAndHashCode(callSuper = true)
@ApiModel(value = "{comment}", description = "{comment}")
public class {className} extends BaseRequest {{
{fields}
}}
'''


_response_class_format = '''
import java.io.Serializable;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.*;

/**
 * @author {author}
 * @version 1.0
 * @description: {comment}
 * @date {time}
 * @email {email}
 */
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@EqualsAndHashCode(callSuper = false)
@ApiModel(value = "{comment}", description = "{comment}")
public class {className} implements Serializable {{
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
    global _not_null, _request_type
    if 'm' == must_type.lower() and _request_type:
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
        if len(fs) < 5:
            continue
        name = fs[0]
        remark = fs[3]
        typ = fs[1]
        must_type = fs[4]
        fields += _field_format.format(name = name, remark = remark, typ = trans_type(typ), 
                                        notnull = build_not_null(remark, must_type))
    return fields

def exchange():
    global _class_comment, _class_name, _request_class_format, _response_class_format, _author, _email, _request_type
    fields = build_fields()

    class_content = (_request_class_format if _request_type else _response_class_format).format(
                                    comment = _class_comment, className = _class_name, 
                                    fields = fields, author = _author, email = _email, 
                                    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    print(class_content)
    pyperclip.copy(class_content)
    print('生成内容已复制到剪贴板中.')



if __name__ == "__main__":
    exchange()
