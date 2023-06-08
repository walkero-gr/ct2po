#!python
# coding=utf-8
import sys, argparse, codecs
import langs

lang = langs.langsHandler()

class helpersHandler:
    def noLC(self, line):
        return line.replace("\n", "")

    def isRef(self, line):
        return line.startswith("MSG_")

    def isIdStr(self, line):
        return line.startswith("; ")

    def isBlockEnd(self, line):
        if self.noLC(line) == ";":
            return True

        return False

    def cleanParenthesis(self, line):
        st = line.find("(")
        return line[0:st].strip()

    def isCatalogDescription(self, filename):
        return filename.endswith(".cd")

def main(argv):
    hlpr = helpersHandler()
    appDescr = "Convert .ct Amiga translation files to .po\nDeveloped by George Sokianos"

    if len(argv) == 0:
        print ("No arguments given. Use ct2po -h for more info.\nThe script must be used from the shell.")
        sys.exit()

    # Parse the arguments
    argParser = argparse.ArgumentParser(description=appDescr, epilog="",
                                        formatter_class=argparse.RawDescriptionHelpFormatter)
    argParser.add_argument('-tr', '--tr-file', action='store', dest='trfile', help='The source translation (.cd/.ct) file')
    argParser.add_argument('-po', '--po-file', action='store', dest='pofile', help='The generated .po/.pot file')
    argParser.add_argument('-ln', '--lang', action='store', dest='lang', help='The language of the translation')
    argParser.add_argument('-pn', '--project-name', action='store', dest='prjn', help='Project name and version')
    args = argParser.parse_args()

    if args.trfile == None:
        print ("Please provide source translation (.cd/.ct) file.\n")
        sys.exit()
    if args.pofile == None:
        print ("Please provide the generated .po filename.\n")
        sys.exit()
    if args.lang == None:
        print ("Please provide the language of the translation.\n")
        sys.exit()
    if args.prjn == None:
        args.prjn = ''

    try:
        isCDfile = hlpr.isCatalogDescription(args.trfile)
        fsrc = codecs.open(args.trfile, 'r', encoding=lang.getEncoding(args.lang))
        ftrg = open(args.pofile, "w+")

        refFound = None  # reference found flag
        endBlockFound = None

        referenceStr = None
        idStr = None
        translatedStr = None

        ftrg.write('msgid ""\n')
        ftrg.write('msgstr ""\n')
        ftrg.write('"Project-Id-Version: %s\\n"\n' % (args.prjn))
        ftrg.write('"POT-Creation-Date: \\n"\n')
        ftrg.write('"PO-Revision-Date: \\n"\n')
        ftrg.write('"Last-Translator: \\n"\n')
        ftrg.write('"Language-Team: \\n"\n')
        ftrg.write('"Language: %s\\n"\n' % (args.lang))
        ftrg.write('"MIME-Version: 1.0\\n"\n')
        ftrg.write('"Content-Type: text/plain; charset=UTF-8\\n"\n')
        ftrg.write('"Content-Transfer-Encoding: 8bit\\n"\n')
        ftrg.write('"X-Generator: ct2po.py\\n"\n\n')

        line = fsrc.readline()
        while line:
            # print (line)

            if hlpr.isBlockEnd(line) and not hlpr.isIdStr(line):
                if referenceStr:
                    ftrg.write("%s\n" % (hlpr.noLC(referenceStr)))
                if idStr:
                    ftrg.write("msgid \"%s\"\n" % (hlpr.noLC(idStr)))
                if translatedStr:
                    if isCDfile:
                        ftrg.write("msgid \"%s\"\n" % (hlpr.noLC(translatedStr)))
                        ftrg.write("msgstr \"\"\n\n")
                    else:
                        ftrg.write("msgstr \"%s\"\n\n" % (hlpr.noLC(translatedStr)))
                referenceStr = None
                refFound = None
                idStr = None
                translatedStr = None
                endBlockFound = True


            if hlpr.isRef(line):
                line = hlpr.cleanParenthesis(line)
                referenceStr = "#: %s" % (line)
                if not refFound:
                    refFound = True     # This means that the first translation block found

            if referenceStr != None and hlpr.isIdStr(line):
                if idStr == None:
                    idStr =  line.replace("; ", "")
                else:
                    idStr = ''.join([idStr, line.replace("; ", "")])

            if referenceStr != None and not hlpr.isRef(line) and not hlpr.isIdStr(line) and not hlpr.isBlockEnd(line):
                if translatedStr == None:
                    translatedStr =  line
                else:
                    translatedStr = ''.join([translatedStr, line])

            if not refFound:
                ftrg.write("#. %s\n" % (hlpr.noLC(line)))

            line = fsrc.readline()


        # Write the last lines of the translations
        if idStr:
            ftrg.write("%s\n" % (hlpr.noLC(idStr)))
        if translatedStr:
            ftrg.write("%s\n" % (hlpr.noLC(translatedStr)))


        ftrg.close()
        fsrc.close()
    except (IOError, UnicodeDecodeError):
        print (IOError["reason"])


    sys.exit()


if __name__ == "__main__":
    main(sys.argv[1:])
