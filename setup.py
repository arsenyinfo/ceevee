from setuptools import setup


def parse_requirements(filename):
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


setup(
    name="ceevee",
    version="0.0.1",
    author="[ods.ai] Arseny Kravchenko",
    description="Deep learning based baselines for various problems",
    package_dir={'': './'},
    packages=['ceevee'],
    include_package_data=True,
    install_requires=parse_requirements("requirements.txt")
)
