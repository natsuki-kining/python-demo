# 异常

def excption1():
    try:
        # 不能确定正确执行的代码
        num = int(input("请输入一个整数："))
    except:
        # 错误的处理代码
        print("请输入正确的整数")

    print("-" * 50)

def excption2():
    """捕捉错误类型"""
    try:
        # 提示用户输入一个整数
        num = int(input("输入一个整数："))

        # 使用 8 除以用户输入的整数并且输出
        result = 8 / num

        print(result)
    except ZeroDivisionError:
        print("除0错误")
    except ValueError:
        print("请输入正确的整数")

def excption3():
    """捕捉未知异常"""
    try:
        # 提示用户输入一个整数
        num = int(input("输入一个整数："))

        # 使用 8 除以用户输入的整数并且输出
        result = 8 / num

        print(result)
    except ValueError:
        print("请输入正确的整数")
    except Exception as result:
        print("未知错误 %s" % result)


def excption4():
    """完整异常的写法"""
    try:
        # 提示用户输入一个整数
        num = int(input("输入一个整数："))

        # 使用 8 除以用户输入的整数并且输出
        result = 8 / num

        print(result)
    except ValueError:
        print("请输入正确的整数")
    except Exception as result:
        print("未知错误 %s" % result)
    else:
        print("尝试成功")
    finally:
        print("无论是否出现错误都会执行的代码")


def excption5():
    return int(input("输入整数："))

def excption6():
    return excption5()

def excption7():
    # 利用异常的传递性，在主程序捕获异常
    try:
        print(excption6())
    except Exception as result:
        print("未知错误 %s" % result)



def excption8():
    """主动抛出异常"""

    # 1. 提示用户输入密码
    pwd = input("请输入密码：")

    # 2. 判断密码长度 >= 8，返回用户输入的密码
    if len(pwd) >= 8:
        return pwd

    # 3. 如果 < 8 主动抛出异常
    print("主动抛出异常")
    # 1> 创建异常对象 - 可以使用错误信息字符串作为参数
    ex = Exception("密码长度不够")

    # 2> 主动抛出异常
    raise ex

def excption9():
    # 提示用户输入密码
    try:
        print(excption8())
    except Exception as result:
        print(result)


excption9()