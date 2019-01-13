import struct


class DivideProtocol(object):
    """
    float divide(1:int num1, 2:int num2=1)
    """
    def _read_all(self,size):
        """
          读取指定长度的字节
          :param size: 长度
          :return: 读取出的二进制数据
        """
        pass

    def args_encode(self,num1,num2=1):
        """
        对调用参数进行编码
        :param num1:int
        :param num2: int
        :return: 编码后的二进制数据
        """

        #处理参数num1,4字节整型
        buff = struct.pack('!B',1)
        buff+=struct.pack('!i',num1)

        #处理参数num2,4字节整型，如为默认值1，则不再放到消息中
        if num2 != 1:
            buff+=struct.pack('!B',2)
            buff+=struct.pack('!i',num2)


        #处理消息总长度，4字节无符号整型
        length = len(buff)

        #处理方法名，字符串类型
        name = "divide"
        #字符串长度，4字节无符号整型
        msg = struct.pack('!I',len(name))
        msg+=name.encode()

        msg += struct.pack('!I',length) + buff

        return msg

    def args_decode(self,connection):
        """
        获取调用参数并进行解码
        :param connection:传输工具对象，如socket对象或者BytesIO对象，从中可以读取消息数据
        :return:解码后的参数字典
        """

        #保存到当前对象中，供_read_all方式使用
        self.conn = connection

        param_name_map = {
            1:"num1",
            2:"num2"
        }

        param_len_map = {
            1:4,
            2:4
        }


        #用于保存解码后的参数字典
        args = dict()

        #读取消息总长度，4字节无符号整数
        buff = self._read_all(4)
        length = struct.unpack("!I",buff)[0]

        #记录已读取的长度
        have = 0

        #读取第一个参数，4字节整型
        buff = self._read_all(1)
        have += 1

        param_seq = struct.unpack("!B",buff)[0]
        param_len = param_len_map[param_seq]
        buff = self._read_all(param_len)

        have += param_len
