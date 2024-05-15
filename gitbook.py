import os
import shutil

dirs = {
    '.\\408\\操作系统\\full'  : 'os',
    '.\\408\\计算机网络\\full': 'network',
    '.\\408\\数据结构\\full'  : 'datastruct',
    #'.\\数学\\高等数学\\note' : 'advenced_math'
}

dirs = [
    ('.\\408\\操作系统\\full'  , 'os', '操作系统'),
    ('.\\408\\计算机网络\\full', 'network', '计算机网络'),
    ('.\\408\\数据结构\\full'  , 'datastruct', '数据结构'),
    #('.\\数学\\高等数学\\note' , 'advenced_math', '高等数学')
]


gitPath = '.\\.gitbook'

def merge_folders(source, destination):
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)

        if os.path.isdir(source_path):
            if os.path.isdir(destination_path):
                merge_folders(source_path, destination_path)
            else:
                shutil.copytree(source_path, destination_path)
        else:
            shutil.copy2(source_path, destination_path)


def setupGitbook():
    if os.path.exists(gitPath):
        shutil.rmtree(gitPath)
    
    os.mkdir(gitPath)
    imagePath = gitPath + '\\image'
    os.mkdir(imagePath)
    for k in dirs:
        childPath = f'{gitPath}\\{k[1]}'
        os.mkdir(childPath)
        for fileName in os.listdir(k[0]):
            filePath = f'{k[0]}\\{fileName}'
            if os.path.isfile(filePath) and fileName.endswith('.md'):
                shutil.copy2(filePath, f'{childPath}\\{fileName}')
        merge_folders(k[0] + '\\image', imagePath)

def createSummary():
    summaryPath = f'{gitPath}\\SUMMARY.md'
    with open(summaryPath, 'w') as sum:
        for k in dirs:
            dirPath = gitPath + '\\' + k[1]
            buf = []
            for fName in os.listdir(f'.\\{gitPath}\\{k[1]}'):
                buf.append(f'    * [{fName[:-3]}](.\\{k[1]}\\{fName})')
            readme = dirPath + '\\' + 'README.md'
            with open(readme, 'w') as rm:
                rm.write(' ')
            sum.write(f'* [{k[2]}](.\\{k[1]}\\README.md)\n')
            for b in buf:
                sum.write(b + '\n')
            sum.write('\n\n')

if __name__ == '__main__':
    setupGitbook()
    createSummary()