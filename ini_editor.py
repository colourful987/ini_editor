import argparse
import subprocess
import sys
import os
import configparser
import pkg_resources


def run_shell(shell):
    cmd = subprocess.Popen(shell, stdin=subprocess.PIPE, stderr=sys.stderr, close_fds=True,
                           stdout=sys.stdout, universal_newlines=True, shell=True, bufsize=1)
    cmd.communicate()
    return cmd.returncode


def find_executable(executable):
    """
    usage : find_executable('node')
    """

    path = os.environ['PATH']
    paths = path.split(os.pathsep)
    base, ext = os.path.splitext(executable)
    if sys.platform == 'win32' and not ext:
        executable = executable + '.exe'

    if os.path.isfile(executable):
        return executable

    for p in paths:
        full_path = os.path.join(p, executable)
        if os.path.isfile(full_path):
            return full_path

    return None


def run_doctor(args):
    """
    检查环境配置：比如检查是否有某些命令
    :param args:
    :return:
    """
    print('[√] 检查环境变量')


def query_operation(args):
    """
    查询 section 下键等于 KEY 的值
    :return:
    """
    config_path = os.path.join(os.path.dirname(pkg_resources.resource_filename(__name__, '')), 'conf/Modules.ini')
    config_obj = configparser.ConfigParser()
    config_obj.read(config_path)
    value = config_obj.get(args.section, args.key)
    print('[√] 查询 SECTION:{section} 下 KEY:{key} 的值为:{value}'.format(section=args.section, key=args.key, value=value))


def add_operation(args):
    """
    在 section 下键添加 KEY 的值
    :return:
    """
    config_path = os.path.join(os.path.dirname(pkg_resources.resource_filename(__name__, '')), 'conf/Modules.ini')
    config_obj = configparser.ConfigParser()
    config_obj.read(config_path)
    config_obj.add_section(args.section, )
    config_obj.set(args.section, args.key, args.value)
    with open(config_path, "w") as f:
        config_obj.write(f)
    print('[√] 添加 SECTION:{section} 下 KEY:{key} 的值为:{value}'.format(section=args.section, key=args.key, value=args.value))


def modify_operation(args):
    """
    在 section 下键修改 KEY 的值
    :return:
    """
    config_path = os.path.join(os.path.dirname(pkg_resources.resource_filename(__name__, '')), 'conf/Modules.ini')
    config_obj = configparser.ConfigParser()
    config_obj.read(config_path)
    config_obj.set(args.section, args.key, args.value)
    with open(config_path, "w") as f:
        config_obj.write(f)

    print('[√] 修改 SECTION:{section} 下 KEY:{key} 的值为:{value}'.format(section=args.section, key=args.key, value=args.value))


def delete_operation(args):
    """
    在 section 下键删除 KEY 的值
    :return:
    """
    config_path = os.path.join(os.path.dirname(pkg_resources.resource_filename(__name__, '')), 'conf/Modules.ini')
    config_obj = configparser.ConfigParser()
    config_obj.read(config_path)
    # remove_section 是删除整个 section
    config_obj.remove_option(args.section, args.key)
    with open(config_path, "w") as f:
        config_obj.write(f)

    print('[√] 删除 SECTION:{section} 下 KEY:{key}'.format(section=args.section, key=args.key))


def parse_entry():
    """
    脚本选项解析，当前支持 doctor, resign 选项
    """
    parser = argparse.ArgumentParser()
    sub_parsers = parser.add_subparsers()

    doctor_parser = sub_parsers.add_parser("doctor", help="检查依赖环境")
    doctor_parser.set_defaults(callback=run_doctor)
    doctor_parser.add_argument("--verbose", action="store_true", help="输出详细的检查日志")

    query_parser = sub_parsers.add_parser("query", help="查询 SECTION 某个 KEY 的值")
    query_parser.set_defaults(callback=query_operation)
    query_parser.add_argument("-s", "--section", help="SECTION 段名称", required=True)
    query_parser.add_argument("-k", "--key", help="KEY 键名称", required=True)

    add_parser = sub_parsers.add_parser("add", help="添加 KEY - VALUE 键值对到 SECTION 下")
    add_parser.set_defaults(callback=add_operation)
    add_parser.add_argument("-s", "--section", help="SECTION 段名称", required=True)
    add_parser.add_argument("-k", "--key", help="KEY 键名称", required=True)
    add_parser.add_argument("-v", "--value", help="字段新值", required=True)

    modify_parser = sub_parsers.add_parser("modify", help="修改 SECTION 下某个 KEY 的值")
    modify_parser.set_defaults(callback=modify_operation)
    modify_parser.add_argument("-s", "--section", help="SECTION 段名称", required=True)
    modify_parser.add_argument("-k", "--key", help="KEY 键名称", required=True)
    modify_parser.add_argument("-v", "--value", help="字段新值", required=True)

    delete_parser = sub_parsers.add_parser("delete", help="删除 SECTION 下某个 KEY")
    delete_parser.set_defaults(callback=delete_operation)
    delete_parser.add_argument("-s", "--section", help="SECTION 段名称", required=True)
    delete_parser.add_argument("-k", "--key", help="KEY 键名称", required=True)

    args = parser.parse_args()
    args.callback(args)


if __name__ == '__main__':
    parse_entry()
