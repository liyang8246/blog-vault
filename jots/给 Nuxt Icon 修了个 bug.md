---
date: 2025-12-20
tags:
  - frontend
  - vue
---
[issue](https://github.com/nuxt/icon/issues/453)
[pull request](https://github.com/nuxt/icon/pull/454)

当我在项目中使用 `material-icon-theme` 图标包时，出现了一个警告：

```powershell
WARN  [Icon] Collection material-icon-theme is not found locally
We suggest to install it via npm i -D @iconify-json/material-icon-theme to provide the best end-user experience.
```

并且 `clientBundle: { scan: true }` 对 `material-icon-theme` 也不起作用。

然而，我已经确认自己已经安装了 `@iconify-json/material-icon-theme`，并且其他所有集合都能正常工作。

在查阅 `nuxt-icon` 源代码时，我注意到一些集合（包括 `material-icon-theme`）并未包含在 `collection-names.ts` 中。

我发现这个文件是通过 `scripts/collections.ts` 生成的。在重新运行该脚本后，`material-icon-theme` 出现在了 `collection-names` 里，并且在我的项目中运行正常。

其实本文就是中文版的 issue :)