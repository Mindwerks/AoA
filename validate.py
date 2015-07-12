#!/usr/bin/python


# bethesda files
morrowind_md5 = None
with open("copyright/morrowind.md5", 'r') as content_file:
    morrowind_md5 = content_file.read()
    
tribunal_md5 = None
with open("copyright/tribunal.md5", 'r') as content_file:
    tribunal_md5 = content_file.read()
    
bloodmoon_md5 = None
with open("copyright/bloodmoon.md5", 'r') as content_file:
    bloodmoon_md5 = content_file.read()
    

def validate(md5_list, version):
    print "\nComparing md5sum of AoA version %s to the contents Bethesda's BSA files." % version
    beth_counter = 0
    for line in md5_list.split('\n'):
        if len(line) > 0:
            md5, file_name = line.split("  ")
            if md5 in morrowind_md5:
                beth_counter += 1
                print "Found in Morrowind.bsa", md5, file_name
            if md5 in tribunal_md5:
                beth_counter += 1
                print "Found in Tribunal.bsa", md5, file_name
            if md5 in bloodmoon_md5:
                beth_counter += 1
                print "Found in Bloodmoon.bsa", md5, file_name
                
    print "Out of %d files, found %d bethesda files.\n" % (len(md5_list.split('\n'))-1, beth_counter)

    
# aoa files
aoav10_md5 = None
with open("manifest/aoav10.md5", 'r') as content_file:
    aoav10_md5 = content_file.read()
    validate(aoav10_md5, "1.0")


aoav11_md5 = None
with open("manifest/aoav11.md5", 'r') as content_file:
    aoav11_md5 = content_file.read()
    validate(aoav11_md5, "1.1")


