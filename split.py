import os, sys, imageio
from PIL import Image

# 默认对此目录进行待拼接各帧图片的存放或者获取
defaultPath = 'gif'

if __name__ == '__main__':
    if len(sys.argv) == 3:
        path = sys.argv[2]
        if sys.argv[1] == 's':
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
            except Exception as e:
                pass
            print('共获取%d帧图片，保存到%s目录下' % (i, defaultPath))
        elif sys.argv[1] == 'g':
            if not '.gif' in path:
                path += '.gif'
            images = []
            fileNums = len(os.listdir(defaultPath))
            for i in range(fileNums):
                image = imageio.imread(os.path.join(defaultPath, '%d.png' % (fileNums - i - 1)))
                images.append(image)
            imageio.mimsave(path, images, 'GIF')
            print('%s保存成功' % path)
        else:
            print('模式参数错误')
    else:
        print('参数数量不正确')
        print('Usage: python split.py [command] [targetPath]')
        print('\tcommand: s[拆分] g[合并]')