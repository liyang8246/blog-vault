---
date: 2025-12-19
tags:
  - frontend
  - vue
description: Nuxt项目中better-sqlite3模块报错解决方案 确保安装VS C++开发环境, 清理依赖并重新编译原生模块.
---
# 错误现象

安装 `nuxt-content` 模块并选择 `better-sqlite3` , 启动开发服务器会报错

```powershell
ERROR  Could not locate the bindings file. Tried:                                                                                                                         17:58:08  
 → C:\Users\xxx\Desktop\nuxt-blog\node_modules\.pnpm\better-sqlite3@12.5.0\node_modules\better-sqlite3\build\better_sqlite3.node
 → C:\Users\xxx\Desktop\nuxt-blog\node_modules\.pnpm\better-sqlite3@12.5.0\node_modules\better-sqlite3\build\Debug\better_sqlite3.node
 → C:\Users\xxx\Desktop\nuxt-blog\node_modules\.pnpm\better-sqlite3@12.5.0\node_modules\better-sqlite3\build\Release\better_sqlite3.node
 → C:\Users\xxx\Desktop\nuxt-blog\node_modules\.pnpm\better-sqlite3@12.5.0\node_modules\better-sqlite3\out\Debug\better_sqlite3.node
 → C:\Users\xxx\Desktop\nuxt-blog\node_modules\.pnpm\better-sqlite3@12.5.0\node_modules\better-sqlite3\Debug\better_sqlite3.node
 → C:\Users\xxx\Desktop\nuxt-blog\node_modules\.pnpm\better-sqlite3@12.5.0\node_modules\better-sqlite3\out\Release\better_sqlite3.node
 → C:\Users\xxx\Desktop\nuxt-blog\node_modules\.pnpm\better-sqlite3@12.5.0\node_modules\better-sqlite3\Release\better_sqlite3.node
 → C:\Users\xxx\Desktop\nuxt-blog\node_modules\.pnpm\better-sqlite3@12.5.0\node_modules\better-sqlite3\build\default\better_sqlite3.node
 → C:\Users\xxx\Desktop\nuxt-blog\node_modules\.pnpm\better-sqlite3@12.5.0\node_modules\better-sqlite3\compiled\24.12.0\win32\x64\better_sqlite3.node
 → C:\Users\xxx\Desktop\nuxt-blog\node_modules\.pnpm\better-sqlite3@12.5.0\node_modules\better-sqlite3\addon-build\release\install-root\better_sqlite3.node
 → C:\Users\xxx\Desktop\nuxt-blog\node_modules\.pnpm\better-sqlite3@12.5.0\node_modules\better-sqlite3\addon-build\debug\install-root\better_sqlite3.node
 → C:\Users\xxx\Desktop\nuxt-blog\node_modules\.pnpm\better-sqlite3@12.5.0\node_modules\better-sqlite3\addon-build\default\install-root\better_sqlite3.node
 → C:\Users\xxx\Desktop\nuxt-blog\node_modules\.pnpm\better-sqlite3@12.5.0\node_modules\better-sqlite3\lib\binding\node-v137-win32-x64\better_sqlite3.node

    at bindings (node_modules\.pnpm\bindings@1.5.0\node_modules\bindings\bindings.js:126:9)
    at new Database (node_modules\.pnpm\better-sqlite3@12.5.0\node_modules\better-sqlite3\lib\database.js:48:64)
    at getDB (/C:/Users/xxx/Desktop/nuxt-blog/node_modules/.pnpm/db0@0.3.4_better-sqlite3@12.5.0/node_modules/db0/dist/connectors/better-sqlite3.mjs:17:9)
    at Object.exec (/C:/Users/xxx/Desktop/nuxt-blog/node_modules/.pnpm/db0@0.3.4_better-sqlite3@12.5.0/node_modules/db0/dist/connectors/better-sqlite3.mjs:24:18)
    at getLocalDatabase (/C:/Users/xxx/Desktop/nuxt-blog/node_modules/.pnpm/@nuxt+content@3.9.0_better-sqlite3@12.5.0_magicast@0.5.1/node_modules/@nuxt/content/dist/module.mjs:358:16)
    at async processCollectionItems (/C:/Users/xxx/Desktop/nuxt-blog/node_modules/.pnpm/@nuxt+content@3.9.0_better-sqlite3@12.5.0_magicast@0.5.1/node_modules/@nuxt/content/dist/module.mjs:3038:14)
    at async /C:/Users/xxx/Desktop/nuxt-blog/node_modules/.pnpm/@nuxt+content@3.9.0_better-sqlite3@12.5.0_magicast@0.5.1/node_modules/@nuxt/content/dist/module.mjs:3012:20       
    at async initNuxt (/C:/Users/xxx/Desktop/nuxt-blog/node_modules/.pnpm/nuxt@4.2.2_@parcel+watcher@_124526d42cee1f867208ff68a27f3ce1/node_modules/nuxt/dist/index.mjs:5390:3)   
    at async #initializeNuxt (/C:/Users/xxx/Desktop/nuxt-blog/node_modules/.pnpm/@nuxt+cli@3.31.3_cac@6.7.14_magicast@0.5.1/node_modules/@nuxt/cli/dist/dev-BKPehGZf.mjs:492:3)   
    at async NuxtDevServer.init (/C:/Users/xxx/Desktop/nuxt-blog/node_modules/.pnpm/@nuxt+cli@3.31.3_cac@6.7.14_magicast@0.5.1/node_modules/@nuxt/cli/dist/dev-BKPehGZf.mjs:384:3)

 ERROR  Could not locate the bindings file. Tried:                                                                                                                         17:58:08  
 → C:\Users\xxx\Desktop\nuxt-blog\node_modules\.pnpm\better-sqlite3@12.5.0\node_modules\better-sqlite3\build\better_sqlite3.node
 → C:\Users\xxx\Desktop\nuxt-blog\node_modules\.pnpm\better-sqlite3@12.5.0\node_modules\better-sqlite3\build\Debug\better_sqlite3.node
 → C:\Users\xxx\Desktop\nuxt-blog\node_modules\.pnpm\better-sqlite3@12.5.0\node_modules\better-sqlite3\build\Release\better_sqlite3.node
 → C:\Users\xxx\Desktop\nuxt-blog\node_modules\.pnpm\better-sqlite3@12.5.0\node_modules\better-sqlite3\out\Debug\better_sqlite3.node
 → C:\Users\xxx\Desktop\nuxt-blog\node_modules\.pnpm\better-sqlite3@12.5.0\node_modules\better-sqlite3\Debug\better_sqlite3.node
 → C:\Users\xxx\Desktop\nuxt-blog\node_modules\.pnpm\better-sqlite3@12.5.0\node_modules\better-sqlite3\out\Release\better_sqlite3.node
 → C:\Users\xxx\Desktop\nuxt-blog\node_modules\.pnpm\better-sqlite3@12.5.0\node_modules\better-sqlite3\Release\better_sqlite3.node
 → C:\Users\xxx\Desktop\nuxt-blog\node_modules\.pnpm\better-sqlite3@12.5.0\node_modules\better-sqlite3\build\default\better_sqlite3.node
 → C:\Users\xxx\Desktop\nuxt-blog\node_modules\.pnpm\better-sqlite3@12.5.0\node_modules\better-sqlite3\compiled\24.12.0\win32\x64\better_sqlite3.node
 → C:\Users\xxx\Desktop\nuxt-blog\node_modules\.pnpm\better-sqlite3@12.5.0\node_modules\better-sqlite3\addon-build\release\install-root\better_sqlite3.node
 → C:\Users\xxx\Desktop\nuxt-blog\node_modules\.pnpm\better-sqlite3@12.5.0\node_modules\better-sqlite3\addon-build\debug\install-root\better_sqlite3.node
 → C:\Users\xxx\Desktop\nuxt-blog\node_modules\.pnpm\better-sqlite3@12.5.0\node_modules\better-sqlite3\addon-build\default\install-root\better_sqlite3.node
 → C:\Users\xxx\Desktop\nuxt-blog\node_modules\.pnpm\better-sqlite3@12.5.0\node_modules\better-sqlite3\lib\binding\node-v137-win32-x64\better_sqlite3.node
```

# 错误分析
这是因为 `better-sqlite3` 是 `nodejs` 原生模块, 需要编译安装

# 错误处理
1. 确保安装了 `Visual Studio` 里的 `C++桌面开发` 套件
2. 在 `devDependencies` 中添加 `better-sqlite3`
3. 在 `onlyBuiltDependencies` 中添加 `better-sqlite3`
```json [package.json]
{
  "dependencies": { ... },
  "devDependencies": {
    "better-sqlite3": "x.x.x"
  },
  "pnpm": {
    "onlyBuiltDependencies": [
      "better-sqlite3"
    ]
  }
}
```
4. 删除 `node_modules`
5. 清除一下 `pnpm` 存储 `pnpm store prune`
6. 现在应该可以正常运行了