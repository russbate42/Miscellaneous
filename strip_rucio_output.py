file_names_stripped = []
with open('rucio_2023data_output.txt', 'rb') as handle:
    for line in handle.readlines():
        linestr = str(line.rstrip())
        if not 'user.mswiatlo' in str(line):
            continue
        
        sublines = linestr.split('|')
        for subline in sublines:
            if '.root' in subline:
                file_names_stripped.append(subline.strip())

with open('rucio_2023_filesnames.txt', 'w') as handle:
    for fname in file_names_stripped:
        subfname = fname.split(':')[-1]
        print(subfname)
        handle.writelines(subfname)

