import argparse
from PIL import Image

#此处是采用argparse，直接在doc界面进行参数输入
parser=argparse.ArgumentParser()
parser.add_argument('file')
#设置图像的输入路径
parser.add_argument('-o','--output')
#设置最后文件的输出路径，此处进行了参数简化，用-o代替-output
parser.add_argument('--width',type=int,default=100)
parser.add_argument('--height',type=int,default=80)
args=parser.parse_args()
#第5，12行是固定的，通过arg来接受参数

IMG=args.file
WIDTH=args.width
HEIGHT=args.height
OUTPUT=args.output

charList=list("123456789QWERTYUIOPLKJHGFDSAZXCCVF123456789QWERTYUIOPLKJHGFDSAZXCCVF")
def get_char(r,g,b,alpha=256):		
	length=len(charList)
	gray=int(0.2126 * r + 0.7152 * g + 0.0722 * b)
	unit=(256+1)/length
	return charList[int(gray/unit)]

if __name__=='__main__':

#如果在终端运行此程序，则进行下列程序
	img=Image.open(IMG)
	img=img.resize((WIDTH,HEIGHT),Image.NEAREST)

	txt=""

	for i in range(HEIGHT):
		for j in range(WIDTH):
			txt += get_char(*img.getpixel((j,i)))
		txt += '\n'
#对txt里加子符的方法可以借鉴一下

#下面的部分是对字符串txt进行文件写入，并输出
#用with的方法的好处是替代了try exception finally
	print(txt)
	if OUTPUT:
		with open(OUTPUT,'w') as f:
			f.write(txt)
	else:
		with open("outout.txt",'w') as f:
			f.write(txt)
