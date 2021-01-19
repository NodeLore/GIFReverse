import os, sys, imageio, shutil
from PIL import Image

# 默认对此目录进行待拼接各帧图片的存放或者获取
defaultPath = 'gif'

# 分解GIF并保存到默认目录
def splitGIF(path):
    if not os.path.exists(path):
        print('%s不存在' % path)
        sys.exit(1)
    if not os.path.exists(defaultPath):
        os.mkdir(defaultPath)
    image = Image.open(path)
    i = 0
    try:
        while True:
            image.seek(i)
            image.save(os.path.join(defaultPath, '%d.png' % i))
            i += 1
    except:
        pass
    print('共获取%d帧图片，保存到%s目录下' % (i, defaultPath))

# 从默认目录拼接GIF
# reverseOrNot反转选项
def generateGIF(path, reverseOrNot=True):
    if not '.gif' in path:
        path += '.gif'
    images = []
    fileNums = len(os.listdir(defaultPath))
    for i in range(fileNums):
        image = imageio.imread(os.path.join(defaultPath, '%d.png' % ((fileNums - i - 1) if True == reverseOrNot else i)))
        images.append(image)
    imageio.mimsave(path, images, 'GIF')
    print('%s保存成功' % path)

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        mode = sys.argv[1]
        path = sys.argv[2]
        if mode == 's':
            splitGIF(path)
        elif mode == 'g':
            generateGIF(path, False)
        elif mode == 'r':
            generateGIF(path)
        elif mode == 'f' and len(sys.argv) == 4:
            newPath = sys.argv[3]
            splitGIF(path)
            generateGIF(newPath)
            shutil.rmtree(defaultPath)
        else:
            print('模式参数错误')
    else:
        print('参数不正确')
        print('Usage: python split.py [command] [targetPath] ([newPath])')
        print('\tcommand: s[拆分] g[合并] r[反转合并] f[快速反转合并]')