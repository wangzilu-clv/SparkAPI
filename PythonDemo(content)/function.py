import os
def load_file(content):
    number=1
    while os.path.exists('resume{}.txt'.format(number)):
        number+=1
    if "工作经历" and "求职意向" and "自我评价"and "学历" in content:
        with open('resume{}.txt'.format(number), 'w',encoding='utf-8') as f:
            f.write(content)
        f.close()
        number+=1






