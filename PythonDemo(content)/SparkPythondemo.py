# coding: utf-8
import SparkApi
import time
import function
#以下密钥信息从控制台获取   https://console.xfyun.cn/services/bm35
appid = "1597eef5"     #填写控制台中获取的 APPID 信息
api_secret = "NGViN2I4OTM2NjlhZDIyNWZiZWIzNWFl"   #填写控制台中获取的 APISecret 信息
api_key ="f69ed50ae237015ec323768c22c5aef9"    #填写控制台中获取的 APIKey 信息

domain = "4.0Ultra"      # Max版本
#domain = "generalv3"       # Pro版本
#domain = "general"         # Lite版本

Spark_url = "wss://spark-api.xf-yun.com/v4.0/chat"   # Max服务地址
#Spark_url = "wss://spark-api.xf-yun.com/v3.1/chat"  # Pro服务地址
#Spark_url = "wss://spark-api.xf-yun.com/v1.1/chat"  # Lite服务地址

#初始上下文内容，当前可传system、user、assistant 等角色
text =[
    {"role": "system", "content": "你是一个公司的hr，可以帮助求职者评价与优化简历，请对求职者的简历进行优化，只需要直接输出简历就行，不需要输出其他内容，以文本格式进行输出"}, # 设置对话背景或者模型角色
    # {"role": "user", "content": "你是谁"},  # 用户的历史问题
    # {"role": "assistant", "content": "....."} , # AI的历史回答结果
    # # ....... 省略的历史对话
    # {"role": "user", "content": "你会做什么"}  # 最新的一条问题，如无需上下文，可只传最新一条问题
]


def getText(role,content):
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)

    #if role=="assistant":
    #     function.load_file(content)
    return text

def getlength(text):
    length = 0
    for content in text:
        temp = content["content"]
        leng = len(temp)
        length += leng
    return length

def checklen(text):
    while (getlength(text) > 8000):
        del text[0]
    return text
    


if __name__ == '__main__':

    while(1):
        Input = input("\n" +"求职者:")
        #question = checklen(getText("user",Input))
        question = getText("user", Input)
        SparkApi.answer =""
        print("星火:",end ="")
        SparkApi.main(appid,api_key,api_secret,Spark_url,domain,question)
        #print(SparkApi.answer)
        function.load_file(SparkApi.answer)
        getText("assistant",SparkApi.answer)




