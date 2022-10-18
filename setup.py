from setuptools import setup

setup(
    name = 'data_pipeline.sakuragi_v2',
    version = '1.0.0',
    url = 'https://github.com/sakuragi-zero/data_pipeline.git',
    license = 'Free',
    author = 'iwata & sauragi',
    # author_email = '---',
    description = 'このパッケージはデータの分析を行う上で必要なデータ加工やモデルの作成を簡単に、再帰的に行えるようにする',
    # install_requires = ['setuptools'],
    packages = ["data_pipeline.sakuragi_v2"],
    entry_points = {
        'console_scripts': [
            'data_reshape = sakuragi-zero.data_pipeline.sakuragi_v2:data_reshape',
        ]
    }
)
