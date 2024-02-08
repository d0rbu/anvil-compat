import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name='anvil-compat',
    version='1.0.2',
    author='d0rb',
    description='A Minecraft anvil file format parser.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/d0rbu/anvil-compat',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'nbt',
        'frozendict',
    ],
    include_package_data=True
)
