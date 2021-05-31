import argparse
import pytest

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--keyword', help='只执行匹配关键字的用例，会匹配文件名、类名、方法名', type=str)
    parser.add_argument('-d', '--dir', help='指定要测试的目录', type=str)
    parser.add_argument('-m', '--markexpr', help='只运行符合给定的mark表达式的测试', type=str)
    parser.add_argument('-s', '--capture', help='是否在标准输出流中输出日志,1:是、0:否,默认为0', type=str)
    parser.add_argument('-r', '--reruns', help='失败重跑次数,默认为0', type=int)
    parser.add_argument('-lf', '--lf', help='是否运行上一次失败的用例,1:是、0:否,默认为0', type=int)
    parser.add_argument('-clr', '--clr', help='是否清空已有测试结果,1:是、0:否,默认为0', type=int)
    args = parser.parse_args()

    pytest_execute_params = []
    if args.dir:
        pytest_execute_params.append('-d')
        pytest_execute_params.append(args.dir)
    if args.keyword:
        pytest_execute_params.append('-k')
        pytest_execute_params.append(args.keyword)
    if args.markexpr:
        pytest_execute_params.append('-m')
        pytest_execute_params.append(args.markexpr)
    # 判断是否失败重跑
    if args.reruns:
        if int(args.reruns):
            pytest_execute_params.append('-r')
            pytest_execute_params.append(args.reruns)

    # 判断是否只运行上一次失败的用例
    if args.lf:
        if int(args.lf):
            pytest_execute_params.append('-lf')
    # 判断是否清空已有测试结果
    if args.clr:
        if int(args.clr):
            pytest_execute_params.append('-clr')


    # print('%s开始测试......' % DateTimeTool.getNowTime())
    pytest.main(pytest_execute_params)