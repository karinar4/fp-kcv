import setuptools

setuptools.setup(
    name="diabetes-prediction",
    version="1",
    author="Karina Rahmawati",
    author_email="karinarahmawati219@gmail.com",
    description="Diabetes Prediction",
    url="https://github.com/karinar4/fp-kcv",
    install_requires=open('requirements.txt').read().split('\n'),
    include_package_data=True,
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
