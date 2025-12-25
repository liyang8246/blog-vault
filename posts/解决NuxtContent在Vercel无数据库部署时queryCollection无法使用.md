---
date: 2025-12-25
tags:
  - frontend
  - tutorial
  - vue
description: Nuxt Content部署Vercel时服务端渲染报错, 需手动配置libsql数据库类型和路径解决. 
---
一些相关的 issue [#2378](https://github.com/nuxt/content/issues/2378) [#3548](https://github.com/nuxt/content/issues/3548) 但是好像和我的情况也并不是完全一样

# 错误分析

在 [NuxtConent文档](https://content.nuxt.com/docs/deploy/vercel) 中写到

> Nuxt Content projects can be deployed to Vercel with zero configuration. The module will automatically detect a Vercel environment and will prepare the necessary configuration for deployment.
> 
> By default module will use SQlite database in Vercel located at /tmp directory.

但是用起来根本不是这么回事, 当第一次访问网站或刷新的时候, 执行服务端渲染, `queryCollection` 会报错

``` plaintext
[request error] [unhandled] [POST] http://localhost/__nuxt_content/posts/query?v=v3.5.0--sQOL_VDT2UvjJojMgyr9A2dCR_p4vKKfAomhLcxsIvQ
 H3Error: Module did not self-register: '/var/task/node_modules/better-sqlite3/build/Release/better_sqlite3.node'.
    at Object..node (node:internal/modules/cjs/loader:1865:18)
    ... 8 lines matching cause stack trace ...
    at require (node:internal/modules/helpers:147:16) {
  cause: Error: Module did not self-register: '/var/task/node_modules/better-sqlite3/build/Release/better_sqlite3.node'.
      at Object..node (node:internal/modules/cjs/loader:1865:18)
      at Module.load (node:internal/modules/cjs/loader:1441:32)
      at Function.<anonymous> (node:internal/modules/cjs/loader:1263:12)
      at /opt/rust/nodejs.js:2:13531
      at Function.dn (/opt/rust/nodejs.js:2:13909)
      at Ye.e.<computed>.Je._load (/opt/rust/nodejs.js:2:13501)
      at TracingChannel.traceSync (node:diagnostics_channel:322:14)
      at wrapModuleLoad (node:internal/modules/cjs/loader:237:24)
      at Module.require (node:internal/modules/cjs/loader:1463:12)
      at require (node:internal/modules/helpers:147:16) {
    code: 'ERR_DLOPEN_FAILED'
  },
  statusCode: 500,
  fatal: false,
  unhandled: true,
  statusMessage: undefined,
  data: undefined
}
```

但是如果手动切换一下路由, 此时是客户端渲染, `queryCollection` 会使用客户端的数据库查询, 就能正常使用, 所以一定是服务端的数据库出了问题.

# 解决方法

结果多次测试发现, 只要手动指定一下 database 就可以用了

```typescript [file=nuxt.config.ts]
{
  content: {
    database: {
      type: 'libsql',
      url: 'file:/tmp/content.db',
    },
  }
}
```
