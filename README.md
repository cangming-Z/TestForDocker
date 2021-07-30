1、生成requirements.txt
（1）安装pipreqs依赖
  pip install pipreqs
（2）生成文件
  项目根目录下执行
  pipreqs ./
  Windows系统下直接使用会出现编码错误UnicodeDecodeError: 'gbk' codec can't decode byte 0xad in position 173: illegal multibyte sequence，所以在使用时要指定编码格式
  pipreqs ./ --encoding=utf8
