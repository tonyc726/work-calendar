# 工作日历 📅

通过 Github Action，生成工作日历 📅 数据

在线访问地址（Base64）：

https://bluetron-work-calendar-data.vercel.app/data.js

备用地址：
https://cdn.jsdelivr.net/gh/tonyc726/work-calendar@master/dist/data.js

使用方法：

```Typescript
fetch('https://cdn.jsdelivr.net/gh/tonyc726/work-calendar@master/dist/data.js')
  .then((dataBuffer) => dataBuffer.text())
  .then((dataBase64Str) => {
    // Base64 String -> atob -> JSON.parse >>> JSON
    const data = JSON.parse(atob(dataBase64Str));

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
     *     // isHoliday 0: 上班， 1: 放假
     *     1
     *   ]
     * ]
     * ```
     */
  });
```

---

Made by Tony ([blog](https://itony.net))
