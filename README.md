#RTbatch

Python script for batch porcessing in [RawTherapee](https://en.wikipedia.org/wiki/RawTherapee).

It can currenly process one file while iterating through a list of profiles, and generate useful template code for publishing resulting images on [Octopress](https://github.com/imathis/octopress). 
RTbatch also supports automated creation of optimized mini images for web previews, all customizable from within the command line.

##Installation

####On [Gentoo Linux](http://en.wikipedia.org/wiki/Gentoo_linux) and [Derivatives](http://en.wikipedia.org/wiki/Category:Gentoo_Linux_derivatives):

RTbatch is available in the [Portage](http://en.wikipedia.org/wiki/Portage_(software)) *[chymeric overlay](https://github.com/TheChymera/chymeric)* as **[app-misc/RTbatch](https://github.com/TheChymera/chymeric/tree/master/app-misc/RTbatch)**.
Just run the following command:

```
emerge RTbatch
```

*If you are not yet using this overlay, it can be enabled with just two commands, as seen in [the README](https://github.com/TheChymera/chymeric).*

####On all other Operating Systems:

For all other Linux distributions or operating systems, the package can easily be installed via [pip](http://en.wikipedia.org/wiki/Pip_(Python)).
This also handles all Python dependencies.

```
git clone https://github.com/TheChymera/RTbatch.git your/local/repository/path
pip install [--user] -e your/local/repository/path
```

*Please bear in mind that this will not pull in RawTherapee, make sure you have already installed it.*

###Dependencies:

####Mandatory:
* [**chr-helpers**](https://github.com/TheChymera/chr-helpers) - in Portage (chymeric overlay) as [**dev-python/chr-helpers**](https://github.com/TheChymera/chymeric/tree/master/dev-python/chr-helpers)!
* [**RawTherapee**](http://en.wikipedia.org/wiki/RawTherapee) - in Portage as **media-gfx/rawtherapee**

##Usage
Run the script either as `RTbatch_cli` (if installed globally), or as `./RTbatch_cli.py` from the containing folder:
```
RTbatch_cli  [-h] [-f] [-m] [-w MINI_WIDTH] [-i IPTC_PROFILE]
		[-o OUTPUT_DIR] [-t TEMPLATE]
		input
```

Example:
```
RTbatch_cli -fm ~/path/to/your/pics/folder/DSC_1337.NEF -t octopress-imgcap -i ~/.config/RawTherapee4.1/profiles/your_custom_profile.pp3
```

##Arguments

```
positional arguments:
  input                 Input file for RT processing

optional arguments:
  -h, --help            show this help message and exit
  -f, --fullsize-only   Export files only in full-size - default exports both
                        full-size and minis (thumbnails)
  -m, --minis-only      Export files only as thumbnails (minis) - default
                        exports both full-size and minis
  -w MINI_WIDTH, --mini-width MINI_WIDTH
                        Thumbnail (mini) width
  -i IPTC_PROFILE, --iptc-profile IPTC_PROFILE
                        Path to IPTC profile (defaults to
                        .../RTbatch/profiles/iptc.pp3)
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        Specify the output directory (by default
                        .../RTbatch/output/)
  -t TEMPLATE, --template TEMPLATE
                        Markup template for obtaining a codeblock with which
                        you can display your images (choose from under
                        .../RTbatch/templates)
```

---
Released under the GPLv3 license.
Project led by Horea Christian (address all correspondence to: h.chr@mail.ru)
