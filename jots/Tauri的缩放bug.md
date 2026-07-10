## 问题描述

在 Windows 上关闭 `性能选项` 里的 `拖动时显示窗口内容` , 应用以 100% 缩放启动后 将系统缩放调整为 125%, 主窗口的 WebView 内容放大了 但 Window 框架没有跟着变大 导致出现滚动条

## 原因

问题出在 [tauri/tao](https://github.com/tauri-apps/tao) 的 `WM_DPICHANGED` 处理中：

``` rust [tao/src/platform_impl/windows/event_loop.rs]
if !is_show_window_contents_while_dragging_enabled() {
    new_physical_inner_size = old_physical_inner_size;
}
```

## 来源

2024 年 1 月，[tauri#8499](https://github.com/tauri-apps/tauri/issues/8499) [tao PR #858](https://github.com/tauri-apps/tao/pull/858) 报告：当 "拖动时显示窗口内容" 关闭时，在多显示器不同缩放之间拖动窗口会导致窗口尺寸异常变大。

> "当 `拖动时显示窗口内容` 关闭时，Windows 会在拖拽完成时自动调整窗口大小，所以 tao 不应该再额外调整，否则会双重缩放。"

在这个 Issue 里, 他出现了和我们类似的问题, 但是他是跨屏幕的尺寸缩放, windows 在这里会主动(应该是主动)缩放窗口, 但是在调整显示设置的缩放时没有主动调整导致了 bug

## 咋办

我也不知道咋办, 目前我是在 ts 里手动处理一下

``` ts
  mainWindow.onScaleChanged(async () => {
    if (handlingScaleChange) return
    handlingScaleChange = true

	await mainWindow.setSize(new LogicalSize(width, height))
	
    setTimeout(() => {
	  handlingScaleChange = false
	}, 200)
  })
```

## 相关信息

[winit#4119](https://github.com/rust-windowing/winit/pull/4119)、[winit#4341](https://github.com/rust-windowing/winit/pull/4341)
