#RTbatch

Python script for batch porcessing in [RawTherapee](https://en.wikipedia.org/wiki/RawTherapee).

It can currenly process one file while iterating through a list of profiles, and generate useful template code for publishing resulting images on [Octopress](https://github.com/imathis/octopress). 
RTbatch also supports automated creation of optimized mini images for web previews, all customizable from within the command line.

##Installation

###Portage (Gentoo)

RTbatch is available in the [Portage](http://en.wikipedia.org/wiki/Portage_(software)) *[chymerc overlay](https://github.com/TheChymera/chymeric)* as **app-misc/RTbatch**.
Just run the following command:

```
emerge RTbatch
```

If you do not have the Chymeric overlay enable yet, you will also need to have run the following beforehand:

```
echo "PORTDIR_OVERLAY=\"/usr/local/portage/chymeric\"" >> /etc/portage/make.conf
git clone https://github.com/TheChymera/chymeric.git /usr/local/portage/chymeric
```


###PIP (Python Easy Install)

If you do not use Gentoo, or any other distribution with easy Portage integration, the package can easily be installed via pip. 

```
git clone https://github.com/TheChymera/RTbatch.git your/local/repository/path
pip install [--user] -e your/local/repository/path
```

###Dependencies:

* [**Chr-helpers**](https://github.com/TheChymera/chr-helpers) - available on Gentoo as [dev-python/chr-helpers](https://github.com/TheChymera/chymeric/tree/master/dev-python/chr-helpers)!

##Usage


Released under the GPLv3 license.
Project led by Horea Christian (address all correspondence to: h.chr@mail.ru)
