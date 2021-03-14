# 工作日历 📅

通过 Github Action，生成工作日历 📅 数据

在线访问地址（Base64）：

https://cdn.jsdelivr.net/gh/tonyc726/work-calendar@main/dist/data.js

使用方法：

```Typescript
// window.atob 与 window.bota 处理中文会乱码
JSON.parse(decodeURIComponent(atob(DATA)))

// ...
```

Schema：
```JSON
[
  [
    // date,
    '2020-01-01',
    // description
    'xxxxxx',
    // 0: 上班， 1: 放假
    1
  ]
]
```

---

Made by Tony ([blog](https://itony.net))
