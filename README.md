maker\_parame51
===============


Presentation
------------

This repo is a maker-repository. It stores the parameters and the STL-files of parts made with *desi51*, *desi52*, *desi53* and *desi53b*.
The designs come from the following javascript packages:
- [desi51-cli](https://www.npmjs.com/package/desi51-cli)
- [desi51-uis](https://www.npmjs.com/package/desi51-uis)
- [desi51](https://charlyoleg2.github.io/parame51/)
- [desi52-cli](https://www.npmjs.com/package/desi52-cli)
- [desi52-uis](https://www.npmjs.com/package/desi52-uis)
- [desi52](https://charlyoleg2.github.io/parame52/)
- [desi53-cli](https://www.npmjs.com/package/desi53-cli)
- [desi53-uis](https://www.npmjs.com/package/desi53-uis)
- [desi53](https://charlyoleg2.github.io/parame53/)
- [desi53b](https://charlyoleg2.github.io/parame53b/)


Requirements
------------

- [node](https://nodejs.org) > 22.00.0
- [npm](https://docs.npmjs.com/cli) > 11.0.0


### Optional requirements

- [OpenSCAD](https://openscad.org/)

For Ubuntu users, *OpenSCAD* is available on [snapcraft](https://snapcraft.io/openscad) and can be installed with:

```bash
sudo snap install openscad
```

Upgrade
-------

For working with the latest *desi82* version:

```bash
npm outdated
npm update --save
git commit -am 'npm update --save'
```


Dev
---

```bash
git clone https://github.com/charlyoleg2/maker_parame51
cd maker_parame51
npm install
npm run
npm run desi82-uis
npx desi82-uis
npx desi82-cli --help
./make_parts.js
```

Vocabulary
----------

- Design: A parametrizable 3D parts. Desginix is a collection of designs.
- Part or Reference: A particular parametrization of a design.
- Instance: The realization of a reference.


References for the maker\_parame51
-----------------------------------

ID | Reference           | Design             | Nb of instances
---|---------------------|--------------------|----------------
1  | myPartA             | myPartA            | 1
2  | myPartB             | myPartB            | 1
3  | myPartC             | myPartC            | 1
4  | myPartD             | myPartD            | 1
5  | myPartE             | myPartE            | 1
6  | myPartF             | myPartF            | 1
7  | myPartG             | myPartG            | 1
8  | myPartH             | myPartH            | 1
9  | myPartI             | myPartI            | 1
10 | myPartJ             | myPartJ            | 1
11 | myPartK             | myPartK            | 1
12 | myPartL             | myPartL            | 1
13 | myPartM             | myPartM            | 1
14 | myPartN             | myPartN            | 1
15 | myPartO             | myPartO            | 1
16 | myPartP             | myPartP            | 1
17 | myPartQ             | myPartQ            | 1
18 | myPartR             | myPartR            | 1
19 | myPartS             | myPartS            | 1
20 | myPartT             | myPartT            | 1
21 | myPartU             | myPartU            | 1
22 | myPartV             | myPartV            | 1
23 | myPartW             | myPartW            | 1

Each reference has its own directory with its json-parametrization, scad-script and stl-file.


