from setuptools import setup

setup(
    name="Rejoui",
    version="1.0.0",
    install_requires=["packageA", "packageB"],
    extras_require={
        "develop": ["dev-packageA", "dev-packageB"]
    },
    entry_points={
        "console_scripts": [
            "foo = package_name.module_name:func_name",
            "foo_dev = package_name.module_name:func_name [develop]"
        ],
        "gui_scripts": [
            "bar = gui_package_name.gui_module_name:gui_func_name"
        ]
    }
)

from setuptools import setup

setup(
    name = 'Rejoui',
    version = '1.0.0',
    url = 'https://github.com/sakuragi-zero/data_pipeline.git',
    license = 'Free',
    author = 'iwata & sauragi',
    author_email = '---',
    description = 'このパッケージはデータの分析を行う上で必要なデータ加工やモデルの作成を簡単に、再帰的に行えるようにする',
    # install_requires = ['setuptools'],
    packages = ["sakuragi-zero.data_pipeline"],
    entry_points = {
        'console_scripts': [
            'data_reshape = sakuragi-zero.data_pipeline.sakuragi_v2.py:data_reshape',
        ]
    }
)
