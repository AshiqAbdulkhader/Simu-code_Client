from setuptools import setup,find_packages

setup(
    name='Simu-Code',
    version='1.0',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask==1.1.2',
        'requests==2.25.0',
        'gunicorn==20.0.4',
        'flask_wtf',
        'wtforms'
        ]
)
