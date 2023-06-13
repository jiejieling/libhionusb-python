#!/srv/python3/bin/python3

from setuptools import setup, find_packages

# # 导入静态文件
# file_data = [
#     ("smart/static", ["smart/static/icon.svg", "smart/static/config.json"]),
# ]

# 第三方依赖
requires = [
    'pywin32==305'
]

# 自动读取包信息
about = {}
with open('hionusb/__version__.py', 'r') as f:
    exec(f.read(), about)

setup(
    name=about['__name__'],  # 包名称
    version=about['__version__'],  # 包版本
    description=about['__description__'],  # 包详细描述
    long_description=about['__description__'],  # 长描述，通常是readme，打包到PiPy需要
    author=about['__author__'],  # 作者名称
    author_email=about['__author_email__'],  # 作者邮箱
    url='https://github.com/jiejieling/libhionusb-python.git',
    packages=find_packages(),  # 项目需要的包
    install_requires=requires,  # 第三方库依赖
    zip_safe=False,  # 此项需要，否则卸载时报windows error
    #data_files=file_data,  # 打包时需要打包的数据文件，如图片，配置文件等
    #include_package_data=True,  # 是否需要导入静态数据文件
)
