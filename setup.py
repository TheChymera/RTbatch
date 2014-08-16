from distutils.core import setup
setup(
    name="RTbatch",
    packages = ["RTbatch"], # this must be the same as the name above
    version="",
    description = "Command line batch functionality for RawTherapee",
    author = "Horea Christian",
    author_email = "h.chr@mail.ru",
    url = "https://github.com/TheChymera/RTbatch",
    heywords = ["batch", "RawTherapee", "plugin"],
    py_modules = ["RTbatch"],
    classifiers = [],
    install_requires=[
	"chr-helpers>=9999"
    ],
    dependency_links = [
    "https://github.com/TheChymera/chr-helpers/tarball/master#egg=chr-helpers-9999"
    ]
    )
