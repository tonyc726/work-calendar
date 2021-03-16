#!/usr/local/bin/python3

from pathlib import Path
import os
import json
import base64

def reduceDataFromDir(dir):
    print('# 正在读取目录：`' + str(dir) + '`')
    reduceData = []
    for home, dirs, files in os.walk(dir):
        print('# > 目录中共 ' + str(len(files)) + ' 个文件')
        for filename in files:
            fullname = os.path.join(home, filename)
            print('# >> 正在读取：' + filename)
            with open(fullname) as json_file:
                data = json.load(json_file)
                print('# >>> ' + filename + ' 中共 ' + str(len(data)) + ' 条数据')
                for day in data:
                    date = day.get('date')
                    description = day.get('description')
                    isHoliday = day.get('isHoliday')
                    simplifyDay = [date, description,
                                   1 if isHoliday == True else 0]
                    existedDay = [x for x in reduceData if x[0] == date]
                    if not existedDay:
                        reduceData.append(simplifyDay)
                    else:
                        existedDay = simplifyDay
        print('# > 共聚合数据：' + str(len(reduceData)) + ' 条')
        return reduceData


if __name__ == "__main__":
    sourceDir = (Path(os.getcwd(), './data')).resolve()
    reduceSourceData = reduceDataFromDir(sourceDir)
    reduceDataStr = json.dumps(reduceSourceData)
    reduceDataStrBase64 = base64.b64encode(reduceDataStr.encode())

    distFilePath = (Path(os.getcwd(), './dist', 'data.js')).resolve()
    print('# 正在写入至：`' + str(distFilePath) + '`')
    with open(distFilePath, 'wt') as distFile:
        distFile.write(reduceDataStrBase64.decode())
        distFile.close()
    print('# ✅ 写入成功！')
