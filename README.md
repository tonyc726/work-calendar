# 工作日历 📅

通过 Github Action，生成工作日历 📅 数据

在线访问地址（Base64）：

https://cdn.jsdelivr.net/gh/tonyc726/work-calendar@master/dist/data.js

使用方法：

```Typescript
fetch('https://cdn.jsdelivr.net/gh/tonyc726/work-calendar@master/dist/data.js')
  .then((dataBuffer) => dataBuffer.text())
  .then((dataBase64Str) => {
    // Buffer -> Base64 -> String -> decodeURIComponent -> JSON.parse >>> JSON
    const data = JSON.parse(decodeURIComponent(atob(dataBase64Str)));

    /**
     * TODO...
     *
     * ```JSON
     * [
     *   [
     *     // date,
     *     '2020-01-01',
     *     // description
     *     'xxxxxx',
     *     // 0: 上班， 1: 放假
     *     1
     *   ]
     * ]
     * ```
     */
  });
```

---

Made by Tony ([blog](https://itony.net))
