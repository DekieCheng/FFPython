from setuptools import setup, find_packages

setup(
    name="dekiefirstpymodule",  # 包名
    version="0.4",  # 版本号
    packages=find_packages(),  # 自动发现所有包
    install_requires=[
        # 列出你的依赖包
    ],
    author="dekie",  # 作者名
    author_email="dekie.cheng@flex.com",  # 作者邮箱
    description="A brief description of your package dekiefirstpymodule build from Github on 0.4 version.",  # 简短描述
    long_description="This is my first pyton package uploaded from git hub."
)
