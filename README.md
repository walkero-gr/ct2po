# ct2po
Convert .ct/.cd Amiga translation files to .po/.pot files.

The goal is to be able to use online platform for translations and bring more translations to the Amiga platform. [Flexcat](https://github.com/adtools/flexcat) is able to convert the gettext po files to catalogs which can be distributed with an application.

## Usage

```bash
  -h, --help            show this help message and exit
  -tr TRFILE, --tr-file TRFILE
                        The source translation (.cd/.ct) file
  -po POFILE, --po-file POFILE
                        The generated .po/.pot file
  -ln LANG, --lang LANG
                        The language of the translation
  -pn PRJN, --project-name PRJN
                        Project name and version
```

To create a .pot file, which will be the source for the translations a .cd  file needs to be used as the source file. This can be done like
```bash
ct2po.py -tr app.cd -po app.pot -ln en -pn "My App 1.0"
```

To convert a .ct file to .po the following command can be used:
```bash
ct2po.py -tr app.ct -po greek.po -ln el -pn "My App 1.0"
```

## Issues

Please have a look at the Issues section for some features/bugs that are not implemented yet. Until they are fixed I would recommend the usage of an application like [POEdit](https://poedit.net/) which could fix those issues automatically.

# Similar software

Alternatively, the [cd2po.sh](https://raw.githubusercontent.com/jens-maus/yam/master/scripts/cd2po.sh) by Jens Maus can be used which generates a little bit different files, but they are more compatible with what Flexcat expects to find.