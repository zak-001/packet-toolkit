
from setuptools import setup, find_packages

setup(
    name="packinjection",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "click==8.2.1",
	"markdown-it-py==3.0.0",
	"mdurl==0.1.2",
	"Pygments==2.19.2",
	"rich==14.1.0",
	"scapy==2.6.1"
    ],
)
