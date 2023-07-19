import setuptools

setuptools.setup(
    name="ImgTextClipboard-python",  # 库的名字
    version='0.1',  # 库的版本号，后续更新的时候只需要改版本号就行
    author="LanluZ",  # 你的你的名字
    description="Convenient to operate clipboard related images by oneself",  # 介绍
    long_description_content_type="text/markdown",
    url='https://github.com/LanluZ/ImgTextClipboard-python',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
# 注意：没有注释的地方不要改
