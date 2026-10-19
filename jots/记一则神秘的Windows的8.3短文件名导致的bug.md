---
date: 2026-07-29
tags:
  - rust
---
## 问题描述

在我们的程序中, 使用 `std::env::temp_dir()` 获取临时路径的地址, 返回值为 `C:\Users\ADMINI~1\AppData\Local\Temp` 但是我们并没有 `ADMINI~1` 用户, 我们的用户名是 `Administer` , 这导致了后续大量逻辑判断出了问题

## bug 原因

`Administer` 超过了 8 个字符, 回退到了 DOS 兼容 8.3 短文件名, 就变成了 ADMIN~1, 实际上是同一个路径, 但是我们的程序在使用字符串判断路径, 导致了 bug

## 怎么办

用 `fs::canonicalize`

`canonicalize` 是什么? 自己问AI, :)
