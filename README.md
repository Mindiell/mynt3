# mynt

_Another static site generator?_

With the ever growing population of static site generators, all filling a certain need, I've yet to find one that allows the generation of anything but the simplest of blogs.

That's where mynt comes in, being designed to give you all the features of a CMS with none of the often rigid implementations of those features.


### Information about my conversion to python 3

As I was lurking on the internet, I found out that [pyladies][pyladies] were using [mynt][mynt] and that it was stucked on python 2 version only.

So I did some conversion work in order to upgrade mynt to python 3.8. This is clearly a partial work for now but mynt3 is working and I tend to finish this conversion and add some testing in the near future in order to help anybody using it to reach the present ;o)

As I will contact Anomareh (author of mynt), maybe this repo will die and the official one will use my code in order to give users a clean way to upgrade.


### Install

From PyPI:

    $ pip install mynt

Latest trunk:

    $ pip install git+https://github.com/Mindiell/mynt3.git


### Getting started

After installing mynt head on over and give the [quickstart][quickstart] page and [docs][docs] a read.


### Dependencies

+ [Hoep][hoep]
+ [Jinja2][jinja]
+ [Pygments][pygments]
+ [PyYAML][pyyaml]
+ [watchdog][watchdog]

#### Optional

+ [Docutils][docutils] _(reST)_


### Support

If you run into any issues or have any questions, either open an [issue][issues] or hop in #mynt on irc.freenode.net.


[docs]: http://mynt.uhnomoli.com/
[docutils]: http://docutils.sourceforge.net/
[hoep]: https://github.com/Anomareh/Hoep
[issues]: https://github.com/Mindiell/mynt3/issues
[jinja]: http://jinja.pocoo.org/
[pygments]: http://pygments.org/
[pyyaml]: http://pyyaml.org/
[quickstart]: http://mynt.uhnomoli.com/docs/quickstart/
[watchdog]: http://packages.python.org/watchdog/
[pyladies]: https://pyladies.com/
[mynt]: https://github.com/Anomareh/mynt
